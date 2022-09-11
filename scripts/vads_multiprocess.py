import argparse
import sys

from copy import deepcopy
from scipy.signal import lfilter

import numpy as np
from tqdm import tqdm
import soundfile as sf
import os.path as osp

from multiprocessing import Pool
from functools import partial
_root = ""
_gc = 0

def get_parser():
    parser = argparse.ArgumentParser(description="compute vad segments")
    parser.add_argument(
        "--rvad-home",
        "-r",
        help="path to rvad home (see https://github.com/zhenghuatan/rVADfast)",
        required=True,
    )

    parser.add_argument('--ori_file',type=str,help='path to tsv file',required=True)
    parser.add_argument('--vad_file',type=str,help='gene vad file',required=True)
    parser.add_argument('--cpus',type=int,default=8,help='multi processing num of cores')

    return parser


def rvad(path):
    winlen, ovrlen, pre_coef, nfilter, nftt = 0.025, 0.01, 0.97, 20, 512
    ftThres = 0.5
    vadThres = 0.4
    opts = 1

    import speechproc
    
    global _root
    global _gc
    _gc += 1
    if _gc % 1 == 0:
        print(_gc,"per core parsed",path)
    #s()
    data, fs = sf.read(path)
    assert fs == 16000, "sample rate must be 16khz"
    ft, flen, fsh10, nfr10 = speechproc.sflux(data, fs, winlen, ovrlen, nftt)

    # --spectral flatness --
    pv01 = np.zeros(ft.shape[0])
    pv01[np.less_equal(ft, ftThres)] = 1
    pitch = deepcopy(ft)

    pvblk = speechproc.pitchblockdetect(pv01, pitch, nfr10, opts)

    # --filtering--
    ENERGYFLOOR = np.exp(-50)
    b = np.array([0.9770, -0.9770])
    a = np.array([1.0000, -0.9540])
    fdata = lfilter(b, a, data, axis=0)

    # --pass 1--
    noise_samp, noise_seg, n_noise_samp = speechproc.snre_highenergy(
        fdata, nfr10, flen, fsh10, ENERGYFLOOR, pv01, pvblk
    )

    # sets noisy segments to zero
    for j in range(n_noise_samp):
        fdata[range(int(noise_samp[j, 0]), int(noise_samp[j, 1]) + 1)] = 0

    vad_seg = speechproc.snre_vad(
        fdata, nfr10, flen, fsh10, ENERGYFLOOR, pv01, pvblk, vadThres
    )
    return vad_seg, data


def main():
    parser = get_parser()
    args = parser.parse_args()

    sys.path.append(args.rvad_home)

    stride = 160
    # lines = sys.stdin.readlines()
    #


    num_lines = sum(1 for line in open(args.ori_file, 'r', encoding="utf8"))
    rf = open(args.ori_file, 'r', encoding="utf8").readlines()
    wf = open(args.vad_file, 'a+', encoding="utf8")

    _root = rf[0].rstrip()
    #print(_root)
    rf = [osp.join(_root, path.split()[0]) for path in rf[1:]]
    p = Pool(args.cpus)


    func = partial(rvad)


    for rslt in tqdm(p.imap(func, rf, chunksize=256),total=num_lines-1):
        vads, wav = rslt
        #print("done")

        start = None
        vad_segs = []
        for i, v in enumerate(vads):
            if start is None and v == 1:
                start = i * stride
            elif start is not None and v == 0:
                vad_segs.append((start, i * stride))
                start = None
        if start is not None:
            vad_segs.append((start, len(wav)))

        print(" ".join(f"{v[0]}:{v[1]}" for v in vad_segs))
        wf.write(" ".join(f"{v[0]}:{v[1]}" for v in vad_segs)+'\n')



    # for fpath in tqdm(lines[1:]):
    #     path = osp.join(root, fpath.split()[0])
    #     vads, wav = rvad(speechproc, path)
    #
    #     start = None
    #     vad_segs = []
    #     for i, v in enumerate(vads):
    #         if start is None and v == 1:
    #             start = i * stride
    #         elif start is not None and v == 0:
    #             vad_segs.append((start, i * stride))
    #             start = None
    #     if start is not None:
    #         vad_segs.append((start, len(wav)))
    #
    #     print(" ".join(f"{v[0]}:{v[1]}" for v in vad_segs))


if __name__ == "__main__":
    main()

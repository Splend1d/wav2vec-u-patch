# wav2vec-u-patch
Repository for the paper [Analyzing the Robustness of Unsupervised Speech Recognition](https://arxiv.org/abs/2110.03509), including patches to wav2vec-u and analysis code
## Env setup
Follow https://github.com/facebookresearch/fairseq/tree/main/examples/wav2vec/unsupervised
This is a patch to the w2v2-u repo, to successfully run, merge all content in this repo with the fairseq repo



## Patches to w2vu
### removing silence from audio faster
```
python scripts/vads.py -r $RVAD_ROOT < /path/to/train.tsv > train.vads
# removing silence from audio
```
could be time consuming, to make sure progress is saved and the program is still running, run the following patch instead.
```
export GAN_SPEECH_DATA=data/TED/TEDLIUM_release-3/wav_line/train
export LIBRI_ROOT=~/$GAN_SPEECH_DATA
export SAVE_ROOT=workspace/$GAN_SPEECH_DATA

python divide_and_conquer_data.py workspace/$GAN_SPEECH_DATA/raw
for i in {0..100};
do
    echo "splt ${i}"
    python scripts/vads_multiprocess.py -r $RVAD_ROOT --ori_file $SAVE_ROOT/raw/train.tsv.${i} --vad_file $SAVE_ROOT/raw/train.vads.${i};
done;
python divide_and_conquer_data.py workspace/$GAN_SPEECH_DATA/raw
```
divide_and_conquer_data.py will both divide the tsv into chunks, and merge the finished chunks.

### variety-text-corpus
other text corpus (LibriLM, wiki103...) is hosted on https://www.kaggle.com/datasets/a24998667/variety-text-corpus

### calculate per
run ```calculate_per.ipynb``` to calculate per

### calculate jsd
cd to ```analysis/JSD```
After prepare_text.sh get phone sequences samples from ```lm.phones.filtered.txt```
samples should look like ```./data/LibriLM.raw``` and ```./data/LibriSpeech9.6.raw```
then execute
```
bash run_jsda.sh ${1st corpus name} ${2nd corpus name}
# for example
bash run_jsda.sh LibriLM.raw LibriSpeech9.6.raw
# the jsd result will be printed on the screen
```

## How to run code on TWCC

twcc -> 建立開發型容器 -> custom image -> pytorch-21.06-py3:UnsupervisedASR8

*90GB好像不夠，建議可選2GPU,180G的setting

進去之後執行
```conda activate /ASR```
(注意：'/' is mandatory)

These PATH are created upon conda activation 
```
FAIRSEQ_ROOT=/ASR/pkgs/fairseq/
RVAD_ROOT=/ASR/pkgs/fairseq/examples/wav2vec/unsupervised/rVADfast
KENLM_ROOT=/ASR/pkgs/fairseq/examples/wav2vec/unsupervised/kenlm/build/bin/
KALDI_ROOT=/ASR/pkgs/pykaldi/tools/kaldi/
LD_LIBRARY_PATH=/ASR/pkgs/pykaldi/tools/kaldi/src/lib/
```
PYTHONPATH is appended with /ASR/site-packages, however, this may overwrite the original site-package location, if you install another package, you might need to add that path to PYTHONPATH
```
wget https://www.dropbox.com/s/c99gcaf6uir8924/runtest
```
When training, do not use $PYTHONPATH=xxx, this will overwrite the needed path, instead, append xxx to $PYTHONPATH.

to obtain a test_run of the pipeline
change ```--config w2vu_testing``` to ```--config w2vu``` for longer(default) training

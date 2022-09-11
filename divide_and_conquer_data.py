# +
import sys
_dir = sys.argv[1]
import os
_tsv_path = os.path.join(_dir,"train.tsv")
with open(_tsv_path,"r") as f:
    header = f.readline()
    data = f.readlines()
flac_total = len(data)
n_splits = len(range(0,len(data),8192))
print(n_splits, "splits","8192 each")

for i in range(0,len(data),8192):
    partdata = data[i:i+8192]
    splt = _tsv_path+"."+str(i//8192)
    with open(splt,"w") as f:
        f.writelines([header]+partdata)

# +

_remove_silence_file_name = "train.vads"

all_data = []
for i in range(n_splits):
    partial_name = _remove_silence_file_name+"."+str(i)
    path = os.path.join(_dir,partial_name)
    with open(path,"r") as f:
        all_data += f.readlines()

print(len(all_data),flac_total)
assert len(all_data) == flac_total
merge_path = os.path.join(_dir,_remove_silence_file_name)
with open(merge_path,"w") as f:
    f.writelines(all_data)
# -



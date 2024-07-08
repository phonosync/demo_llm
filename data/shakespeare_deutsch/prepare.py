import os
import tiktoken
import numpy as np

# download the tiny shakespeare dataset
input_file_path = 'data/shakespeare_deutsch/shakespeare_deutsch_komplett.txt'

with open(input_file_path, 'r') as f:
    data = f.read()
print(f"length of dataset in characters: {len(data):,}")

enc = tiktoken.get_encoding("gpt2")
def encode(s):
    return enc.encode(s, allowed_special={"<|endoftext|>"})
def decode(l):
    return enc.decode(l)

# create the train and test splits
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode both to integers
train_ids = encode(train_data)
val_ids = encode(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

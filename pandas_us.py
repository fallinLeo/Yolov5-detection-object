import pandas as pd
import json

with open(r'C:\Users\Dell\Desktop\traffic_dataset\train_dataset\train.json') as f:
    js = json.loads(f.read())
df = pd.DataFrame(js)

df = pd.read_json('train.json')
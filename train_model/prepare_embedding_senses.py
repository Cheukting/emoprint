import csv
from easybert import Bert
import time
import os
import pickle
from tqdm import tqdm

dataset = pickle.load(open("pickled/refined_dataset.p", "rb"))
try:
    embedded_vector_map = pickle.load(open("pickled/embedded_vector_map.p", "rb"))
except:
    embedded_vector_map = {}

print("==========")
print("**Bert embedding is in process")
bert = Bert("https://tfhub.dev/google/bert_multi_cased_L-12_H-768_A-12/1")
start = time.time()
count = 0
try:
    for emoji, info_dict in tqdm(dataset.items()):
        for emoji in embedded_vector_map:
            continue
        collected_sentances = []
        for pos in info_dict['senses'].values():
            if len(pos) > 0:
                for sense in pos:
                    definision_list = list(sense.values())[0]
                    for definision in definision_list:
                        if definision not in collected_sentances:
                            collected_sentances.append(definision)
        collencted_embedded = []
        for sentances in tqdm(collected_sentances):
            collencted_embedded.append(bert.embed(sentances.lower()))
        embedded_vector_map[emoji] = collencted_embedded
        count += 1
    end = time.time()
    print(f"time for embedding {count} emoji: {(end-start)/60}mins")
finally:
    pickle.dump(embedded_vector_map, open("pickled/embedded_vector_map.p", "wb"))

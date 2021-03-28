from easybert import Bert
from scipy import spatial
import pickle

embedded_vector_map = pickle.load(open("pickled/embedded_vector_map.p", "rb"))
bert = Bert("https://tfhub.dev/google/bert_multi_cased_L-12_H-768_A-12/1")

def pick_emoji(input_str):
    input_embedded = bert.embed(input_str.lower())
    min_dist = None
    for emoji, embedded_list in embedded_vector_map.items():
        for vector in embedded_list:
            distance = spatial.distance.cosine(input_embedded, vector)
            if (min_dist is None) or (distance < min_dist):
                pick = emoji
                min_dist = distance
    return pick

pricked = pick_emoji("sad")
print(pricked)

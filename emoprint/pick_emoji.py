import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from easybert import Bert
from scipy import spatial
import pickle
import os

this_dir = os.path.dirname(os.path.realpath(__file__))
embedded_vector_map = pickle.load(open(this_dir + "/pickled/embedded_vector_map.p", "rb"))
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

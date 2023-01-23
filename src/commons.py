import os
import pickle
import editdistance
from unidecode import unidecode

def fish_in_list(name, l):
    l = [s.lower() for s in l]
    name = unidecode(name.lower())

    similars = []
    for s in l:
        ed = editdistance.eval(unidecode(s), name)
        if (ed <= 2) or (name in unidecode(s)):
            similars.append(s)

    return similars


def list_to_pickle(l, filepath):
    with open(filepath, 'wb') as fp:
        pickle.dump(l, fp)

def pickle_to_list(filepath):
    assert os.path.exists(filepath)
    with open (filepath, 'rb') as fp:
        l = pickle.load(fp)
    return l


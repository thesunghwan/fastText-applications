import numpy, random
from scipy import spatial
word_vectors = []

with open('model.vec') as f:
    for line in f:
        splitted_line = line.split()
        word_vectors.append({
            "word": splitted_line.pop(0),
            "vector": numpy.array(list(map(float, splitted_line))),
            "cosine_similarity": 0
        })

word_to_test = {
    "word": "삼성전자",
    "vector": None,
    "cosine_similarity": 0
}

for word_vector in word_vectors:
    if word_vector["word"] == word_to_test["word"]:
        word_to_test["vector"] = word_vector["vector"]

word_vectors.pop(0)
max_cosine_vector = word_vectors.pop(0)

#max_cosine_word = next (iter (word_vectors.keys()))
#max_cosine_word_vector = word_vectors[max_cosine_word]
#print(max_cosine_word_vector)
max_cosine_vector["cosine_similarity"] = 1 - spatial.distance.cosine(word_to_test["vector"], max_cosine_vector["vector"])
for word_vector in word_vectors:
    if max_cosine_vector["vector"].shape[0] == word_vector["vector"].shape[0]:
        word_vector["cosine_similarity"] = 1 - spatial.distance.cosine(word_to_test["vector"], word_vector["vector"])

from operator import itemgetter
newlist = sorted(word_vectors, key=itemgetter('cosine_similarity'), reverse=True)

for i in range(150):
    print(newlist[i]["word"], newlist[i]["cosine_similarity"])

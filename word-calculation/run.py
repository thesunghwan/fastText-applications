import numpy, random, sys
from scipy import spatial

given_words = []
with open("result/temp.txt") as f:
    for line in f:
        splitted_line = line.split()
        given_words.append({
            "word": splitted_line.pop(0),
            "vector": numpy.array(list(map(float, splitted_line)))
        })

word1 = given_words[0]
word2 = given_words[1]
word3 = given_words[2]

question_vector = word1["vector"] - word2["vector"] + word3["vector"]

word_vectors = []
with open("result/text9.vec") as f:
    for line in f:
        splitted_line = line.split()
        word_vectors.append({
            "word": splitted_line.pop(0),
            "vector": numpy.array(list(map(float, splitted_line))),
            "cosine_similarity": 0
        })

word_vectors.pop(0)

for word_vector in word_vectors:
    if(word_vector["word"] != word1["word"] and word_vector["word"] != word2["word"] and word_vector["word"] != word3["word"]):
        word_vector["cosine_similarity"] = 1 - spatial.distance.cosine(question_vector, word_vector["vector"])

from operator import itemgetter
newlist = sorted(word_vectors, key=itemgetter('cosine_similarity'), reverse=True)

print(newlist[0]["word"])

"""for i in range(10):
    print(newlist[i]["word"])"""

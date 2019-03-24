import nltk
from nltk.util import bigrams, trigrams
from collections import Counter
from operator import itemgetter
import re


f = open("arabhistory.txt", encoding='utf-8')
words=""
for line in f:

    words+=line

words = re.split('[-_,.\s]', words)
# print(words)

wordsCounter = list(Counter(words).items())
wordsCounter = sorted(wordsCounter, key=lambda x: x[1])
wordsCounter = [list(i) for i in wordsCounter]
print(wordsCounter)

biGrams = list(bigrams(words))
# print(len(biGrams))
biGramsCounter = list(Counter(biGrams).items())
biGramsCounter = sorted(biGramsCounter, key=lambda x: x[1])
biGramsCounter = [list(i) for i in biGramsCounter]
print(biGramsCounter)

triGrams = list(trigrams(words))
# print(len(triGrams))
triGramsCounter = list(Counter(triGrams).items())
triGramsCounter = sorted(triGramsCounter, key=lambda x: x[1])
triGramsCounter = [list(i) for i in triGramsCounter]
print(triGramsCounter)

def counterReturn(ourTri,Tri):
    for i in Tri:
        if i[0] == ourTri:
            return i[1]
    return 0

def predict(string,biG,triG):
    Probabilities=[]
    for i in biG:
        ourTri = (string,i[0][0],i[0][1])
        triProb = counterReturn(ourTri,triG)/len(triG)
        biProb = counterReturn(i[0],biG)/len(biG)
        totalProb = triProb/biProb
        Probabilities.append([ourTri,totalProb])
    Probabilities=sorted(Probabilities, key=itemgetter(1))
    Probabilities=Probabilities[::-1]
    return Probabilities[0:10]



while True:
    input = str(input())
    print(input)
    g = input.split(" ")
    g = g[-1]

    finalProb=predict(g,biGramsCounter,triGramsCounter)
    for i in finalProb:
        print((i[0][1],i[0][2],i[1]))
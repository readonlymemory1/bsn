# from konlpy.tag import Okt
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import random as rand
from nltk.corpus import reuters


a = [''' '''] #데이터 
# for qsent in sent_tokenize(q[0]):
#     None

# for asent in sent_tokenize(a[0]):
#     None
# model = Word2Vec(sentences=result, vector_size=100, window=5, min_count=5, workers=4, sg=0)
# for i in range(len(q)):
#     qword= word_tokenize(q[i])
#     aword= word_tokenize(a[i])

# print(pos_tag(qword))
manyb = []
result = []
# otk = Okt()
aword = word_tokenize(a[1])
# aword = sen
# aword = otk.morphs(a[2])
def search_rule

def searchAfter(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+1])
        except:
            after.append([""])
    return after

def searchAfter2(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+2])
        except:
            after.append([""])
    return after

def searchAfter3(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+3])
        except:
            after.append([""])
    return after
def searchAfter4(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+4])
        except:
            after.append([""])
    return after

def searchAfter5(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    after = []
    for j in range(len(searchText)):
        try:
            after.append(aword[searchText[j]+5])
        except:
            after.append([""])
    return after


    
def searchBefore(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-1])
    return before 

def searchBefore2(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-2])
    return before 

def searchBefore3(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-3])
    return before 

def searchBefore4(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-4])
    return before 

def searchBefore5(text):
    searchText = list(filter(lambda e:aword[e] == text, range(len(aword))))
    before = []
    for j in range(len(searchText)):
        before.append(aword[searchText[j]-5])
    return before 

def manyText(text):
    global manyb
    global result
    manyb = []
    for i in range(len(text)):
        manyb.append(text.count(text[i]))
        # manyb = set(manyb)
        # text = set(text)
        manyb = list(manyb)
    # try:

    r = rand.randrange(0, 6)
    if r ==0:
        result = text[manyb.index(max(manyb))]
        return result
    elif r ==1:
        result = text[manyb.index(max(manyb))]
        return result
    else:
        ra = rand.randrange(0, len(text))
        return text[ra]
    #many.reverse()
    


# sb5 = manyText(searchBefore(String))

# sbsb5 = searchBefore(sb5[0])
# sbsb2S = searchBefore2(String)
# sb4 = manyText(sbsb5+sbsb2S)

# sbsb4 = searchBefore(sb4[0])
# sbsb25 = searchBefore2(sb5[0])
# sb3 = manyText(sbsb4+sbsb25)

# sbsb3 = searchBefore(sb3[0])
# sbsb24 = searchBefore2(sb4[0])
# sb2 = manyText(sbsb3+sbsb24)

# sbsb2 =searchBefore(sb2[0])
# sbsb23 = searchBefore2(sb3[0])
# sb1 = manyText(sbsb2+sbsb23)

# sa5 = manyText(searchAfter(String))
# sa4 = manyText(searchAfter(sa5[0])+searchAfter2(String))
# sa3 = manyText(searchAfter(sa4[0])+searchAfter2(sa5[0]))
# sa2 = manyText(searchAfter(sa3[0])+searchAfter2(sa4[0]))
# sa1 = manyText(searchAfter(sa2[0])+searchAfter2(sa3[0]))
# generateA = [sb1]+[sb2]+[sb3]+[sb4]+[sb5]+[String]+[sa5]+[sa4]+[sa3]+[sa2]+[sa1] 



String = "I" #중심단어
keyword = "coding"


def typeA(String):
    generateA = [manyText(searchBefore(String))]+[String]+[manyText(searchAfter(String))]
    generateB = [manyText(searchBefore(generateA[0]) + searchBefore2(String))] + generateA + [manyText(searchAfter2(String)+searchAfter(generateA[len(generateA)-1]))]
    generateC = [manyText(searchBefore(generateB[0]) + searchBefore2(generateA[0]) + searchBefore3(String))] + generateB + [manyText(searchAfter3(String)+searchAfter2(generateA[len(generateA)-1])+searchAfter(generateB[len(generateB)-1]))]
    generateD = [manyText(searchBefore(generateC[0]) + searchBefore2(generateB[0]) + searchBefore3(generateA[0])+ searchBefore4(String))]+generateC+[manyText(searchAfter4(String)+searchAfter3(generateA[len(generateA)-1])+searchAfter2(generateB[len(generateB)-1])+searchAfter(generateC[len(generateC)-1]))]
    generateE = [manyText(searchBefore(generateD[0]) + searchBefore2(generateC[0]) + searchBefore3(generateB[0])+ searchBefore4(generateA[0])+searchBefore5(String))]+generateD+[manyText(searchAfter5(String)+searchAfter4(generateA[len(generateA)-1])+searchAfter3(generateB[len(generateB)-1])+searchAfter2(generateC[len(generateC)-1])+searchAfter(generateD[len(generateD)-1]))]
    return generateE

def typeB(String):
    
    generateA = [manyText(searchAfter(String))]
    generateB = generateA + [manyText(searchAfter2(String)+searchAfter(generateA[len(generateA)-1]))]
    generateC = generateB + [manyText(searchAfter3(String)+searchAfter2(generateA[len(generateA)-1])+searchAfter(generateB[len(generateB)-1]))]
    generateD = generateC+[manyText(searchAfter4(String)+searchAfter3(generateA[len(generateA)-1])+searchAfter2(generateB[len(generateB)-1])+searchAfter(generateC[len(generateC)-1]))]
    generateE = generateD+[manyText(searchAfter5(String)+searchAfter4(generateA[len(generateA)-1])+searchAfter3(generateB[len(generateB)-1])+searchAfter2(generateC[len(generateC)-1])+searchAfter(generateD[len(generateD)-1]))]
    return generateE


print("I"+" ".join(typeB(String)))

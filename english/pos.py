import nltk
def clf(corpus):
    text = nltk.word_tokenize(corpus)
    corpus_pos = nltk.pos_tag(text)
    return corpus_pos 
    
def noun(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][0] =="N":
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr
	
def Commoun_noun(k):
	arr=[]
	for i in range(len(k)):
		if k[i][1] =="NN" or k[i][1] =="NNS":
			arr.append(k[i][0])
	return arr

def pronoun(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][:3] =="PRP" or k[i][1][:2] =="WP" :
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr
def adjective(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][0] =="J":
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr
def adverb(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][:2] =="RB"  :
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr

def verb(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][:2] =="VB":
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr
def determiner(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][:3] =="DT": # what are pre determiners
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr
def conjuction_coord(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][:3] =="CC": # what are pre determiners
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr


def interjection(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][:2] =="VH": # what are pre determiners
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr

def preposition(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][:2] =="IN": # what are pre determiners
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr

def modal(k):
    arr=[]
    word=[]
    for i in range(len(k)):
        if k[i][1][0] =="M":
            arr.append(k[i][0])
            word.append(k[i][1])
    
    return arr

def vocab(sent):
	token = clf(sent)
	com = sorted(set(Commoun_noun(token)))
	ver = sorted(set(verb(token)))
	adve = sorted(set(adverb(token)))
	adj = sorted(set(adjective(token)))
	arr_voc = com+ver+adve+adj
	return arr_voc
	
    


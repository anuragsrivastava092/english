import nltk
from random import shuffle,randint
import en
#import sys
#reload(sys)  # Reload does the trick!
#sys.setdefaultencoding('UTF8')
#o = no omission, 1=omission
def clf(corpus):
    text = nltk.word_tokenize(corpus)
    corpus_pos = nltk.pos_tag(text)
    return corpus_pos 

# do not choose sentence having numeral - LS and CD or abbrevation.
# how to handle noun phrase
# &
def count_noun(k):
    nou = ""
    arr = []
    non_noun=[]
    for i in range(len(k)):
        if k[i][1] == "CD" or k[i][1] == "LS" :
            return -1,-1
        elif k[i][1][0] == "N":
            nou += " " + k[i][0]
        else:
            if k[i][0][0] not in [",",".","?",";","'"]:
                non_noun.append(k[i][0])
            if len(nou)>0 :
                arr.append(nou)
            nou = ""
    if len(nou)>0 :
        arr.append(nou)
    return arr,non_noun

def noun_count_ques(sent):
    token = clf(sent)
    noun_li,non_noun = count_noun(token)
    if noun_li == -1:
        return -1
    leng = len(noun_li)
    inst = "Count the no of nouns in the given sentence"
    ans  = leng
    
    if leng == 0:
        inst_arr=[inst,sent]
        option_arr = [0,1,2,3]
        shuffle(option_arr)
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,leng
    else:
        inst_arr = [inst,sent]
        option_arr =[leng,leng+1,leng-1,leng+2]
        shuffle(option_arr)
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,ans,"noun_count",0
#        
def noun_ident_ques(sent):
    token = clf(sent)
    noun_li,non_noun = count_noun(token)
    inst = "Choose the noun"
    if noun_li == -1:
        return -1
    shuffle(noun_li)
    shuffle(non_noun)
    leng_n = len(noun_li)
    leng_on = len(non_noun)
    if leng_on<3:
        return -1
    if leng_n==0 :
        option_arr = ["none"]+ non_noun[:3]
        shuffle(option_arr)
        ans = "none"
        inst_arr = [inst,sent]
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,ans
    elif leng_n>0:
        ans = noun_li[0]
        option_arr = non_noun[:3]+ noun_li[:1]
        shuffle(option_arr)
        inst_arr = [inst,sent]
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,ans,"noun_ident",0

# type of singular _ plural question in nouns
# countable or not, masculine or feminine 
# noun before determiner - either,many,neither,nor
# number  before noun
# plural noun
# simple common noun
# regular plurals
# irregular plurals
# irrgular plural
# error is possible if com_noun accur twice and at one place have non noun tag
# 
def sub_noun_ques(sent):
    token = clf(sent)
    arr=[]
    inst = "Choose the correct option"
    com_sing_noun = []
    com_plu_noun = []
    for i in range(len(token)):
        if token[i][1]=="NN":
            com_sing_noun.append(token[i][0])
        elif token[i][1]=="NNS" :
            com_plu_noun.append(token[i][0])
    if len(com_sing_noun)==0 and len(com_plu_noun)==0:
        return -1
    else :
        shuffle(com_sing_noun)
        shuffle(com_plu_noun)
        if len(com_sing_noun) > 0 :
            com_noun = com_sing_noun[0]
            le = len(com_noun)
            try :
                loc = sent.index(com_noun)
            except ValueError :
                return -1 
            blank = sent[:loc] + "______" +sent[(loc+le):]
            plu = en.noun.plural(com_noun)
            if plu == com_noun:
                option_arr=[com_noun,com_noun+"s",com_noun+"es",com_noun+"ies"]
            elif plu[-3:] == "ies":
                option_arr=[com_noun,plu[:-3]+"s",plu[:-3]+"es",plu]
            elif plu[-2:] == "es":
                option_arr=[com_noun,plu[:-2]+"s",plu[:-2]+"ies",plu]
            elif plu[-1:] == "s":
                option_arr=[com_noun,plu[:-1]+"es",plu[:-1]+"ies",plu]
            else:
                return -1
        elif len(com_plu_noun)>0:
            com_noun = com_plu_noun[0]
            le = len(com_noun)
            try : 
                loc = sent.index(com_noun)
            except ValueError:
                return -1 
            blank = sent[:loc] + "______" +sent[(loc+le):]
            sing = en.noun.singular(com_noun)
            if sing == com_noun:
                option_arr=[com_noun,com_noun+"s",com_noun+"es",com_noun+"ies"]
            else:
                option_arr=[com_noun,sing,]
            
        inst_arr=[inst,blank]
        ans = com_noun
        que_word = ans
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,ans,"sub_noun",1,que_word
        
        
# Me, Myself, And I
def pronoun_cor_ques(sent):
    token = clf(sent)
    inst = "choose the correct"
    arr =[]
    pronoun_1=["I","my","myself","me"]
    pronoun_2=["you","your","yourself","yours"]
    pronoun_3 =["he", "his","himself","him"]
    pronoun_4=["she","her","hers","himself"]
    pronoun_5=["it","its","itself","that"]
    pronoun_6=["we","our","ourselves","us"]
    pronoun_7=["they","their","themselves","them"]
    pronoun_8=["that",  "whichever", "whoever", "whomever"]
    pronoun_9=["which", "who", "whom", "whose"]
    for i in range(len(token)):
        if token[i][1][:3] =="PRP":
            arr.append(token[i][0])
           
    if len(arr) ==0:
        return -1
    else:
        shuffle(arr)
        word = arr[0].lower()
        if word in pronoun_1:
            option_arr = pronoun_1
            ans = word
        elif word in pronoun_2:
            option_arr = pronoun_2
            ans = word
        elif word in pronoun_3:
            option_arr = pronoun_3
            ans = word
            
        elif word in pronoun_4:
            option_arr = pronoun_4
            ans = word
        elif word in pronoun_5:
            option_arr = pronoun_5
            ans = word
        elif word in pronoun_6:
            option_arr = pronoun_6
            ans = word
        elif word in pronoun_7:
            option_arr = pronoun_7
            ans = word
        elif word in pronoun_8:
            option_arr = pronoun_8
            ans = word
        elif word in pronoun_9:
            option_arr = pronoun_9
            ans = word
        else:
            return -1
    
     # how to handle word occuring in between sent
    #print word
    try:
        a= sent.index(word.capitalize())
    except ValueError:
        a=-1
        
    if a==0:
        word = word.capitalize()
        pronoun = word + " "
    else:
        pronoun = " "+ word + " "
    le = len(pronoun)
    try:
        loc = sent.index(pronoun)
    except ValueError:
        return -1 
    blank = sent[:loc] + "______" +sent[(loc+le):]
    # how to generate different options
    inst_arr=[inst,blank]
    que_word = ans
    ans = option_arr.index(ans) + 1
    return option_arr,inst_arr,ans,"pronoun_cor",1,que_word
    
# "Who" vs. "Whom 
def pronoun_wh_ques(sent):
    wh_list1=["That","What","Whatsoever","Whatever"]
    wh_list2=["Who","Whom","Whosoever","Which"]
    inst  = "choose the correct option"
    token = clf(sent)
    arr =[]   
    for i in range(len(token)):
        if token[i][1][:3] =="WP":
            arr.append(token[i][0])
    if len(arr) ==0:
        return -1
    else:
        shuffle(arr)
        word = arr[0]
        if word in wh_list1:
            option_arr = wh_list1
            ans = arr[0]
        elif word in wh_list2:
            option_arr = wh_list2
            ans = arr[0]
        else:
            return -1
    if sent.index(word) == 0:
        
        pronoun = word + " "
    else:
        pronoun = " "+ word + " "
    le = len(pronoun)
    try : 
        loc = sent.index(pronoun)
    except ValueError:
        return -1
    blank = sent[:loc] + "______" +sent[(loc+le):]
    # how to generate different options
    inst_arr=[inst,blank]
    que_word = ans
    ans = option_arr.index(ans) + 1
    return option_arr,inst_arr,ans,"pronoun_wh",1,que_word

# verb 
# auxiliary verb( help verb ) - subject verb agreement, tense
# main VERB COUNt
# Most action verbs are defined as transitive or intransitive
# transitive verb Transitive verbs always receive a direct object:
# bring send owe contain buy show take tell verify check get wash
# finalize annoy lay lend offer edit make phone
# Intransitive verbs do not need a direct
# object in order to complete their meaning. Many are followed by an adjective,
# adverb, preposition or verb complement (gerund or infinitive).
# come explode laugh sit rise excel respond run cough swim emigrate
# smile act cry immigrate lie arrive continue die go
# auxiliary verb - ______ , main verb 
# using nodebox
# be (am, are, is, was, were, being, been),  do (does, did),
# have (has, had, having),shall, will
# have been

aux_pre_simp = ["do","does"]
aux_pre_cont = ["am", "are", "is"]
aux_pre_perf = ["has","have"]
aux_pre_pe_c = ["have been", "has been"]
#past
aux_pas_simp = ["did"] # 2nd form
aux_pas_cont = ["was", "were"]
aux_pas_perf = ["had"]
aux_pre_pe_c = ["had been"]
# are going to
aux_pas_simp = ["will","shall"]
aux_fut_cont = ["shall be", "will be"]
aux_pas_perf = ["will have","shall have"]
aux_pre_pe_c = ["will have been"]

def verb_aux_ques(sent):
    token = clf(sent)
    arr =  []
    inst = "choose the correct"
    for i in range(len(token)):
        if token[i][1][:2] == "VB":
            arr.append(token[i][0])
    if len(arr)==0:
        return -1
    else:
        shuffle(arr)
        ans = arr[0]
        article = " " + ans + " "
        le = len(article)
        try :
            loc = sent.index( article )
        except ValueError:
            return -1
        blank = sent[:loc] + "______" +sent[(loc+le):]
        if ans in ["is","am","are"]:
            option_arr=["is","am","are","none"] # how to generate different options
            inst_arr=[inst,blank]
            
            que_word = ans
            ans = option_arr.index(ans) + 1
            return option_arr,inst_arr,ans,"verb_aux",1,que_word
        elif ans in ["do","does","did"]:
            option_arr=["do","does","did","none"] 
            inst_arr=[inst,blank]
            
            que_word = ans
            ans = option_arr.index(ans) + 1
            return option_arr,inst_arr,ans,"verb_aux",1,que_word
        elif ans in ["has","have","had"]:
            option_arr=["has","have","had","none"] 
            inst_arr=[inst,blank]
            
            que_word = ans
            ans = option_arr.index(ans) + 1
            return option_arr,inst_arr,"verb_aux",1,que_word
        elif ans in ["will","shall"]:#
            option_arr=["will","shall", "shall be", "will be"] #
            inst_arr=[inst,blank]
            
            que_word = ans
            ans = option_arr.index(ans) + 1
            return option_arr,inst_arr,ans,"verb_aux",1,que_word
        else:
            return -1

 #Irregular Verbs
# not handle 
def verb_main_ques(sent):
    token = clf(sent)
    arr =  []
    inst = "choose the correct"
    for i in range(len(token)):
        if token[i][1][:2] == "VB":
            arr.append(token[i][0])
    if len(arr)==0:
        return -1
    else:
        shuffle(arr)
        ans = arr[0]
        article = " " + ans + " "
        le = len(article)
        try:
            loc = sent.index( article )
        except ValueError:
            return -1 
        blank = sent[:loc] + "______" +sent[(loc+le):]
        option_1  = en.verb.present(arr[0])
        option_1  = en.verb.present(arr[0], person=3, negate=False)
        option_2  = en.verb.infinitive(arr[0])
        option_3  = en.verb.past(arr[0])
        option_4  = en.verb.past_participle(arr[0])
        option_arr = [option_1,option_2,option_3,option_4]
        inst_arr=[inst,blank]
        ans = article
        que_word = ans
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,ans,"verb_main",1,que_word
    
	
	

# article
# the definite article is not used: cars have accelerators, (plural common noun )
# with many proper names: John, France, London
# The indefinite article a (before a consonant sound) or an (before a vowel sound) is used only with singular, countable nouns
# Many nouns, especially singular forms of countable nouns which you will learn about later, must have an article. - article without noun
# generate question where there is no article
#Remember that A(AN) means "one" or "a single". You cannot use A(AN) with plural nouns.
def article_cor_ques(sent):
    token = clf(sent)
    arr=[]
    inst ="Choose the correct option"
    for i in range(len(token)):
        if token[i][1]=="DT" and token[i][0] in ["a","an","the"]:
            arr.append(token[i][0])
    if len(arr)==0:
        return -1
    else:
        shuffle(arr)
        ans  = arr[0] 
        article = " " + ans + " "
        le = len(article)
        try :
            loc = sent.index( article )
        except ValueError:
            return -1 
			
        blank = sent[:loc] + "______" +sent[(loc+le):]
        option_arr=["a","an","the","none"] # how to generate different options
        inst_arr=[inst,blank]
        
        que_word = ans
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,ans,"article_cor",1,que_word
# determiner
# demonstratives = this, that, 
# possessive determiners = my and their
# quantifiers = many, few and several
# numerals
# distributive determiners = each, any
# interrogative determiners =  which, what may be followed by ever
# article = a, an , the
#demonstrative and possessive determiners = demonstrative adjectives and possessive adjectives
# or as  (adjectival) demonstrative pronouns and (adjectival) possessive pronouns
# the possessives my, your etc. are used without articles
# confusion with an array

# preposition question:
def prep_cor_ques(sent):
    token = clf(sent)
    arr=[]
    inst ="Choose the correct option"
    for i in range(len(token)):
        if token[i][1]=="IN": # and in db, so to exclude subordinating conjuction
            arr.append(token[i][0])
    if len(arr)==0:
        return -1
    else:
        shuffle(arr)
        article = " " + arr[0] + " "
        le = len(article)
        try :
            loc = sent.index( article )
        except ValueError:
            return -1 
        blank = sent[:loc] + "______" +sent[(loc+le):]
        inst_arr=[inst,blank]
        ans = arr[0]
        if ans in ["in","on","at","for"]:
            option_arr = ["in","on","at","for"]
        elif ans in [ "under", "into","onto","inside"]:
            option_arr = [ "under", "into","onto","inside"]
        elif ans in ["while", "during", "near",  "behind"]:
            option_arr = ["while", "during", "near",  "behind"]
        elif ans in ["for","from","off","of"]:
            option_arr = ["for","from","off","of"]
        elif ans in ["amid","amidst","among","between"]:
            option_arr = ["amid","amidst","among","between"]
        elif ans in ["between","in","inside","within"]:
            option_arr = ["between","in","inside","within"]
        elif ans in ["without","minus","less","none"]:
            option_arr = ["without","minus","less","none"]
        elif ans in ["with","on","in","for"]:
            option_arr = ["with","on","in","for"]
        elif ans in ["via","through","thur","by"]:
            option_arr = ["via","through","thur","by"]
        elif ans in ["versus","against","vs","none"]:
            option_arr = ["versus","against","vs","none"]
        elif ans in ["upon","on","up","in"]:
            option_arr = ["upon","on","up","in"]
        elif ans in ["up","down","upward","upwards"]:
            option_arr = ["up","down","upward","upwards"]
        elif ans in ["below","underneath","beneath","neath"]:
            option_arr = ["below","underneath","beneath","neath"]
        elif ans in ["under","toward","for","towards"]:
            option_arr = ["under","toward","for","towards"]
        elif ans in ["as of","since","for","till"]:
            option_arr = ["as of","since","for","till"]
        elif ans in ["apart from","aside from","except","excluding"]:
            option_arr = ["apart from","aside from","except","excluding"]
        elif ans in ["excluding","with the exception of ","bar","save"]:
            option_arr = ["excluding","with the exception of ","bar","save"]
        elif ans in ["as of","since","for","till"]:
            option_arr = ["as of","since","for","till"]
        elif ans in ["until","till","plus","minus"]:
            option_arr = ["until","till","plus","minus"]
        elif ans in ["about","on""above","over"]:
            option_arr = ["about","on""above","over"]
        elif ans in ["after","following","behind","before"]:
            option_arr = ["after","following","behind","before"]
        elif ans in ["along","by","aside","lies"]:
            option_arr = ["along","by","aside","lies"]
        elif ans in ["with","by","from","of"]:
            option_arr = ["with","by","from","of"]
        elif ans in ["around","circa","round","across"]:
            option_arr = ["around","circa","round","across"]
        elif ans in ["on","during","upon","in"]:
            option_arr = ["on","during","upon","in"]
        elif ans in ["in","about","upon","with"]:
            option_arr = ["in","about","upon","with"]
        elif ans in ["near","by","through","along"]:
            option_arr = ["near","by","through","along"]
        elif ans in ["in","about","upon","with"]:
            option_arr = ["in","about","upon","with"]
        elif ans in ["regarding","about","apropos","as for"]:
            option_arr = ["regarding","about","apropos","as for"]
        elif ans in ["as regards","as to","concerning","in connection","with"]:
            option_arr = ["as regards","as to","concerning","in connection","with"]
        elif ans in ["re","respecting","with regard to"]:
            option_arr = ["re","respecting","with regard to"]
        else:
            return -1
        
            
            
            
        que_word = ans
        ans = option_arr.index(ans) + 1  
        return option_arr,inst_arr,ans,"article_cor","prep_cor",1,que_word

    
def modals_cor_ques(sent):
     
    token = clf(sent)
    arr=[]
    inst ="Choose the correct option modals"
    for i in range(len(token)):
        if token[i][1][0]=="M" :
            arr.append(token[i][0])
    
    if len(arr)==0:
        return -1
    else:
        shuffle(arr)
        
        article = " " + arr[0] + " "
        le = len(article)
        try:
            loc = sent.index( article )
        except ValueError:
            return -1 
        blank = sent[:loc] + "______" +sent[(loc+le):]
        pos_option_arr=["can","could","dare","may","might","need","ought to","shall","should","will","would","must"] # how to generate different options
        shuffle(pos_option_arr)
        option_arr = [arr[0]]
        
        i=-1
        while len(option_arr)<4:
            i=i+1
            if pos_option_arr[i] not in option_arr:
                option_arr.append(pos_option_arr[i])
            
                
        option_arr = option_arr[:4]
        inst_arr=[inst,blank]
        ans = arr[0]
        que_word = ans
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,ans,"modals_cor",1,que_word
# no count question
# only mcq with options

        
            
#subordinating conjuction
#correlative conjuction
def conj_cord_que(sent):
    token = clf(sent)
    arr =[]
    arr1=["for","and","nor","but","or","yet","so"]
    inst="choose the coorect"
    for i in range(len(token)):
        if token[i][1][:3] =="CC" and token[i][0] in arr1: # what are pre determiners
            arr.append(token[i][0])
    if len(arr)==0:
        return -1
    else:
        shuffle(arr)
        
        conjuction = " " + arr[0] + " "
        le = len(conjuction)
        try :
            loc = sent.index(conjuction )
        except ValueError:
            return -1 
        blank = sent[:loc] + "______" +sent[(loc+le):]
        option_arr=arr1[:3]+[arr[0]] # how to generate different options
        inst_arr=[inst,blank]
        ans = arr[0]
        que_word = ans
        ans = option_arr.index(ans) + 1
        return option_arr,inst_arr,ans,"conj_cord_que",1,que_word

# adjective question
# tut about use of "the" with superlative
# more,must
# no of adjective opinion,size,age,shape,colour,origin,material,type
# in, anti, dis,un , non
#mitigators 
def adjective(sent):
    token = clf(sent)
    arr =[]
    for i in range(len(token)):
        if token[i][1][:2]=="JJ":
            arr.append(token[i][0])
            break
    if len(arr) == 0:
        return -1
    else:
        if i>1 and token[i][1]=="JJS" and token[i-1][1]=="DT": # the largest
            option_arr = []
        elif i>2 and token[i][1]=="JJ" and token[i-2][1]=="DT" and token[i-1][1]=="RBS": # the most beautiful
            option_arr = []
        elif token[i][1]=="JJR": # larger
            option_arr = []
        elif i>1 and token[i][1]=="JJ" and token[i-1][1]=="RBR": # more beautiful
            option_arr = []
        elif token[i][1]=="JJ": # 3 form, voab,
            option_arr = []
        else:
            return -1
    shuffle(arr)
    shuffle(arr1)
    conjuction = " " + arr[0] + " "
    le = len(conjuction)
    try:
        loc = sent.index(conjuction )
    except ValueError:
        return -1 
    blank = sent[:loc] + "______" +sent[(loc+le):]
    option_arr=arr1[:3]+[arr[0]] # how to generate different options
    inst_arr=[inst,blank]
    ans = conjuction
    que_word = ans
    ans = option_arr.index(ans) +1 
    return option_arr,inst_arr,ans,"adjective",1,que_word

# punctuation
# comma
# 1 1. To separate the elements in a list of three or more items.
# "and" after comma with a word or multiple word.
# 2  Before certain conjunctions. - 1
# 3  To separate introductory elements in a sentence.
# 4 To separate parenthetical elements in a sentence.
# 5 To separate direct speech or quoted elements from the rest of the sentence.
# 6  Commas are used to separate elements in a sentence that express contrast.
# 7 Commas are used for typographical reasons to separate dates and years, towns and counties etc.
# 8 Commas are used to separate several adjectives.
# 9 Use a comma after a dependent clause that starts a sentence. - no
# days and month 
# feedback in case of commas
# none 
def comma_main_ques(sent):
    token = clf(sent)
    arr =[]
    inst = "choose the correct"
    for i in range(len(token)):
        if token[i][1]==",":
            arr.append(token[i][0])
            
            if token[i+1][0] in ["and", "but", "for", "or", "nor", "so", "yet"]: # 
                feedback = "Use a comma before " + '"' + token[i+1][0] + '"' + ",as it is a coordinating conjunction that links two independent clauses."
            elif token[i+2][0] == "and": # Use commas to separate words and word groups in a simple series of three or more items.
                feedback = "Use commas to separate words and word groups in a simple series of three or more items."
            elif token[i+1][0] == "''" : # Use a comma when attributing quotes.
                feedback = "Use a comma when attributing quotes."
            elif (i-1 == 0 or i-1 == 1) and token[i-1][1][:2] =="RB" : # Use a comma after introductory adverbs
                feedback = "Use a comma after introductory adverbs"
            elif token[i-1][1][:2] =="JJ"  and token[i+1][1][:2] =="JJ" : # Use a comma between two adjectives that modify the same noun and the order of the adjectives is interchangeable..
                feedback = "Use a comma between two adjectives that modify the same noun and the order of the adjectives is interchangeable.."
            elif token[i+1][0] =="not"  : # Use a comma to offset negation in a sentence.
                feedback = "Use a comma to offset negation in a sentence."
            elif token[i+1][1] =="CD" and token[i-1][1] =="CD"  : # also use a comma to separate the elements in a full date (weekday, month and day, and year). Also separate a combination of those elements from the rest of the sentence with commas.
                feedback = "lso use a comma to separate the elements in a full date (weekday, month and day, and year). Also separate a combination of those elements from the rest of the sentence with commas."
            elif token[i-1][0] =="Yes"  or token[i-1][0] =="NO" : # Use a comma when the first word of the sentence is "yes" or "no."
                feedback = "Use a comma when the first word of the sentence is 'yes' or 'no.'"
            elif token[i+1][0] in ["namely", "i.e.", "e.g."] or (token[i+1][0]=="that" and token[i+2][0]=="is") : # Use a comma before and after certain introductory words or terms, such as namely, that is, i.e., e.g., and for instance, when they are followed by a series of items.
                feedback = "Use a comma before and after certain introductory words or terms, such as namely, that is, i.e., e.g., and for instance, when they are followed by a series of items."
            else:
                feedback = " use noun tutorial"
            break 

            
                
    if len(arr) == 0:
        return -1
    
    conjuction = ","
    le = len(conjuction)
    try :
        loc = sent.index(conjuction )
    except ValueError:
        return -1 
    blank = sent[:loc] + "______" +sent[(loc+le):]
    option_arr=[",",";","?","None"] # how to generate different options
    inst_arr=[inst,blank]
    ans = conjuction
    que_word = ans
    ans = option_arr.index(ans) +1
    
    
    return option_arr,inst_arr,ans,"comma_main",1,que_word

# The apostrophe   
#"It's vs. "Its"
# THE APOSTROPHE IN CONTRACTIONS
# plural's apos
def apost_poss_ques(sent):
    token = clf(sent)
    arr =[]
    inst = "choose the correct"
    for i in range(len(token)):
        if token[i][1]=="POS":
            arr.append(token[i][0])
            search = token[i][0]
            if token[i-1][0][-1] != "s" and token[i][0]=="'s" : # In most cases you simply need to add 's to a noun to show possession
                conjuction = token[i-1][0]+token[i][0]
                feedback = "Simply add 's to a noun to show possession"
                option_arr = [token[i-1][0],token[i-1][0]+token[i][0],token[i-1][0]+"s", token[i-1][0]+" is"]
                #print option_arr
            elif token[i-1][0][-1] == "s" and token[i][0]=="s": # Ordinary (or common) nouns that end in s, both singular and plural, show possession simply by adding an apostrophe after the s.
                feedback = "Ordinary (or common) nouns that end in s, both singular and plural, show possession simply by adding an apostrophe after the s."
                option_arr = [token[i-1][0],token[i-1][0]+token[i][0],token[i-1][0]+"s", token[i-1][0]+"s's"]
                conjuction = token[i-1][0]+token[i][0]
            elif token[i-1][0][-1] == "s" and token[i][0]=="'s": #  Proper nouns (names of people, cities, countries) that end in s can form the possessive either by adding the apostrophe + s 
                feedback = "Proper nouns (names of people, cities, countries) that end in s can form the possessive either by adding the apostrophe + s "
                option_arr = [token[i-1][0],token[i-1][0]+token[i][0],token[i-1][0]+"s", token[i-1][0]+"es"]
                conjuction = token[i-1][0]+token[i][0]
            else:
                feedback ="look at tutorial"
            break
    if len(arr) == 0:
        return -1
    le = len(conjuction)
    try :
        loc = sent.index(conjuction )
    except ValueError:
        return -1 
    blank = sent[:loc] + "______" +sent[(loc+le):]
    inst_arr=[inst,blank]
    ans = conjuction
    ans = option_arr.index(ans) +1
    
    
    return option_arr,inst_arr,ans,feedback

                
        
            
#Inflection
    
# preposition  - 
# modals -
# Multi-word verb
# verb,  - tenses, subject verb agreement
# 
# adverb, adjective   
# 2 type of conjuction  
#word structuring
# phrasal verb



# semicolon
# 1 In complicated lists.
# In the meeting today we have Professor Wilson, University of Barnsley;
#Dr Watson, University of Barrow in Furness;
#Colonel Custard, Metropolitan Police and Dr Mable Syrup, Genius General, University of Otago, New Zealand.
# 2 Separating closely-related independent clauses.
# Terry always slept with the light on; he was afraid of the dark.
# Terry always slept with the light on. He was afraid of the dark



# ambiguity by often and only
# Students who go to the pub often can get worse grades.

# The students who went to the pub only found warm beer.

# Consistency of Tense.
# Subject/Verb Agreement.
# infinitive - to go, to eat 
# split infinitive - to boldly go
# Collocation
# verb type - Ergative verb
# verb type - transitive or intransitive,

# list of idioms

# Double negative

# English compound

# English conditional sentences - 0,1,2,3,4 conditionals

# Gender in English - Gender-neutral language

# Subject auxiliary inversion  question, negative

# Preposition and postposition

# English subjunctive

# English modals of deduction

# English markers of habitual aspect

# idiom list

# The study covered both grammar checking (usage, contextual spelling, punctuation, sentence structures)
# and style checking (wordiness, redundancy, cliches, platitudes, jargon, informality, overworked and trite expressions,
#	affected language, pompous phrases, empty intensifiers, awkward usage, slang, nonstandard and nonidiomatic diction,
#	rash overstatements, tautologies, vague terms, outmoded diction, and potentially offensive language).



# sentence type 
# first break sentence into clauses
# study clause - its grammar, subject, object(noun, noun phrases), predicate verb

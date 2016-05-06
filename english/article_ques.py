import final_quest
import nltk.data
from random import randint
import codecs
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def question_generation():
        count = 100
        art=[]
        article=open("eco.txt","r")
        
        
          
        
        #a = question_generation('')
        
        for i in article:

                print i
                
                if i!= '\r\n':
                        if i[-2:] =="\r\n":
                                ikm=i[:-2]
                                sent_token = tokenizer.tokenize(ikm)
                                art.append(sent_token)
                        else:
                                sent_token = tokenizer.tokenize(i)
                                art.append(sent_token)

                                
                
        
        ar=[]   
        loc=[]
        print len(art)
        for i in range(13):
                # first choose para, then sent
                n=0
                try:
                        a_par = randint(0,len(art)-1)
                except ValueError:
                        print " a_par error randint"
                try:
                        b_par = randint(0,len(art)-1)
                except ValueError:
                        print " b_par error randint"
                # print art
                while a_par==b_par:
                        b_par = randint(0,len(art)-1)
                        # 2 diff para already has been selected
                
                try:
                        a_sent = randint(0,len(art[a_par])-1)
                except ValueError:
                        a_sent=0
                try:
                        b_sent = randint(0,len(art[b_par])-1)
                except ValueError:
                        b_sent=0
                
                
                if i==0:
                        qt_a = final_quest.noun_count_ques(art[a_par][a_sent])
                        qt_b = final_quest.noun_count_ques(art[b_par][b_sent])
                        
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                elif i==1:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.noun_ident_ques(art[a_par][a_sent])
                        qt_b = final_quest.noun_ident_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                elif i==299:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.sub_noun_ques(art[a_par][a_sent])
                        qt_b = final_quest.sub_noun_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                elif i==3:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.pronoun_cor_ques(art[a_par][a_sent])
                        qt_b = final_quest.pronoun_cor_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                                
                elif i==4:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.pronoun_wh_ques(art[a_par][a_sent])
                        qt_b = final_quest.pronoun_wh_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                        
                elif i==5:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.verb_aux_ques(art[a_par][a_sent])
                        qt_b = final_quest.verb_aux_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                elif i==61: # recheck
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.verb_main_ques(art[a_par][a_sent])
                        qt_b = final_quest.verb_main_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                elif i==7:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.modals_cor_ques(art[a_par][a_sent])
                        qt_b = final_quest.modals_cor_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]

                    
                    
                elif i==8:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.conj_cord_que(art[a_par][a_sent])
                        qt_b = final_quest.conj_cord_que(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                elif i==9:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.comma_main_ques(art[a_par][a_sent])
                        qt_b = final_quest.comma_main_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]

                elif i==10:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.apost_poss_ques(art[a_par][a_sent])
                        qt_b = final_quest.apost_poss_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]

                elif i==11:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.article_cor_ques(art[a_par][a_sent])
                        qt_b = final_quest.article_cor_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]
                elif i==12:
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.prep_cor_ques(art[a_par][a_sent])
                        qt_b = final_quest.prep_cor_ques(art[b_par][b_sent])
                        if qt_a!=-1:
                                loc.append([a_par,a_sent])
                                ar.append(qt_a)
                                print qt_a
                                print [a_par,a_sent]
                        if qt_b!=-1:
                                loc.append([b_par,b_sent])
                                ar.append(qt_b)
                                print qt_b
                                print [b_par,b_sent]

                elif i==17:# adjective
                        qt_a_k = final_quest.clf(art[a_par][a_sent])
                        qt_a = final_quest.adjective(art[a_par][a_sent])
                        qt_b = final_quest.adjective(art[b_par][b_sent])
                        if qt_a!=-1:
                                ar.append(qt_a)
                                print qt_a
                                print art[a_par][a_sent]
                        if qt_b!=-1:
                                ar.append(qt_b)
                                print qt_b
                                print art[b_par][b_sent]

                
        return ar,loc
                            
      
                            
        

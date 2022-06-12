
from GoogleNews import GoogleNews
#from newspaper3k import Article
from newspaper import Article
import pandas as pd
import pprint
import requests
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('punkt')
#nltk.download('stopwords')
#print('hi')
def stopwords_remove(para):
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(para)
  filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  filtered_sentence=[i for i in filtered_sentence if len(i)>=2]
  return filtered_sentence
def select_regect(para,word):
     for i in para:
        if str(i.lower())==str(word.lower()):
           return True
           break
     return False 
#filtering the key_word       
def paragraph(para,key_word):
    filter_para=stopwords_remove(para)
    sent=select_regect(filter_para,str(key_word))
    if sent == True:
       return para
    else:
         return "no keyword found"
def solution(df,key_word):
    a=[]
    for i in range(len(df)):
      f_para=df["desc"][i]
      b=paragraph(f_para,key_word)
      if b!= "no keyword found":
          a.append(i)
    return a
def company_details(c_name,key_word,date1,date2):
            try:
                googlenews=GoogleNews(start=date1 ,end=date2)
                googlenews.search(c_name)
                results=googlenews.result(sort = True)
                df=pd.DataFrame(results)
                #print(df.columns)
                b=solution(df,key_word)
                #df_filtered=pd.DataFrame(b)
                #df_filtered=df_filtered.T
            
                d=""
                for i in b:
                    website = results[i]["link"]
                    article = Article(website)
                    article.download()
                    article.parse()
                    article.nlp()
                    a=article.text
                    d=d+a
                #print(a)
                return(d)
            except:
                return 'no news found or please check start date and end date.'
def reverse_date(date):
   date=str(date)
   date=date.split("-")
   s=""
   s=date[1]+"/"+date[2]+"/"+date[0]
   return s

#df = company_details ('ABB','price')
#print(df)

#date  = reverse_date('2022-06-13')
#print(date)


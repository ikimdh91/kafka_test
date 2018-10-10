
from kafka import KafkaProducer


import requests
import json
import time
import datetime

def executeSomething():
    #code here
    time.sleep(5)



if __name__ == '__main__':

    # sNLP = StanfordNLP()

    url = "http://sclab.gachon.ac.kr:19002/query/service"
    producer = KafkaProducer(acks=0, compression_type='gzip',
                             bootstrap_servers='daeho.local:9092, daeho.local:9093, daeho.local:9094')
    total = 0
    flag=-1
    total2=0

    while True:
        # executeSomething()

        # print('\n',datetime.datetime.now(),'\n')

        ts = int(round(time.time() * 1000)) - 500000
        q = 'use feeds; select * from DiseaseTweets Limit 10;'
        # q += ' where lang="en" and to_bigint(timestamp_ms) >=' + str(ts - 5000) \
        #      + ' and to_bigint(timestamp_ms) < ' + str(ts) + ';'

        r = requests.post(url, data={
            'statement': q
        })
        json_data = r.json()
        data = json_data['results']

        for d in data :
            print('\nSTART ', datetime.datetime.now(), '\n')
            total=total+1
            total2 = total2 + 1
            value=[]
            # print(d)
            # print(d['DiseaseTweets']['geo']['coordinates'])
            print(d['DiseaseTweets']['user']['screen_name'])
            # print(d['DiseaseTweets']['location'])
            print(d['DiseaseTweets']['created_at'])


            # if 'geo' in d['DiseaseTweets'] :
            #     bytesstr = '1'.encode('utf-8')\
            #                + str(d['DiseaseTweets']['text']).encode('utf-8') + '/'.encode('utf-8') \
            #                + str(d['DiseaseTweets']['created_at']).encode('utf-8') + '/'.encode('utf-8')\
            #                + str(d['DiseaseTweets']['user']['screen_name']).encode('utf-8') + '/'.encode('utf-8')\
            #                + str(d['DiseaseTweets']['geo']['coordinates']).encode('utf-8') + '/'.encode('utf-8') \
            # else :
            #     bytesstr = '0'.encode('utf-8') \
            #                + str(d['DiseaseTweets']['text']).encode('utf-8') + '/'.encode('utf-8') \
            #                + str(d['DiseaseTweets']['created_at']).encode('utf-8') + '/'.encode('utf-8') \
            #                + str(d['DiseaseTweets']['user']['screen_name']).encode('utf-8') + '/'.encode('utf-8')

            bytesstr = '0'.encode('utf-8') \
                       + str(d['DiseaseTweets']['text']).encode('utf-8') + '/'.encode('utf-8') \
                       + str(d['DiseaseTweets']['created_at']).encode('utf-8') + '/'.encode('utf-8') \
                       + str(d['DiseaseTweets']['user']['screen_name']).encode('utf-8') + '/'.encode('utf-8')

            # print("total : ",total,d['DiseaseTweets']['text'], "\n----------------")
            print("Disease Tweet : ", total, "      Total Tweet : ", total2)

            producer.send('3Broker', bytesstr)
            producer.flush()
            print('\nEND ', datetime.datetime.now(), '\n')



# for d in data:
#     for disease in diseases:
#         words = sNLP.word_tokenize(d['Tweets']['text'])
#         lower_words = []
#         for word in words :
#             lower_words.append(word.lower())
#         if disease in lower_words :
#             cnt = cnt+1
#             print("\nDISEASES DETECTED = ",cnt,"   DISEASE = ",disease, "\n",d['Tweets']['text'])


# print(d['Tweets']['text'])



# text = 'The number of 25-34 year olds who died annually from alcohol-related liver disease nearly tripled between 1999 and 2016.'
# print ("Annotate:", sNLP.annotate(text))
# print ("POS:", sNLP.pos(text))
# print ("Tokens:", sNLP.word_tokenize(text))
# print ("NER:", sNLP.ner(text))
# print ("Parse:", sNLP.parse(text))
# print ("Dep Parse:", sNLP.dependency_parse(text))



# for i in range(1, 11):
#     producer.send('diseases', key='1', value='%d - Apache Kafka is a distributed streaming platform - key=1' % i)
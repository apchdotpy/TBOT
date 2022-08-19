#https://docs.tweepy.org/en/stable/api.html
# import modules
import tweepy
from KEYS import *

class TBOT():
    def __init__(self):
        # private variables
        self.__consumer_key=apikey
        self.__consumer_secret=apikeysecret
        self.__access_token=accesstoken
        self.__access_token_secret=accesstokensecret
        # public variable
        self.api=''
    
    def login(self):
        # create auth
        auth = tweepy.OAuth1UserHandler(self.__consumer_key,
                                        self.__consumer_secret,
                                        self.__access_token,
                                        self.__access_token_secret)
        #create API
        try:
            self.api = tweepy.API(auth)
            print('CONNECTED')
            return True
        except Exception as error:
            print(error)

    def search30d(self,botname='',quest='',log=True,fname='tweets'):
        if log:
            for tweets in self.api.search_30_day(label=botname,query=quest):
                with open(str(fname)+'..txt','a', encoding='utf-8') as T:
                    T.write(str(tweets.text)+'\n')
        else:
            print('Login has failed')

    def searchfull(self,botname='',quest='',log=True,fname='tweets'):
        if log:
            for items in self.api.search_full_archive(label='irpybot',query='پایتون'):
                with open(str(fname)+'.txt','a', encoding='utf-8') as T:
                    T.write(str(items.text)+'\n')        
            print(items.user.screen_name)
        else:
            print('Login has failed')

    def homeline(self,count=0,delrep=True,log=True,fname='tweets'):
        if log:
            for items in self.api.home_timeline(count=count,exclude_repies=delrep):
                with open(str(fname)+'..txt','a', encoding='utf-8') as T:
                    T.write(str(items.text)+'\n')            
        else:
            print('Login has failed')

    def mentionline(self,count=0,log=True,fname='tweets'):
        if log:
            for items in self.api.mentions_timeline(count=count):
                with open(str(fname)+'.txt','a', encoding='utf-8') as T:
                    T.write(str(items.text)+'\n')            
        else:
            print('Login has failed')

    def userline(self,username='',count='',delrep=True,rt=False,log=True,fname='tweets'):
        if log:
            for items in self.api.user_timeline(screen_name=username,count=count,
                                                exclude_replies=delrep,include_rts=rt):
                with open(str(fname)+'.txt','a', encoding='utf-8') as T:
                    T.write(str(items.text)+'\n')            
        else:
            print('Login has failed')

    def getfav(self,username='',count=0,log=True,fname='tweets_like'):
        if log: 
            for items in self.api.get_favorites(screen_name=username,count=count):
                with open(str(fname)+'.txt','a', encoding='utf-8') as T:
                    T.write(str(items.text)+'\n')  

def main():
    tbot=TBOT()
    t=tbot.login()
    #tbot.search30d('irpybot','لینوکس',t,'linux')
    #tbot.searchfull('irpybot','پایتون',t,'python')
    #tbot.homeline(count=10,rep=t,log=t,fname='Home')
    #tbot.homeline(10,t,t,'home')
    #tbot.mentionline(10,t,'mention')
    #tbot.userline('apchdotpy',count=10,delrep=True,rt=False,log=t,fname='userline')
    tbot.getfav(username='AudioMasterApp',count=10,log=t)
if __name__=='__main__':
    main()
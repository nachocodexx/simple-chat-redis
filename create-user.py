import time
import redis
import uuid
import sys,argparse
r= redis.Redis(host="localhost",port=6379,db=0)


class User(object):
    def __init__(self,username:str):
        self.username=username
        self.created_at = int(time.time())
        self.userId= str(uuid.uuid4())

if __name__ == '__main__':
    isRunning=True
    parser = argparse.ArgumentParser(description='Create a user, simple chat application by Ignacio Castillo')
    parser.add_argument("-u","--username",help="Username")
    args = parser.parse_args()
    user = User(args.username)
    r.hset("user:"+user.userId,mapping=user.__dict__)
    print("USER ID: "+user.userId)

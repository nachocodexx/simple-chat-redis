import time
import redis
import uuid
import sys,argparse
r= redis.Redis(host="localhost",port=6379,db=0)


class Message(object):
    def __init__(self,message:str,userId:str):
        self.message=message
        self.sent_at = int(time.time())
        self.userId= userId

def checkIfExists(chatRoom:str,userId:str):
    chatRoomExists = int(r.exists("chatroom:"+chatRoom)) ==1
    userExists = int(r.exists("user:"+userId)) ==1 
    if not (chatRoomExists):
        print("Chat room: {} does not exist".format(chatRoom))
        sys.exit(1)
    if not (userExists):
        print("User: {} does not exist".format(userId))
        sys.exit(1)


if __name__ == '__main__':
    isRunning=True
    parser = argparse.ArgumentParser(description='Send message simple chat application by Ignacio Castillo')
    
    parser.add_argument("-u","--user",help="User UUID")
    parser.add_argument('-cr','--chat-room',help="Chat room id")

    args = parser.parse_args()
    charRoomId = args.chat_room
    userId =args.user
    checkIfExists(charRoomId,userId)
    username = r.hget(userId,"username")

    while(isRunning):
        messageText=input("Message: ")
        r.execute_command("XADD","chatroom:{}:stream".format(charRoomId),"*","message",messageText,"sent_at",int(time.time()),"user_id",userId)
        print("Your message was successfully sent to [{}]".format(charRoomId))



import sys
import time
import redis
import argparse
r= redis.Redis(host="localhost",port=6379,db=0)
class ChatServer(object):
    def __init__(self,chatRoomId:str):
        self.chatRoomId=chatRoomId
        
    def start(self):
        exists = int(r.exists("chatroom:"+self.chatRoomId))==1
        if not(exists):
            print("Chat room: {} does not exist".format(self.chatRoomId))
            sys.exit(1)

        while(True):
            response = r.execute_command("XREAD","BLOCK","0","STREAMS","chatroom:"+self.chatRoomId+":stream","$")
            print(response)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chat server, simple chat application by Ignacio Castillo")
    parser.add_argument("-cr","--chat-room",help="Chat room id")
    args = parser.parse_args()
    chatServer=ChatServer(args.chat_room)
    chatServer.start()

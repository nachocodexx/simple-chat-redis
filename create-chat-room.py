import time
import redis
import uuid
import sys,argparse
r= redis.Redis(host="localhost",port=6379,db=0)


class ChatRoom(object):
    def __init__(self):
        self.created_at = int(time.time())
        self.chatRoomId= str(uuid.uuid4())

def addUsersToChatRoom(chatRoomId:str,usersIds):
    r.sadd("chatroom:"+chatRoomId+":users",*usersIds)
    return True
def checkIfUsersExists(usersIds):
    for userId in usersIds:
        userExists = int(r.exists("user:"+userId)) == 1
        if not (userExists):
            print(userId+" does not exist")
            sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a chat room, simple chat application by Ignacio Castillo')
    parser.add_argument("-u","--users",action='append',help="List of user id's",required=True)
    parser.add_argument("-cr","--chat-room",help="Chat room id",required=False)
    args = parser.parse_args()
    chatRoomId = args.chat_room
    usersIds = args.users
    if(chatRoomId):
        checkIfUsersExists(usersIds)
        addUsersToChatRoom(chatRoomId,usersIds)
        print("CHAT ROOM: ".format(chatRoomId))
        sys.exit(0)
    else:
        chatRoom  = ChatRoom()
        checkIfUsersExists(usersIds)
        addUsersToChatRoom(chatRoom.chatRoomId,usersIds)
        r.hset("chatroom:"+chatRoom.chatRoomId,mapping=chatRoom.__dict__)
        print("CHAT ROOM: {}".format(chatRoom.chatRoomId))



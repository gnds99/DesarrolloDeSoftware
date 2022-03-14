import time
class ChatRoom:
    @staticmethod
    def showMessage(user, message):
        print(time.strftime("%I:%M:%S") + " [" + user.getName() + "] : " + message)

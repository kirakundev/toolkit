# oke this program by python language
import os,sys,time
#+++++++++++++++++// Tool
def tool():
    os.system('clear')
    print """
            [#] Welcome the toolkit [#]
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
      bash app/installer/termux-de/main.sh 
    elif tool == 2:
      bash app/installer/proot-de/main.sh 
    elif tool == 3:
       bash app/pentest/main.py 
    elif tool == 4:
       bash app/main.sh 
    elif tool == 0:
       os.system('python2 main.py')
#=++++++++///Batas suci
      
def update():
    os.system('git pull')
    print "[*]Successfull updateing ..."
    time.sleep (2)
    os.system('python2 main.py')
def main():
    os.system('clear')
    print """
         
            [#] Warceu Project Toolkit [#]
        ______________________________________

        Menu:
             (1).Inatall require packagess
             (2).Start toolkit
             (3).Update
             (5).About
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

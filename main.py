
"""
 Oke this program by python version 2.7 language
 this program toolkit created by Ers ID 
 This project is copyrighted under MIT license 
 This project is open source
 please read the license ! 
 not for sale
 please don't recode my project  
 recode will not make you mastah or master 
"""
import os,sys,time,random
class cl:
    red="\033[1;31m"
    grn="\033[1;32m"
    ylw="\033[1;33m"
    blu="\033[1;34m"
    pop="\033[1;35m"
    cyn="\033[1;36m"
    end="\033[0m"
    mir="\033[3;37m"
#++++++++++++++//Batas suci
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan lumpat :v
        time.sleep(random.random() * 0.1)
#+++++++++++++//batas suci
def update():
    os.system('clear')
    print cl.end + "[" + cl.grn + "*" + cl.end + "]" + cl.cyn + "Updating..."
    os.system('git pull')
    print cl.grn + "Successfull update"
    time.sleep(2)
    os.system('python2 main.py')
#+++++++++++++//batas suci
def about():
    os.system('bash asst/about.sh')
#++++++++++++//batas suci
def main():
    os.system('clear')
    print ""
    print cl.end + "           [" + cl.grn + "#" + cl.end + "]" + cl.cyn + "Warceu Project Center" + cl.end + "[" + cl.grn + "#" + cl.end + "]" 
    print cl.mir + "                Created By Ers ID" + cl.end  
    print cl.cyn + "  Version: " + cl.grn + "0.1.1"
    print ""
    print cl.end + " [" + cl.grn + "MENU" + cl.end + "]:"
    print ""
    print cl.end + "     (1)." + cl.cyn + "Install" + cl.end + "(recommend)"
    print cl.end + "     (2)." + cl.cyn + "Start"
    print cl.end + "     (3)." + cl.cyn + "Update"
    print cl.end + "     (4)." + cl.cyn + "About"
    print cl.end + "     (0)." + cl.red + "Exit" + cl.end  
    print ""
main()
pil = input (cl.end + "[" + cl.grn + "#" + cl.end +  "]" + cl.cyn + "Chosse: " + cl.grn )
if pil == 1:
    os.system('bash packagess/install.sh')
elif pil == 2:
    #+++++++++++++//batas suci
    def start():
        os.system('clear')
        print ""
        print cl.end + "           [" + cl.grn + "#" + cl.end + "]" + cl.cyn + "Warceu Project Toolkt" + cl.end + "[" + cl.grn + "#" + cl.end + "]" 
        print cl.mir + "                Created By Ers ID" + cl.end  
        print ""
        print cl.end + " [" + cl.grn + "MENU TOOLKIT" + cl.end + "]:" 
        print ""
        print cl.end + "     (1)." + cl.cyn + "Termux DE"
        print cl.end + "     (0)." + cl.red + "Back to Home"
    start()
    st = input (cl.end + "[" + cl.grn + "#" + cl.end + "]" + cl.cyn + "Chosse: " + cl.grn)
    if st == 1:
        def TD():
            os.system('clear')
            print ""
            print cl.end + "          [" + cl.grn + "#" + cl.end + "]" + cl.cyn + "Welcome To Termux Desktop" + cl.end + "[" + cl.grn + "#" + cl.end + "]" 
            print ""
            print cl.end + " [" + cl.grn + "MENU TERMUX-DE" + cl.end + "]:"
            print ""
            print cl.end + "    (1)." + cl.cyn + "Termux-DE by Ers ID" + cl.end + "(Sedang dalam perbaikan.)"
            print cl.end + "    (2)." + cl.cyn + "Termux-DE by Adi1090x"
            print cl.end + "    (3)." + cl.cyn + "Termux-DE by Yizus7u7"
            print cl.end + "    (0)." + cl.red + "Back to home"
            print ""
        TD()
        td = input (cl.end + "[" + cl.grn + "#" + cl.end + "]" + cl.cyn + "Chosse: " + cl.grn)
        if td == 1:
            os.system('clear')
            mengetik"Mohon maaf peoject termux deskto ini sedang dalam"
            mengetik"perbaikan,mohon tunggu update an selanjutnya"
            raw_input("Enter to back home")
            os.system('python2 main.py')
        elif td == 2:
            os.system('clear')
            print "Please wait..."
            time.sleep(2)
            os.system('bash app/installer/termux-de/td1.sh')
        elif td == 3:
            os.system('clear')
            print "Please wait..."
            time.sleep(2)
            os.system('bash app/installer/termux-de/td2.sh')
        elif td == 0:
            os.system('python2 main.py')
        else:
            print cl.red + "Wrong input !"
            time.sleep(3)
            os.system('python2 main.py')
        #+++++++//batas suci
    elif st == 0:
        os.system('python2 main.py')
    else:
        print cl.red + "Wrong input !" 
        time.sleep(3)
        os.system('python2 main.py')
    #+++++//bats suci
elif pil == 3:
    update()
elif pil == 4:
    about()
elif pil == 0:
    print cl.ylw + "Exit program"
    time.sleep(3)
    sys.exit()
else:
    print cl.red + " Wrong input ! " + cl.end  
    time.sleep(3)
    os.system("python2 main.py")
#++++//DONE
# copyright@2022 

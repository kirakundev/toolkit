clear
echo "[*]Installing basic packages..."
apt update -y 
apt upgrade -y
apt install root-repo -y
apt install x11-repo -y
sleep 1
echo "[*]Installing more packagess..."
apt install -y python2 python php ruby curl wget 
echo "[*]Installing module python v.3..."
pip install requests 
pip install mechanize 
pip install bs4
pip install colorama
echo "[*]Installing module python v.2.7..."
pip2 install requests 
pip2 install mechanize 
pip2 install bs4
pip2 install colorama
echo "[♧]Installing Done..."
sleep 2
echo "[+]Setup the toolkit..."
cd ..
python2 main.py 

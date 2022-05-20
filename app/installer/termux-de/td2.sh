read -p "Enter to continue"
cd $HOME
wget https://raw.githubusercontent.com/Yisus7u7/termux-desktop-xfce/main/boostrap.sh --no-check-certificate
chmod 777 boostrap.sh
bash boostrap.sh

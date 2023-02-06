#! /bin/bash

white="\033[1;37m"
green="\033[1;32m"
blue="\033[1;34m"


#directory verification
directory=$(pwd)


if which figlet >/dev/null; then
sleep 1
echo ""
echo -e "$blue(figlet) ................................................... Instalado [✓]"
else
sleep 1
echo -e "(figlet) No instalado [✗]"
sleep 1
echo -e "\e[1;32mInstalando figlet ...\e[0m"
sleep 3
pkg install figlet
fi

#directory verification
directory=$(pwd)


if which python >/dev/null; then
sleep 1
echo ""
echo -e "$blue(python) ................................................... Instalado [✓]"
else
sleep 1
echo -e "(figlet) No instalado [✗]"
sleep 1
echo -e "\e[1;32mInstalando python ...\e[0m"
sleep 3
pkg install python -y
fi

setterm -foreground blue
figlet Script-B

echo ""
echo "***"
echo -e "\e[1;33mGenerateBIN\e[0m \e[1;32m= Esta Script de bin sirve para comprar Youtube Premiun\e[0m"
echo -e "\e[1;33mDragon-X\e[0m \e[1;32m= Esta Script generara bins para usar en diferentes streaming\e[0m"
echo -e "\e[1;33mNansonG\e[0m \e[1;32m= Esta Script funciona igual que la pagina namsonGen\e[0m"
echo ""
while :
do
setterm -foreground white
echo "#SELECCIONE UNA HERRAMIENTA DE BIN"
echo ""
echo -e "\e[1;37m[\e[0m\e[1;31m1\e[0m\e[1;37m]\e[0m\e[1;32mGenerateBIN\e[0m"
echo -e "\e[1;37m[\e[0m\e[1;31m2\e[0m\e[1;37m]\e[0m\e[1;32mDragon-X\e[0m"
echo -e "\e[1;37m[\e[0m\e[1;31m3\e[0m\e[1;37m]\e[0m\e[1;32mNansonG\e[0m"
echo -e -n "\e[1;31m[+]Opcion >> \e[0m"
read opcion
case $opcion in
1)
#! /bin/bash
python bin.py
exit
;;
2)
#! /bin/bash
python dragon.py
exit
;;
3)
#! /bin/bash
python namsonG.py
exit
;;
esac 
done

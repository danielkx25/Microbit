# Add your Python code here. E.g.
from microbit import *
l1=00000
l2=00000
l3=00000
l4=00000
l5=00000
imagem=str(l1)+":"+str(l2)+":"+str(l3)+":"+str(l4)+":"+str(l5)
#gerador de imagem com  leds programáveis

pos=0
i=0

while True:
    display.show(Image(str(imagem)))
    
    l3="";
    
    if button_a.is_pressed() and int(pos) >0:
        pos = int(pos) - 1
    
    if button_b.is_pressed() and int(pos) <4:
        pos = int(pos) + 1
    
    for i in range(5):
        if(int(pos) != int(i)):
            l3 = str(l3) + "0"
        else:
            l3 = str(l3) + "5"

    imagem=str(l1)+":"+str(l2)+":"+str(l3)+":"+str(l4)+":"+str(l5)
    sleep(100)

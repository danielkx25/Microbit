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
l=0
c=0
disparo=0;
lista_l1 = [5,5,5,5,5]
lista_l2 = [5,5,5,5,5]
interrompido=0

while True:
    display.show(Image(str(imagem)))
    l1="";
    l2="";
    l3="";
    l4="";
    l5="";
    
    if button_a.is_pressed() and button_b.is_pressed() and disparo == 0:
        disparo = 1 
    else:
        if disparo == 0:
            if button_a.is_pressed() and int(pos) >0:
                pos = int(pos) - 1
            else:
                if button_b.is_pressed() and int(pos) <4:
                    pos = int(pos) + 1
    
    for l in range(5):
        for c in range(5):
            if(int(l)==1):
                if(int(c) == int(pos) and int(disparo) == 4 and 
                int(lista_l2[c])==0):
                    l1 = str(l1) + "0"
                    lista_l1[c] = 0
                    interrompido = 1
                else:
                    l1 = str(l1) + str(lista_l1[c])
            if(int(l)==2):
                if(int(c) == int(pos) and int(disparo) == 3 and lista_l2[c] != 0):
                    l2 = str(l2) + "0"
                    lista_l2[c] = 0
                    interrompido = 1
                else:
                    if(int(c) == int(pos) and int(disparo) == 3 and lista_l2[c] == 0):
                        l2 = str(l2) + "5"
                    else:    
                        l2 = str(l2) + str(lista_l2[c])
                
            if(int(l)==3):
                if(int(c) == int(pos) and int(disparo) == 2):
                    l3 = str(l3) + "5"
                else:
                    l3 = str(l3) + "0"
            if(int(l)==4):
                if(int(c) == int(pos) and int(disparo) == 1):
                    l4 = str(l4) + "5"
                else:
                    l4 = str(l4) + "0"
    
    if(disparo>0 and disparo<5 and interrompido==0):
        disparo = int(disparo)+1
    else:
        disparo = 0
        interrompido = 0
    
    for i in range(5):
        if(int(pos) != int(i)):
            l5 = str(l5) + "0"
        else:
            l5 = str(l5) + "5"
        
    imagem=str(l1)+":"+str(l2)+":"+str(l3)+":"+str(l4)+":"+str(l5)
    sleep(50)

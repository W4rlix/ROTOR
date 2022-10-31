from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import socket     
 
Builder.load_file('LoadScreen.kv')
class MyLayout(Widget):
    def skret_lewo(self):
        wartosc = int(self.ids.KAT.text)
        if(wartosc > 0):
            
            wartosc = wartosc-1
            self.ids.KAT.text = str(wartosc)
        
        elif(self.ids.KAT.text == '0'):
            #zmiana kata na 359
            wartosc = 359
            self.ids.KAT.text = str(wartosc)

        self.ids.img.stopnie = str(int(self.ids.img.stopnie) + 1)

        #polaczenie z serwerem za pomoca socket
        s = socket.socket()                 
        s.connect(('127.0.0.1', 12345))
            
        #wyslana komenda Lewo
        data = "Lewo";
        s.send(data.encode())
            
        #odpowiedz od serwera wypisana w terminalu klienta
        dataFromServer = s.recv(1024)
        print(dataFromServer.decode())

        s.close()
    

    def skret_prawo(self):
        wartosc = int(self.ids.KAT.text)
        if(wartosc < 359):
            
            wartosc = wartosc+1
            self.ids.KAT.text = str(wartosc)

        elif(self.ids.KAT.text == '359'):
            #zmiana kata na 0
            wartosc = 0
            self.ids.KAT.text = str(wartosc)

        self.ids.img.stopnie = str(int(self.ids.img.stopnie) - 1)

        #polaczenie z serwerem za pomoca socket
        s = socket.socket()                    
        s.connect(('127.0.0.1', 12345))
            
        #wyslana komenda Prawo
        data = "Prawo";
        s.send(data.encode())
            
        #odpowiedz od serwera wypisana w terminalu klienta
        dataFromServer = s.recv(1024)
        print(dataFromServer.decode())

        s.close()
            
class ROTOR(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    ROTOR().run()

from cProfile import label
import string
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
from kivy.uix.boxlayout import BoxLayout


class App(App):
    def com1(self, instance, *args):
        label = Label()
        return label  

    def com2(self, instance, *args):
        label = Label()
        return label  

    def build(self):

        KAT = Label(text="0", size_hint=(1, 1), pos=(50, 50),color =[0.41, 0.42, 0.74, 1])
        katvar = KAT.text

        button1 = Button(text="LEWO", size_hint=(0.25, 1), pos=(350, 100))
        button1.bind(on_press=partial(self.com1, button1))

        button1.bind(on_press= self.skretLewo)

        button2 = Button(text="PRAWO", size_hint=(0.25, 1), pos=(350, 300))
        button2.bind(on_press=partial(self.com2, button2))

        mainLayout = BoxLayout()
        boxlayout = BoxLayout()

        boxlayout.add_widget(button1)
        boxlayout.add_widget(button2)

        mainLayout.add_widget(KAT)
        mainLayout.add_widget(boxlayout)
        return mainLayout

    def skretLewo(self, event):
        print(dir(self))
      
aplikacja = App()

aplikacja.run()

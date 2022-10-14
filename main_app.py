from distutils.command.build import build
from kivy.app import App
from kivy.uix.button import Button
# from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock
 

# Window.size = (600,600)
# Window.clearcolor=(210/255,128/255,122/255)


# Config.set('graphics', 'resizable', '0');
# Config.set('graphics', 'width', '500');
# Config.set('graphics', 'height', '500');



time_to_read = 5
class first_Screen(Screen, Label):
    
    def __init__(self, name = 'first'):
        super().__init__(name=name)
        box = FloatLayout(size = (300,300))
        txt = Label(text = 'Это Мой подгон за тот урок :)\nВаш первый вопрос:',size_hint=(0.3, 0.2), pos= (20,250))
        self.Unput = TextInput(text = 'Введи свой овтет',size_hint=(.40, 0.10), pos = (0,0))
        btn = Button(text = 'Next', size_hint=(0.3, 0.2), pos = (450,0))
        btn.on_press = self.next
        box.add_widget(self.Unput)
        box.add_widget(btn)
        box.add_widget(txt)
        self.add_widget(box)
    def next(self):
        # self.manager.transition.direction = 'up'
        # self.manager.current = 'first'
        if self.Unput.text == '21':
            self.manager.current = 'second'
        else:
            print('Govno')
    # def on_enter(self):
    #     Clock.schedule_once(self.lose, time_to_read)

    # def lose(self, dt):
        
    #     self.manager.current = 'second' 

    

class second_Screen(Screen):
    def __init__(self, name = 'second'):
        super().__init__(name=name)
        box = FloatLayout(size = (300,300))
        txt = Label(text = 'Ваш второй вопрос:',size_hint=(0.3, 0.2), pos= (8,250))
        self.Unput = TextInput(text = 'Введи свой овтет',size_hint=(.40, 0.10), pos = (0,0))
        btn = Button(text = 'Next', size_hint=(0.3, 0.2), pos = (450,0))
        btn.on_press = self.next
        box.add_widget(self.Unput)
        box.add_widget(txt)
        box.add_widget(btn)
        self.add_widget(box)
    def next(self):
        # self.manager.transition.direction = 'up'
        # self.manager.current = 'first'
        if self.Unput.text == '21':
            self.manager.current = 'three'
        else:
            print('Govno')
    # def on_enter(self):
    #     Clock.schedule_once(self.lose, time_to_read)

    # def lose(self, dt):
    #     print("Прошло", dt, "секунд")
    #     self.manager.current = 'first' 


class three_Screen(Screen):
    def __init__(self, name = 'three'):
        super().__init__(name=name)
        box = BoxLayout(padding=8, spacing=8)
        txt = Label(text = 'Call')
        btn = Button(text = 'Next')
        # btn.on_press = self.next
        box.add_widget(txt)
        box.add_widget(btn)
        self.add_widget(box)
    # def next(self):
    #     # self.manager.transition.direction = 'up'
    #     self.manager.current = 'four'

class four_Screen():
    ... 
class five_Screen():
    ...
class six_Screen():
    ...
class seven_Screen():
    ...
class eight_Screen():
    ...
class nine_Screen():
    ...
class ten_Screen():
    ...

class myApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(first_Screen())
        sm.add_widget(second_Screen())
        sm.add_widget(three_Screen())
        # sm.add_widget(four_Screen())
        # sm.add_widget(five_Screen())
        # sm.add_widget(six_Screen())
        # sm.add_widget(seven_Screen())
        # sm.add_widget(eight_Screen())
        # sm.add_widget(nine_Screen())
        # sm.add_widget(ten_Screen())
    
       
       
        return sm


if __name__ == "__main__":
    myApp().run()

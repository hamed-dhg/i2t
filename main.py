
from kivy.core import text
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
from kivy.core.text import LabelBase
import arabic_reshaper
import bidi.algorithm
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
import pytesseract as tess
from PIL import Image




class Switchscreen(ScreenManager):
    pass

class Mainpage(MDScreen):
    pass

class Resultpage(MDScreen):

    pass
        
        



class I2t(MDApp):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Window.bind(on_keyboard=self.events)
            self.manager_open = False
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager,
                select_path=self.select_path,
                preview=True,
            )
    
    imgpath=''      

    def build(self):
        self.icon='i2t.png'
        
        return Builder.load_file('main.kv')
       


    def back(self):
        self.root.current ='mainpage'

    
    def file_manager_open(self):
        self.file_manager.show('/home/hamed')  # output manager to the screen
        self.manager_open = True
        
    
    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
    
        self.exit_manager()
        toast(path)
        self.root.ids.mainpage.ids.mytext2.text=path
        self.root.ids.mainpage.ids.myimage.source=path
        self.imgpath = path

        
    def converti2ten(self):
        img =Image.open(self.imgpath)
        text=tess.image_to_string(img)
        self.root.ids.resultpage.ids.mytext.text=text
    




    
        
        

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()
        

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

        
        

    
    

I2t().run()

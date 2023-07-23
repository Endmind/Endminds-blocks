from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
from panda3d.core import loadPrcFileData
from direct.gui.OnscreenText import TextNode
from direct.gui.OnscreenText import TextFont
import maskpass
from mapmanager import MapManager
from controller import Controller
from editor import Editor
import sqlite3
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import base64
# from sqlalchemy.exc import IntegrityError, NoInspectionAvailable, InvalidRequestError
# from sqlalchemy.orm.exc import UnmappedInstanceError

nicks = ['Endmind','Lebofffski','nardi','']
passwords = ['1235Endmind','1234Leboffski','QWEdsaZXCnardi','']

def encode_pwd(plaintext_pwd: str):
    return base64.b64encode(plaintext_pwd)

def create_user(login: str = 'johndoe', password: str = '1234'):
    user_creds = {
        "login": login,
        "password": password
    }
    return user_creds

while True:
    nick = input('Введите имя пользователя: ')
    if nick in nicks:
        password = maskpass.askpass('Введите пароль: ')
        if password+nick in passwords:
            print('Вход успешно осуществлён! Запуск игры...')
            break
        else:
            print('Неверный пароль')
    else:
        print('Такой пользователь не зарегестрирован')
# Настройка конфигурации приложения
# Заголовок окна
loadPrcFileData('', "window-title Endmind's blocks")
# Отключение синхронизации
loadPrcFileData('', 'sync-video false')
# Включение отображения FPS
loadPrcFileData('', 'show-frame-rate-meter true')
# скрыть курсор мыши
loadPrcFileData('', 'cursor-hidden true')
# Установка размера окна
#loadPrcFileData('', 'win-size 1000 750')
loadPrcFileData('', 'win-size 1950 1100')

class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        '''font = loader.loadFont('Roboto.ttf')
        text = TextNode('node name')
        text.setText('роатфл')
        text.setFont(font)
        textNodePath = render.attachNewNode(text)
        textNodePath.setScale(0.15)
        textNodePath.setPos(o,5,-3)'''
        skybox = loader.loadModel('skybox.egg')
        skybox.setScale(40)
        skybox.reparentTo(render)
        # режим редактирования
        self.edit_mode = True

        # создаём менеджер карты
        self.map_manager = MapManager()

        # создаём контроллер мышки и клавиатуры
        self.controller = Controller()

        # создаём редактор
        self.editor = Editor(self.map_manager)

        # загружаем картинку курсора
        self.pointer = OnscreenImage(image='target.png',
                                     pos=(0, 0, 0), scale=0.08)
        # устанавливаем прозрачность
        self.pointer.setTransparency(TransparencyAttrib.MAlpha)

        # имя файла для сохранения и загрузки карт
        self.file_name = "my_map.dat"
        self.file_name1 = 'my_map copy.dat'
        self.file_name2 = 'my_map copy 2.dat'
        self.file_name3 = 'my_map copy 3.dat'
        self.file_name4 = 'my_map copy 4.dat'
        self.file_name5 = "my_map.dat"
        self.accept("f1", self.basicMap)
        self.accept("f2", self.generateRandomMap)
        self.accept("f3", self.saveMap)
        self.accept("f4", self.loadMap)
        self.accept("f5", self.setMapTo1)
        self.accept("f6", self.setMapTo2)
        self.accept("f7", self.setMapTo3)
        self.accept("f8", self.setMapTo4)
        self.accept("f9", self.setMapTo5)

        

        print("'f1' - создать базовую карту")
        print("'f2' - создать случайную карту")
        print("'f3' - сохранить карту")
        print("'f4' - загрузить карту")
        
        self.accept("1", self.setColor, [(1,1,1,1)])
        self.accept("2", self.setColor, [(1,0.3,0.3,1)])
        self.accept("3", self.setColor, [(0.3,1,0.3,1)])
        self.accept("4", self.setColor, [(0.3,0.3,1,1)])
        self.accept("5", self.setColor, [(1,1,0.3,0.5)])
        self.accept("6", self.setColor, [(0.3,1,1,0.25)])
        self.accept("7", self.setColor, [(1,0.3,1,0.5)])
        self.accept("8", self.setColor, [None])
        # зарегистрируйте метод переключения режима
        # как функцию обработки события нажатия на клавишу "tab"
        base.accept('tab',self.switchEditMode)

        # генерируем случайный уровень
        self.generateRandomMap()

    def basicMap(self):
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.basicMap()
        print('Basic map generated')

    def generateRandomMap(self):
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.generateRandomMap()
        print('Random map generated')

    def saveMap(self):
        self.map_manager.saveMap(self.file_name)
        print('Map saved to "'+self.file_name+'"')

    def loadMap(self):
        base.camera.setZ(20)
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.loadMap(self.file_name)
        print('Map loaded from "'+self.file_name+'"')


    # Метод переключения режима редактирования
    def switchEditMode(self):
        self.edit_mode = not self.edit_mode
        self.controller.setEditMode(self.edit_mode)
        self.editor.setEditMode(self.edit_mode)

        if self.edit_mode:
            self.pointer.setImage(image='target.png')
        else:
            self.pointer.setImage(image='target1.png')
        self.pointer.setTransparency(TransparencyAttrib.MAlpha)
    def setColor(self,color):
        if self.edit_mode:
            self.map_manager.setColor(color)
    def setMapTo1(self):
        self.file_name = self.file_name5
        print('Saving to 1')
    def setMapTo2(self):
        self.file_name = self.file_name1
        print('Saving to 2')
    def setMapTo3(self):
        self.file_name = self.file_name2
        print('Saving to 3')
    def setMapTo4(self):
        self.file_name = self.file_name3
        print('Saving to 4')
    def setMapTo5(self):
        self.file_name = self.file_name4
        print('Saving to 5')
app = Game()
app.run()

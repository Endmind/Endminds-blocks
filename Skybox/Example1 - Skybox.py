from direct.showbase.ShowBase import ShowBase
from controller import Controller

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/environment')
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 20, -3)
        # устанавливаем поле зрения объектива
        base.camLens.setFov(70)

        skybox = loader.loadModel('skybox.egg')
        skybox.setScale(40)
        skybox.reparentTo(render)

        # создаём контроллер мышки и клавиатуры
        self.controller = Controller()

        self.controller.setMovingStep(0.5)

game = Game()
game.run()

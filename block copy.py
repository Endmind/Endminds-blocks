from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenText import TextNode
from direct.gui.OnscreenText import TextFont
from panda3d.core import TextProperties


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/environment')
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)


        font = loader.loadFont('Roboto.ttf')
        font.setPixelsPerUnit(80)


        TextProperties.setDefaultFont(font)


        textObject1 = OnscreenText(text="Test Проверка 123",
                pos=(0, 0), scale=0.2,
                fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1))


        textObject2 = OnscreenText(text="Test Проверка 123",
                pos=(-0.05, -0.25), scale=0.2,
                fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1),
                bg=(0, 0, 1, 1), frame = (0, 1, 1, 1),
                parent=base.a2dTopRight,
                align=TextNode.ARight)




game = Game()
game.run()

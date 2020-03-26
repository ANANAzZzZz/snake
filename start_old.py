from cocos.scene import Scene
from cocos.director import director
from classes.Game import Game

director.init()

mySnakeGame = Game()
mySnakeGame.initTimer()

myScene = Scene(mySnakeGame)
director.run(myScene)
from cocos.scene import Scene
from cocos.director import director
from classes.SnakeGame import SnakeGame

director.init()

mySnakeGame = SnakeGame()
mySnakeGame.initTimer()

myScene = Scene(mySnakeGame)
director.run(myScene)
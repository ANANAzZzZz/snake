from cocos import scene
from cocos.director import director
from classes.SnakeGame import SnakeGame

director.init()

mySnakeGame = SnakeGame()
mySnakeGame.initTimer()

myScene = scene.Scene(mySnakeGame)
director.run(myScene)
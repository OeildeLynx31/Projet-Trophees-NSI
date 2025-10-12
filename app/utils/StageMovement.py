import pygame

def getRelativePos(stage, x, y):
    relX = x + stage.scroll[0]
    relY = y + stage.scroll[1]
    return [relX, relY]

def getStaticPos(stage, x, y):
    statX = x - stage.scroll[0]
    statY = y - stage.scroll[1]
    return [statX, statY]
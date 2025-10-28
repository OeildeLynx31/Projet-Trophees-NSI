import pygame
import os

class Slider:
    def __init__(self, x, y, width, height, min, max, initialValue, step=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min = min
        self.max = max
        self.step = step

        self.sliding = False
        self.value = initialValue

        self.line = pygame.Rect(x, y + (height / 2), width, 5)
        self.cursor = pygame.Rect(self.getPosForValue(self.value), y+2.5, 10, height)

    def draw(self, surface):
        if (self.isClicked()):
            self.sliding = True
        if (not pygame.mouse.get_pressed()[0]):
            self.sliding = False
        if (self.sliding == True):
            newX = pygame.mouse.get_pos()[0]
            self.cursor.x = self.getStepPos(newX)
            print("val:", self.value)

        pygame.draw.rect(surface, pygame.Color(255, 255, 255, 255), self.line)
        pygame.draw.rect(surface, pygame.Color(255, 255, 255, 255), self.cursor)

    def getValueForPos(self, pos):
        val = (pos - self.x) * (self.max - self.min) / self.width
        val = round(val/self.step)*self.step
        if (val > self.max):
            val = self.max
        elif (val < self.min):
            val = self.min
        return val

    def getPosForValue(self, value):
        return self.x + (self.width / (self.max - self.min) * value - 5)

    def getStepPos(self, pos):
        self.value = self.getValueForPos(pos)
        return self.getPosForValue(self.getValueForPos(pos))

    def isHovered(self):
        mousePos = pygame.mouse.get_pos()
        return self.cursor.collidepoint(mousePos[0], mousePos[1])

    def isClicked(self):
        if (pygame.mouse.get_pressed()[0] and self.isHovered()):
            return True
        else:
            return False

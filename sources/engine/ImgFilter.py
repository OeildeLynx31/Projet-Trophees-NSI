import pygame
from PIL import Image, ImageFilter

def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert_alpha()
        
def surfaceToPilImage(surface, formatType="RGBA"):
    return Image.frombytes(
        formatType, surface.get_size(), pygame.image.tostring(surface, formatType, False))

def damageFilter(img):
    img = surfaceToPilImage(img)
    newimg = Image.new("RGBA", (img.width, img.height))
    for posX in range(img.width):
        for posY in range(img.height):
            px = img.getpixel((posX, posY))
            newimg.putpixel((posX, posY), (255, px[1], px[2], px[3]))
    return pilImageToSurface(newimg)


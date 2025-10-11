import pygame
import os

def get_sprite_collision_rects(image_surface):
    # Return a list of rects for each area of non-transparent pixels.
    mask = pygame.mask.from_surface(image_surface)
    rects = mask.get_bounding_rects()
    return rects

def get_collision_rects_for_background(path, file):
    background = pygame.transform.scale(pygame.image.load(os.path.join(path, file.replace(".png", ".hitbox.png"))), (1280, 720)).convert_alpha()
    return get_sprite_collision_rects(background)

def get_enlarged_hitbox(rect, marginX, marginY):
    enlargedBox = rect.copy()
    enlargedBox.x = enlargedBox.x + marginX
    enlargedBox.y = enlargedBox.y + marginY
    return enlargedBox
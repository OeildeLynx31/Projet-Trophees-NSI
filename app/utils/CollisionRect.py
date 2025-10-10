import pygame

def get_sprite_collision_rects(image_surface):
    # Return a list of rects for each area of non-transparent pixels.
    mask = pygame.mask.from_surface(image_surface)
    rects = mask.get_bounding_rects()
    return rects
import pygame
import os

class Slot:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.item = None  # Holds an Item object or None
        self.quantity = 0

        # Placeholder for slot background image
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((50, 50, 50, 150)) # A semi-transparent dark gray rectangle

    def add_item(self, item, quantity=1):
        if self.item is None:
            self.item = item
            self.quantity = quantity
        elif self.item == item: # Assuming item objects can be compared
            self.quantity += quantity
        else:
            return False # Slot already has a different item
        return True

    def remove_item(self, quantity=1):
        if self.item is None:
            return False # No item to remove
        
        if self.quantity <= quantity:
            removed_item = self.item
            self.item = None
            self.quantity = 0
            return removed_item
        else:
            self.quantity -= quantity
            return self.item # Return a reference to the item type

    def is_empty(self):
        return self.item is None

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        if self.item:
            # Placeholder: Draw item image. Assuming item has an 'image' attribute
            # Need to scale item image to fit slot or handle its size
            item_image = self.item.image # This would come from an actual Item class
            # For now, draw a colored rectangle to represent an item
            pygame.draw.rect(screen, (255, 0, 0), self.rect.inflate(-10, -10)) # Red rectangle inside slot
            # You would blit the actual item image here, scaled to fit
            # screen.blit(pygame.transform.scale(item_image, (self.rect.width - 10, self.rect.height - 10)), self.rect.topleft + (5, 5))
            
            # Draw quantity if more than 1
            if self.quantity > 1:
                # Placeholder for font and text rendering
                font = pygame.font.Font(None, 20) # Replace with actual font loading
                text_surface = font.render(str(self.quantity), True, (255, 255, 255))
                screen.blit(text_surface, (self.rect.right - text_surface.get_width() - 5, self.rect.bottom - text_surface.get_height() - 5))

'''A collection of advanced pygame sprites.'''
import os
from os.path import join

import pygame

def load_image(*path):
    '''
    Loads an image from a path.

    Expect a folder named images to be the same directory which should
    contain the images to be loaded.
    '''
    return pygame.image.load(join(os.getcwd(), 'images', *path)).convert_alpha()

class View(pygame.sprite.Group):
    '''
    A sprite representation.
    
    A view is expected to define image and layer.
    '''

    def add_internal(self, sprite):
        self.initialize(sprite)
        super(View, self).add_internal(sprite)
    
    def initialize(self, sprite):
        '''Initialize the sprite.'''
        sprite.image = self.image
        sprite.rect = sprite.image.get_rect()
        sprite._layer = self.layer
    
    def draw(self, sprite):
        '''Render the sprite.'''
        sprite.rect.center = sprite.position

    def draw_all(self, surface):
        for sprite in self.sprites(): self.draw(sprite)
        super(View, self).draw(surface)

class RotatableView(View):
    '''
    A rotatable view.

    Expects the sprite to have a variable named heading which represents
    the heading of the sprite.
    '''
    
    def draw(self, sprite):
        sprite.image = pygame.transform.rotate(self.image, sprite.heading)
        super(RotatableView, self).draw(sprite)

class LayeredView(pygame.sprite.LayeredUpdates):
    def draw(self, sprite):
        '''Render the sprite.'''
        sprite.views[0].draw(sprite)
    
    def draw_all(self, surface):
        for sprite in self.sprites(): self.draw(sprite)
        super(LayeredView, self).draw(surface)

    
    

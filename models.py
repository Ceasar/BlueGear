'''A collection of advanced pygame sprites.'''
import pygame.sprite

from events import Client

class Manager(pygame.sprite.Group, Client):
    '''A base manager object responsible for updating models.'''

    def update(self, sprite, context):
        sprite.objects.update(sprite, context)

    def update_all(self, context):
        for sprite in self.sprites(): self.update(sprite, context)

    def notify(self, event):
        if isinstance(event, TickEvent):
            self.update_all({'dt': event.dt})

class Model(pygame.sprite.Sprite):
    '''
    A framework for easier sprite creation.

    Models are expected to have a position attribute.
    '''

    def __init__(self):
        super(Model, self).__init__(self.objects, self.views)

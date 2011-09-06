import pygame.time

from event import Event

class TickEvent(Event):
    pass

class Timer(object):
    def __init__(self, framerate=0):
        self.clock = pygame.time.Clock()
        self.framerate = framerate
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            time_passed_ms = self.clock.tick(self.framerate)
            TickEvent()

    def stop(self):
        self.running = False

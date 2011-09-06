import pygame.display
import os

from views import LayeredView

class Background(pygame.Surface):
    def __init__(self, size, color):
        print "initializing background..."
        pygame.Surface.__init__(self, size)
        self.fill(color)

class Screen(object):
    '''A easy to use screen object.

    >>>with Screen(DIMENSION) as screen:
        #do stuff
    If an exception is thrown, the Screen object will automatically call
    pygame.quit() killing the game. (pygame.quit is also IDLE friendly.)
    '''
    def __init__(self, size, bg_color=(0,0,0)):
        print "initializing view..."
        self.background = Background(size, bg_color)
        self.size = size
        self.screen = None
        self.view = LayeredView()

    def register(self, *entities):
        for entity in entities:
            entity.views.append(self.view)
    
    def __enter__(self):
        print "initializing pygame..."
        pygame.init()
        print "initalizing screen..."
        #This line centers the screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.background, (0, 0))
        return self

    def __exit__(self, type, value, traceback):
        pygame.quit()

    def refresh(self):
        self.view.clear(self.screen, self.background)
        self.view.draw_all(self.screen)
        pygame.display.flip()

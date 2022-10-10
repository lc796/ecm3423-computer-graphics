from OpenGL.GL import *
import pygame


class Camera:
    '''
    Basic class for handling the camera pose. At this stage, just x and y offsets.
    '''

    def __init__(self, size):
        self.size = size
        self.position = [0.0, 0.0, 0.0]

    def apply(self):
        '''
        Apply the camera parameters to the current OpenGL context
        Note that this is the old-fashioned API, we will use matrices in the
        future.
        '''
        glTranslate(*self.position)

    def keyboard(self, event):
        '''
        Handles keyboard events that are related to the camera.
        '''
        if event.key == pygame.K_PAGEDOWN:
            self.position[2] += 0.01

        if event.key == pygame.K_PAGEUP:
            self.position[2] -= 0.01

        if event.key == pygame.K_DOWN:
            self.position[1] += 0.01

        if event.key == pygame.K_UP:
            self.position[1] -= 0.01

        if event.key == pygame.K_LEFT:
            self.position[0] += 0.01

        if event.key == pygame.K_RIGHT:
            self.position[0] -= 0.01

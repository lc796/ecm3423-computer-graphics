from OpenGL.GL import *
import pygame

from ecm3423.camera import Camera


class Scene:
    '''
    This is the main class for drawing an OpenGL scene using the PyGame library
    '''

    def __init__(self):
        '''
        Initialises the scene
        '''

        self.window_size = (800, 600)

        # the first two lines initialise the pygame window. You could use another library for this,
        # for example GLut or Qt
        pygame.init()
        screen = pygame.display.set_mode(self.window_size, pygame.OPENGL | pygame.DOUBLEBUF, 24)

        # Here we start initialising the window from the OpenGL side
        glViewport(0, 0, self.window_size[0], self.window_size[1])

        # this selects the background colour
        glClearColor(0.0, 0.5, 0.5, 1.0)

        self.camera = Camera(self.window_size)

        # This class will maintain a list of models to draw in the scene,
        # we will initalise it to empty
        self.models = []

    def add_model(self, model):
        '''
        This method just adds a model to the scene.
        :param model: The model object to add to the scene
        :return: None
        '''
        self.models.append(model)

    def draw(self):
        '''
        Draw all models in the scene
        :return: None
        '''

        # first we need to clear the scene
        glClear(GL_COLOR_BUFFER_BIT)

        # saves the current position
        glPushMatrix()

        # apply the camera parameters
        self.camera.apply()

        # then we loop over all models in the list and draw them
        for model in self.models:
            model.draw()

        # retrieve the last saved position
        glPopMatrix()

        # once we are done drawing, we display the scene
        # Note that here we use double buffering to avoid artefacts:
        # we draw on a different buffer than the one we display,
        # and flip the two buffers once we are done drawing.
        pygame.display.flip()

    def keyboard(self, event):
        if event.key == pygame.K_q:
            self.running = False

        elif event.key == pygame.K_0:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);

        elif event.key == pygame.K_1:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

        self.camera.keyboard(event)

    def run(self):
        '''
        Draws the scene in a loop until exit.
        '''

        # We have a classic program loop
        running = True
        while running:

            # check whether the window has been closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # keyboard events
                elif event.type == pygame.KEYDOWN:
                    self.keyboard(event)

                elif False and event.type == pygame.MOUSEMOTION:
                    if pygame.MOUSEBUTTONDOWN:
                        dx, dy = event.rel
                        self.camera.position[0] -= dx / self.window_size[0] / 10 - 0.5
                        self.camera.position[1] -= dy / self.window_size[1] / 10 - 0.5

            # otherwise, continue drawing
            self.draw()

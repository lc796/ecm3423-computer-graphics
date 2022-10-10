from OpenGL.GL import *
import numpy as np


class BaseModel:
    '''
    Base class for all models, implementing the basic draw function for triangular meshes.
    Inherit from this to create new models.
    '''

    def __init__(self, position=[0, 0, 0], orientation=0, scale=1, color=[1, 1, 1]):
        '''
        Initialises the model data
        '''

        # store the object's color
        self.color = color

        # store the position of the model in the scene, ...
        self.position = position

        # ... the orientation, ...
        self.orientation = orientation

        # ... and the scale factor
        if np.isscalar(scale):
            self.scale = [scale, scale, scale]
        else:
            self.scale = scale

    def apply_parameters(self):
        # apply the position and orientation of the object
        glTranslate(*self.position)
        glRotate(self.orientation, 0, 0, 1)

        # apply scaling across all dimensions
        glScale(*self.scale)

        # then set the colour
        glColor(self.color)

    def draw(self):
        '''
        Draws the model using OpenGL functions
        :return:
        '''

        # saves the current pose parameters
        glPushMatrix()

        self.apply_parameters()

        # Here we will use the simple GL_TRIANGLES primitive, that will interpret each sequence of
        # 3 vertices as defining a triangle.
        glBegin(GL_TRIANGLES)

        # we loop over all vertices in the model
        for vertex in self.vertices:
            # This function adds the vertex to the list
            glVertex(vertex)

        # the call to glEnd() signifies that all vertices have been entered.
        glEnd()

        # retrieve the previous pose parameters
        glPopMatrix()

        def applyPose(self):
            # apply the position and orientation and size of the object
            glScale(self.scale, self.scale, self.scale)
            glRotate(self.orientation, 0, 0, 1)
            glTranslate(*self.position)
            glColor(self.color)


class TriangleModel(BaseModel):
    '''
    A very simple model for drawing a single triangle. This is only for illustration purpose.
    '''

    def __init__(self, position=[0, 0, 0], orientation=0, scale=1, color=[1, 1, 1]):
        BaseModel.__init__(self, position=position, orientation=orientation, scale=scale, color=color)

        # each row encodes the coordinate for one vertex.
        # given that we are drawing in 2D, the last coordinate is always zero.
        self.vertices = np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [1.0, 1.0, 0.0]
            ], 'f')


class ComplexModel(BaseModel):
    '''
    Base class for a complex model, that is composed of other models.
    '''

    def draw(self):
        glPushMatrix()

        # apply the parameters for the whole model
        self.apply_parameters()

        # draw all component primitives
        for component in self.components:
            component.draw()

        glPopMatrix()


class SquareModel(ComplexModel):
    '''
    Simple class for drawing a square using two triangles.
    '''

    def __init__(self, position=[0, 0, 0], orientation=0, scale=1, color=[1, 1, 1]):
        BaseModel.__init__(self, position=position, orientation=orientation, scale=scale)
        self.components = [
            TriangleModel(position=[0, 0, 0], scale=1, orientation=0, color=color),
            TriangleModel(position=[1, 1, 0], scale=1, orientation=180, color=color)
        ]


class TreeModel(ComplexModel):
    '''
    Drawing a tree using triangles.
    '''

    def __init__(self, position=[0, 0, 0], orientation=0, scale=1):
        BaseModel.__init__(self, position=position, orientation=orientation, scale=scale)

        # list of simple components
        self.components = [
            SquareModel(position=[-.125, 0.125, 0], scale=0.25, orientation=0, color=[0.6, 0.2, 0.2]),
            TriangleModel(position=[0, 0, 0], scale=0.5, orientation=45, color=[0, 1, 0]),
            TriangleModel(position=[0, 0.25, 0], scale=0.5, orientation=45, color=[0, 1, 0]),
            TriangleModel(position=[0, 0.5, 0], scale=0.5, orientation=45, color=[0, 1, 0])
        ]


class HouseModel(ComplexModel):
    '''
    Simple class for drawing a house from simple shapes.
    '''

    def __init__(self, position=[0, 0, 0], orientation=0, scale=1):
        BaseModel.__init__(self, position=position, orientation=orientation, scale=scale)

        # list of simple components
        self.components = [
            SquareModel(position=[0, 0.1, 0], scale=0.6, orientation=0, color=[0.9, 0.9, 0.9]),
            TriangleModel(position=[0.3, 0.3, 0], scale=0.5, orientation=45, color=[0.9, 0.1, 0]),
            SquareModel(position=[0.05, 0.4, 0], scale=0.2, orientation=0, color=[0.7, 0.7, 0.9]),
            SquareModel(position=[0.35, 0.4, 0], scale=0.2, orientation=0, color=[0.7, 0.7, 0.9]),
            SquareModel(position=[0.5, 0.10, 0], scale=0.2, orientation=90, color=[0.6, 0.2, 0.2]),
        ]

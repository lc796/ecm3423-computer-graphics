from ecm3423.models import TreeModel, HouseModel
from scene import Scene

if __name__ == '__main__':
    # initialises the scene object
    scene = Scene()

    # adds a few objects to the scene
    scene.add_model(TreeModel(position=[0.4,0,0], scale=0.5))
    scene.add_model(TreeModel(position=[0.7, 0.25, 0], scale=0.4))
    scene.add_model(TreeModel(position=[0.1, 0.10, 0], scale=0.3))
    scene.add_model(TreeModel(position=[-0.1, 0.40, 0], scale=0.2))
    scene.add_model(HouseModel(position=[-0.9,-0.5,0]))

    # starts drawing the scene
    scene.run()
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3, Point3
from direct.task import Task
import sys

class RacingGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Disable default mouse-based camera control
        self.disableMouse()
        
        # Load a simple environment (you can use a more detailed track if you have one)
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25)
        self.environ.setPos(-8, 42, 0)
        
        # Load the car model (make sure you have a car model in the models folder)
        self.car = self.loader.loadModel("models/car")  # Replace with your actual model file
        self.car.reparentTo(self.render)
        self.car.setScale(0.5)
        self.car.setPos(0, 0, 0)
        
        # Setup camera to follow the car
        self.camera.setPos(0, -20, 10)
        self.camera.lookAt(self.car)
        
        # Accept key events for controlling the car
        self.accept("escape", sys.exit)
        self.accept("arrow_up", self.set_key, ["forward", True])
        self.accept("arrow_up-up", self.set_key, ["forward", False])
        self.accept("arrow_down", self.set_key, ["backward", True])
        self.accept("arrow_down-up", self.set_key, ["backward", False])
        self.accept("arrow_left", self.set_key, ["left", True])
        self.accept("arrow_left-up", self.set_key, ["left", False])
        self.accept("arrow_right", self.set_key, ["right", True])
        self.accept("arrow_right-up", self.set_key, ["right", False])
        
        # Dictionary to hold key states
        self.keyMap = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False
        }
        
        # Car movement variables
        self.speed = 25        # units per second
        self.turn_rate = 80    # degrees per second
        
        # Add an update task to move the car
        self.taskMgr.add(self.update, "updateTask")
    
    def set_key(self, key, value):
        self.keyMap[key] = value
    
    def update(self, task):
        dt = globalClock.getDt()
        
        # Move forward/backward
        if self.keyMap["forward"]:
            self.car.setPos(self.car, Vec3(0, self.speed * dt, 0))
        if self.keyMap["backward"]:
            self.car.setPos(self.car, Vec3(0, -self.speed * dt, 0))
        
        # Rotate left/right
        if self.keyMap["left"]:
            self.car.setH(self.car.getH() + self.turn_rate * dt)
        if self.keyMap["right"]:
            self.car.setH(self.car.getH() - self.turn_rate * dt)
        
        # Update camera to follow the car
        # (This sets the camera relative to the car position)
        cam_pos = self.car.getPos() + Vec3(0, -20, 10)
        self.camera.setPos(cam_pos)
        self.camera.lookAt(self.car)
        
        return Task.cont

# Run the game
if __name__ == "__main__":
    game = RacingGame()
    game.run()

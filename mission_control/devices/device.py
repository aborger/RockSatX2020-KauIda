"""

* The Device class is inherited by the the devices on board the KuaIda payload.

* The main mission_control.py script is simpler because each device only has these 4 methods.

* Author: Aaron Borger <aborger@nnu.edu, (307)534-6265>

"""

from abc import ABC, abstractmethod

class Device(ABC):

    @abstractmethod
    def setup(self):
        return

    @abstractmethod
    def activate(self):
        return

    @abstractmethod
    def deactivate(self):
        return

    @abstractmethod
    def shutdown(self):
        return

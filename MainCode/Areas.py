from Erros import *
global areasList
areasList = {}

class Area:
    def __init__(self, name, centerpos=None, width=None, height=None, device=None,action=None, origin=None, end=None):

        if centerpos:
            self.width = width
            self.height = height
            self.centerpos = centerpos
            origin = (int(centerpos[0] - (width / 2)), int(centerpos[1] - (height / 2)))
            end = (int(centerpos[0] + (width / 2)), int(centerpos[1] + (height / 2)))
        if origin and end:
            self.origin = origin
            self.end = end
        else:
           raise MissingPositionError()
        self.device = device
        self.action = action
        self.name = name
        areasList[self.name] = self
    def infos(self, info="all"):

        infos = {
            "origin": self.origin,
            "end": self.end,
            "width": self.width,
            "height": self.height,
            "centerpos": self.centerpos
        }
        if info == "all":
            return infos
        else:
            return infos[info]



    def _isHandInside(self, handPos):
        return self.origin[0] <= handPos[0] <= self.end[0] and self.origin[1] <= handPos[1] <= self.end[1]

    def _ToggleDeviceState(self):
        if self.device and self.device.state != None:
            self.device._ToggleState()
        else:
            raise AreaNotAssociatedWithAnyDevice()


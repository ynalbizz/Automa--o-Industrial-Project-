class MissingPositionError(Exception):
    def __init__(self, message="Center position or origin/end points are missing."):
        self.message = message
        super().__init__(self.message)

class DeviceError(Exception):
    def __init__(self, device):
        self.device = device
        self.message = f"Attempt to connect with Device '{device}' is Failed"
        super().__init__(self.message)

class InvalidActionError(Exception):
    def __init__(self, action):
        self.action = action
        self.message = f"Action '{action}' is not valid."
        super().__init__(self.message)

class AreaNotAssociatedWithAnyDevice(Exception):
    def __init__(self, message="Area not associated with any device"):
        self.message = message
        super().__init__(self.message)

class KeyBuilder:
    def __init__(self):
        self.key = None
        self.steps = []

    def reset(self):
        self.key = None
        self.steps = []

    def set_initial_step(self, image):
        return self

    def set_step(self, image, area, action):
        return self

    def build(self):
        return self.key

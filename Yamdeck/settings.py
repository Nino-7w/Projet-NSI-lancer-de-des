class Settings:
    def __init__(self):
        self.volume = 0.2  # Entre 0.0 et 1.0
        self.resolutions = [(800, 500), (1024, 768), (1280, 720)]
        self.res_index = 0
        
    def get_res(self):
        return self.resolutions[self.res_index]

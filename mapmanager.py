from direct.showbase.ShowBase import ShowBase

class Mapmanager(ShowBase):
    def __init__(self, render, loader, file):
        self.loader = loader
        self.render = render
        self.land = None
        self.texture = 'block.png'
        self.model = 'block.egg'
        self.colors = [(0.2,0.2,0.35,1), (1,0,0,1), (0,0,1,1), (0.2,0.2,0,1)]
        self.file = open('map.txt', )
        self.color = (0.2, 0.2, 0.35, 1)
        self.startNew()
        self.load_land(file)
    
    def clear(self):
        if self.land:
            self.land.remove_node()
        self.startNew()

    def load_land(self, file):
        file = open(file)
        file = file.readlines()
        y = 0
        for string in file:
            x = 0
            string_list = string.split(' ')
            for z in string_list:
                for z_cor in range(int(z)+1):
                    self.addBlock(self.setColor(z_cor), (x,y,z_cor))
                x+=1
            y+=1     

    def setColor(self, z_cor):
        lenght = len(self.colors)
        if z_cor > len(self.colors) - 1:
            return self.setColor(z_cor - lenght)
        return self.colors[z_cor]

    def addBlock(self, color, pos):
        self.block = self.loader.loadModel(self.model)
        texture = self.loader.loadTexture(self.texture)
        self.block.setTexture(texture)
        self.block.setColor(color)
        self.block.setPos(pos)
        self.block.reparentTo(self.land)
    
    def startNew(self):
        self.land = self.render.attachNewNode("Land")
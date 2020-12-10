class charactar:

    speed = 30
    points = 0
    sprite = None

    def __init__(self):
        print("de constructor van charactar")

    def walk(self):
        print("charactar loopt nu met snelheid", self.speed)

class goomba (charactar):

    lives = 3
    item = None

    def __init__(self):

        super().__init__()

        self.speed = 10
    
    def walk(self):
        print("goomba loopt heel anders maar wel met snelheid", self.speed)

    def jump(self):
        print("jump")


characterA = charactar()
goombaD = goomba()

characterA.walk()
goombaD.walk()

print(characterA.speed)
print(goombaD.speed)
print(goombaD.lives)



print(goombaD)
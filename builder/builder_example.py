from abc import ABCMeta, abstractmethod

class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.body, self.arm, self.leg)


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass
    
    @abstractmethod
    def build_leg(self):
        pass

class PrettyGirlBuilder(PlayerBuilder):
    
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "pretty face"

    def build_body(self):
        self.player.body = "slim body"
    def build_arm(self):
        self.player.arm = "long arm"
    def build_leg(self):
        self.player.leg = "long leg"

class Monster(PlayerBuilder):
    
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "ugly face"

    def build_body(self):
        self.player.body = "huge body"
    def build_arm(self):
        self.player.arm = "hairy arm"
    def build_leg(self):
        self.player.leg = "hairy leg"    


class PlayerDirector: # 控制组装顺序
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client 

builder = PrettyGirlBuilder()
director = PlayerDirector()

p = director.build_player(builder)
print(p)

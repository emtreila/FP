class Player:
    def __init__(self, name, strength, player_id: int = None):
        self._name = name
        self._strength = strength
        self._player_id = player_id

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, new):
        self._player_id = new

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, new):
        self._strength = new

    def __str__(self):
        return f"Id: {self.player_id}, Name: {self.name}, Strength: {self.strength}"

    def __repr__(self):
        return self.__str__()

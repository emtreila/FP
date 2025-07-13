class Address:
    def __init__(self, name, number, x, y):
        self._address_id = None
        self._name = name
        self._number = number
        self._x = x
        self._y = y

    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, new):
        self._address_id = new

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new):
        self._number = new

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new):
        self._x = new

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new):
        self._y = new

    def __str__(self):
        return f"Id: {self._address_id}, Name: {self._name}, Number: {self._number}, x= {self._x}, y= {self._y}"

    def __repr__(self):
        return self.__str__()

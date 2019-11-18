import random
from enum import enum


class Mine:
    def __init__(self):
        pass
    def __repr__(self):
        return str(self._value)

    # set five variables
    # x, y, value, mine_around and status
    # getter and setter and property function
    def get_x(self):
        return self._x

    def set_x(self):
        self._x = x

    x = property(fget=get_x, fset=set_x)
    
    def get_y(self):
        return self._y

    def set_x(self):
        self._y = y

    y = property(fget=get_y, fset=set_y)

    def get_value(self):
        return self._value

    def set_value(self):
        self._value = value

    value = property(fget=get_value, fset=set_value)

    def get_mine_around(self):
        return self._mine_around

    def set_mine_around(self):
        self._mine_around = mine_around

    mine_around = property(fget=get_mine_around, fset=set_around)        

    def get_status(self):
        return self._status

    def set_status(self):
        self._status = status

    status = property(fget=get_status, fset=set_status)
        
        

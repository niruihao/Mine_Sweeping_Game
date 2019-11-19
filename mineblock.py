import random
from enum import Enum

class blockstat(Enum):
    normal = 1  # not_click
    opened = 2  # clicked
    mine = 3    # mine
    flag = 4    # set as min
    ask = 5     # set a ?
    bomb = 6    # step on the bomb
    hint = 7    # blocks around the both click
    double = 8  # both click the mouse
    wrong = 9   # made mistake, set blank as mine

class Mine:

    # set five variables
    # x, y, value, mine_around and status
    # getter and setter and property function

    def __init__(self, x, y, value):
        self._x = x
        self._y = y
        self._value = 0
        self._mine_around = -1
        self._status = blockstat.normal

    def __repr__(self):
        return str(self._value)

    
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
    	if value:
    		self._value = 1
    	else:
    		self._value = 0

    value = property(fget=get_value, fset=set_value, doc='0:non-mine 1:mine')

    def get_mine_around(self):
        return self._mine_around

    def set_mine_around(self):
        self._mine_around = mine_around

    mine_around = property(fget=get_mine_around, fset=set_around)

    def get_status(self):
        return self._status

    def set_status(self):
        self._status = status

    status = property(fget=get_status, fset=set_status,'blockstat')
        
        

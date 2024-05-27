#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=9):
        self.brand=brand
        self.size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        """size must be an integer"""
        if not isinstance(size, int):
            print("size must be an integer")
        self._size = size
        
    @property
    def brand(self):
        """The brand property"""
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand
        
        
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    
 
stansmith = Shoe("Adidas" , 10)
stansmith.cobble()  
   
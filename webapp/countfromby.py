#! /usr/bin/env pethon3

class CountFromBy:
    
    def __init__(self, v: int=0, i: int=1) -> None:
#        pass
        self.val = v
        self.incr = i
    
    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)


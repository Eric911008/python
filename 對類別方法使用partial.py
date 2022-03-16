#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
對類別方法使用partial

@author: linweicheng
"""

import functools
help(functools)

if __name__ == "__main__":
    class Hero:
        DEFAULT_NAME = "Superman"
        def __init__(self):
            self.name = self.DEFAULT_NAME
            
        def rename(self, new_name):
            self.name = new_name
            
        reset_name = functools.partialmethod(rename, new_name = "Batman")
        
        def __repr__(self):
            return f"HERO({self.name!r})"
        
if __name__ == "__main__":
    hero = Hero()
    assert hero.name == "Superman"
    hero.rename("Batman")
    assert hero.name == "Batman"
    hero.reset_name()
    assert hero.name == "Batman"
    print("___" * 5)
    print("程式正常執行")
        
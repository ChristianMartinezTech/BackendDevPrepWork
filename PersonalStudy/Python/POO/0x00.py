#!/usr/bin/python3
"""OOP playtesting with Minecraft"""

class Cube:
    """Cube Class"""
    id = 0
    
    def __init__(self, material, color):
        self.material = material
        self.color = color

        Cube.id += 1
    
    @classmethod
    def instance_print(cls):
        print(cls)
        print(cls.material)
        print(cls.color)
        print(cls.id)
        print("---")

    def behavior(cls):
        if cls.material == "Sand":
            print("This is sand")
        if cls.material == "Wood":
            print("This is wood")

# Instanciating objects
cube_example_1 = Cube("Sand", "white")
cube_example_2 = Cube("Wood", "brown")
cube_example_3 = Cube("Sand", "brown")

# Calling the instance_print method
cube_example_1.instance_print()
cube_example_2.instance_print()
cube_example_3.instance_print()

""" Calling the behavior method
Cube.behavior(cube_example_1)
Cube.behavior(cube_example_2)
Cube.behavior(cube_example_3)"""
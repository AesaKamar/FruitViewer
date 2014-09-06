import os
import time

f = open(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'/db/seeds.rb', 'w')

f.write('fruits = Fruit.create([')

f.write()

f.write('])')
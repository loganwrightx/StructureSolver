"""
Author: Logan Wright

File: main.py
"""

# Custom modules
from structure_tools import (
  Joint,
  Structure,
  Vector
)

# Third-party modules

# Builtin modules
from argparse import ArgumentParser

def main():
  ap = ArgumentParser(description="StructureSolver automation tool")
  
  j1 = Joint(Vector(0, 0, 0))
  j2 = Joint(Vector(1, 1, 0))
  
  s = Structure()
  s.add(j1)
  s.add(j2)
  
  print(s)

if __name__ == "__main__":
  main()
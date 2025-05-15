"""
Author: Logan Wright

File: joint.py
"""

# Custom modules
from .joint import Joint as _Joint

# Third-party modules

# Builtin modules
from typing import Dict as _Dict

class Structure:
  """A class to represent a joint section between trusses in a structure"""
  _instance = None
  _joints: _Dict[int, _Joint] = {}
  def __new__(cls):
    if not cls._instance:
      cls._instance = super(Structure, cls).__new__(cls)
    
    return cls._instance
  
  def __init__(self):
    pass
  
  def add(self, joint: _Joint) -> None:
    """Adds a joint to the structure"""
    self._joints[joint.idx] = joint
  
  def __repr__(self) -> str:
    return f"Structure: {[(idx, vec.pos) for idx, vec in self._joints.items()]}"

__all__ = [
  "Structure"
]
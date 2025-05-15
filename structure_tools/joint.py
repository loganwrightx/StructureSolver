"""
Author: Logan Wright

File: joint.py
"""

from __future__ import annotations

# Custom modules
from .vector import Vector as _Vector

# Third-party modules

# Builtin modules

class Joint:
  """A class to represent a joint section between trusses in a structure"""
  _counter = 0
  _idx = 0
  _pos: _Vector
  _ext_forces = _Vector(0, 0, 0)
  _adjacents = set()
  def __init__(self, pos: _Vector):
    self._pos = pos
    Joint._counter += 1
    self._idx = Joint._counter
  
  def connect(self, adjacent: Joint) -> None:
    """Add truss connecting joints by defining an adjacent joint"""
    self._adjacents.add(adjacent)
  
  def load(self, force: _Vector) -> None:
    """Adds external load to equillibrium equation"""
    self._ext_forces += force
  
  def lock(self) -> None:
    """Convert set of adjacents to frozenset for better memory optimization"""
    self._adjacents = frozenset(self._adjacents)
  
  @property
  def pos(self) -> _Vector:
    return self._pos
  
  @property
  def idx(self) -> int:
    return self._idx

__all__ = []
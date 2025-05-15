"""
Author: Logan Wright

File: main.py
"""

# Custom modules

# Third-party modules
from numpy import ndarray as _ndarray
from numpy import asarray as _asarray

# Builtin modules

class Vector(_ndarray):
  """Subclass 3d array of ndarray for fast math ops and control over dimension"""
  def __new__(cls, x: float, y: float, z: float):
    return _asarray([x, y, z], dtype=float).view(cls)
  
  def __array_finalize__(self, obj):
    """Required method declaration for ndarray subclassing"""
    if obj is None:
      return
  
  @property
  def x(self) -> float:
    return self[0]
  
  @x.setter
  def x(self, value: float):
    self[0] = value
  
  @property
  def y(self) -> float:
    return self[1]
  
  @y.setter
  def y(self, value: float):
    self[1] = value
  
  @property
  def z(self) -> float:
    return self[2]
  
  @z.setter
  def z(self, value: float):
    self[2] = value

__all__ = [
  "Vector"
]
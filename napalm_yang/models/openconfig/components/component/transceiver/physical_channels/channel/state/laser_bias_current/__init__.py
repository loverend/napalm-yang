
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class laser_bias_current(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/transceiver/physical-channels/channel/state/laser-bias-current. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The current applied by the system to the transmit laser to
achieve the output power. The current is expressed in mA
with up to two decimal precision. Values include the
instantaneous, average, minimum, and maximum statistics.
If avg/min/max statistics are not supported, the target is
expected to just supply the instant value
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__instant','__avg','__min_','__max_',)

  _yang_name = 'laser-bias-current'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__avg = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)
    self.__instant = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)
    self.__max_ = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)
    self.__min_ = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'components', u'component', u'transceiver', u'physical-channels', u'channel', u'state', u'laser-bias-current']

  def _get_instant(self):
    """
    Getter method for instant, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current/instant (decimal64)

    YANG Description: The instantaneous value of the statistic.
    """
    return self.__instant
      
  def _set_instant(self, v, load=False):
    """
    Setter method for instant, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current/instant (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instant is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instant() directly.

    YANG Description: The instantaneous value of the statistic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instant must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)""",
        })

    self.__instant = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instant(self):
    self.__instant = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)


  def _get_avg(self):
    """
    Getter method for avg, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current/avg (decimal64)

    YANG Description: The arithmetic mean value of the statistic over the
sampling period.
    """
    return self.__avg
      
  def _set_avg(self, v, load=False):
    """
    Setter method for avg, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current/avg (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_avg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_avg() directly.

    YANG Description: The arithmetic mean value of the statistic over the
sampling period.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """avg must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)""",
        })

    self.__avg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_avg(self):
    self.__avg = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)


  def _get_min_(self):
    """
    Getter method for min_, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current/min (decimal64)

    YANG Description: The minimum value of the statistic over the sampling
period
    """
    return self.__min_
      
  def _set_min_(self, v, load=False):
    """
    Setter method for min_, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current/min (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_() directly.

    YANG Description: The minimum value of the statistic over the sampling
period
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_ must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)""",
        })

    self.__min_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_(self):
    self.__min_ = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)


  def _get_max_(self):
    """
    Getter method for max_, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current/max (decimal64)

    YANG Description: The maximum value of the statistic over the sampling
period
    """
    return self.__max_
      
  def _set_max_(self, v, load=False):
    """
    Setter method for max_, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current/max (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_() directly.

    YANG Description: The maximum value of the statistic over the sampling
period
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_ must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)""",
        })

    self.__max_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_(self):
    self.__max_ = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', original_module='openconfig-types', yang_type='decimal64', is_config=False)

  instant = __builtin__.property(_get_instant)
  avg = __builtin__.property(_get_avg)
  min_ = __builtin__.property(_get_min_)
  max_ = __builtin__.property(_get_max_)


  _pyangbind_elements = {'instant': instant, 'avg': avg, 'min_': min_, 'max_': max_, }



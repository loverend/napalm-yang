
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/timers/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the timers used for the BGP
neighbor
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__connect_retry','__hold_time','__keepalive_interval','__minimum_advertisement_interval','__negotiated_hold_time',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__keepalive_interval = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="keepalive-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    self.__hold_time = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(90), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    self.__minimum_advertisement_interval = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="minimum-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    self.__connect_retry = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="connect-retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    self.__negotiated_hold_time = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="negotiated-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-neighbor', yang_type='decimal64', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'timers', u'state']

  def _get_connect_retry(self):
    """
    Getter method for connect_retry, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/connect_retry (decimal64)

    YANG Description: Time interval in seconds between attempts to establish a
session with the peer.
    """
    return self.__connect_retry
      
  def _set_connect_retry(self, v, load=False):
    """
    Setter method for connect_retry, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/connect_retry (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connect_retry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connect_retry() directly.

    YANG Description: Time interval in seconds between attempts to establish a
session with the peer.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="connect-retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connect_retry must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="connect-retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)""",
        })

    self.__connect_retry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connect_retry(self):
    self.__connect_retry = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="connect-retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)


  def _get_hold_time(self):
    """
    Getter method for hold_time, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/hold_time (decimal64)

    YANG Description: Time interval in seconds that a BGP session will be
considered active in the absence of keepalive or other
messages from the peer.  The hold-time is typically
set to 3x the keepalive-interval.
    """
    return self.__hold_time
      
  def _set_hold_time(self, v, load=False):
    """
    Setter method for hold_time, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/hold_time (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_time() directly.

    YANG Description: Time interval in seconds that a BGP session will be
considered active in the absence of keepalive or other
messages from the peer.  The hold-time is typically
set to 3x the keepalive-interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(90), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_time must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(90), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)""",
        })

    self.__hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_time(self):
    self.__hold_time = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(90), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)


  def _get_keepalive_interval(self):
    """
    Getter method for keepalive_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/keepalive_interval (decimal64)

    YANG Description: Time interval in seconds between transmission of keepalive
messages to the neighbor.  Typically set to 1/3 the
hold-time.
    """
    return self.__keepalive_interval
      
  def _set_keepalive_interval(self, v, load=False):
    """
    Setter method for keepalive_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/keepalive_interval (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_keepalive_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_keepalive_interval() directly.

    YANG Description: Time interval in seconds between transmission of keepalive
messages to the neighbor.  Typically set to 1/3 the
hold-time.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="keepalive-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """keepalive_interval must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="keepalive-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)""",
        })

    self.__keepalive_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_keepalive_interval(self):
    self.__keepalive_interval = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="keepalive-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)


  def _get_minimum_advertisement_interval(self):
    """
    Getter method for minimum_advertisement_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/minimum_advertisement_interval (decimal64)

    YANG Description: Minimum time which must elapse between subsequent UPDATE
messages relating to a common set of NLRI being transmitted
to a peer. This timer is referred to as
MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to
reduce the number of UPDATE messages transmitted when a
particular set of NLRI exhibit instability.
    """
    return self.__minimum_advertisement_interval
      
  def _set_minimum_advertisement_interval(self, v, load=False):
    """
    Setter method for minimum_advertisement_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/minimum_advertisement_interval (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_minimum_advertisement_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_minimum_advertisement_interval() directly.

    YANG Description: Minimum time which must elapse between subsequent UPDATE
messages relating to a common set of NLRI being transmitted
to a peer. This timer is referred to as
MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to
reduce the number of UPDATE messages transmitted when a
particular set of NLRI exhibit instability.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="minimum-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """minimum_advertisement_interval must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="minimum-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)""",
        })

    self.__minimum_advertisement_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_minimum_advertisement_interval(self):
    self.__minimum_advertisement_interval = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="minimum-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)


  def _get_negotiated_hold_time(self):
    """
    Getter method for negotiated_hold_time, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/negotiated_hold_time (decimal64)

    YANG Description: The negotiated hold-time for the BGP session
    """
    return self.__negotiated_hold_time
      
  def _set_negotiated_hold_time(self, v, load=False):
    """
    Setter method for negotiated_hold_time, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/negotiated_hold_time (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_negotiated_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_negotiated_hold_time() directly.

    YANG Description: The negotiated hold-time for the BGP session
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="negotiated-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-neighbor', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """negotiated_hold_time must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="negotiated-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-neighbor', yang_type='decimal64', is_config=False)""",
        })

    self.__negotiated_hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_negotiated_hold_time(self):
    self.__negotiated_hold_time = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="negotiated-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-neighbor', yang_type='decimal64', is_config=False)

  connect_retry = __builtin__.property(_get_connect_retry)
  hold_time = __builtin__.property(_get_hold_time)
  keepalive_interval = __builtin__.property(_get_keepalive_interval)
  minimum_advertisement_interval = __builtin__.property(_get_minimum_advertisement_interval)
  negotiated_hold_time = __builtin__.property(_get_negotiated_hold_time)


  _pyangbind_elements = {'connect_retry': connect_retry, 'hold_time': hold_time, 'keepalive_interval': keepalive_interval, 'minimum_advertisement_interval': minimum_advertisement_interval, 'negotiated_hold_time': negotiated_hold_time, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/timers/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the timers used for the BGP
neighbor
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__connect_retry','__hold_time','__keepalive_interval','__minimum_advertisement_interval','__negotiated_hold_time',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__keepalive_interval = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="keepalive-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    self.__hold_time = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(90), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    self.__minimum_advertisement_interval = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="minimum-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    self.__connect_retry = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="connect-retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    self.__negotiated_hold_time = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="negotiated-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-neighbor', yang_type='decimal64', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'timers', u'state']

  def _get_connect_retry(self):
    """
    Getter method for connect_retry, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/connect_retry (decimal64)

    YANG Description: Time interval in seconds between attempts to establish a
session with the peer.
    """
    return self.__connect_retry
      
  def _set_connect_retry(self, v, load=False):
    """
    Setter method for connect_retry, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/connect_retry (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connect_retry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connect_retry() directly.

    YANG Description: Time interval in seconds between attempts to establish a
session with the peer.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="connect-retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connect_retry must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="connect-retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)""",
        })

    self.__connect_retry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connect_retry(self):
    self.__connect_retry = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="connect-retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)


  def _get_hold_time(self):
    """
    Getter method for hold_time, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/hold_time (decimal64)

    YANG Description: Time interval in seconds that a BGP session will be
considered active in the absence of keepalive or other
messages from the peer.  The hold-time is typically
set to 3x the keepalive-interval.
    """
    return self.__hold_time
      
  def _set_hold_time(self, v, load=False):
    """
    Setter method for hold_time, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/hold_time (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_time() directly.

    YANG Description: Time interval in seconds that a BGP session will be
considered active in the absence of keepalive or other
messages from the peer.  The hold-time is typically
set to 3x the keepalive-interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(90), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_time must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(90), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)""",
        })

    self.__hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_time(self):
    self.__hold_time = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(90), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)


  def _get_keepalive_interval(self):
    """
    Getter method for keepalive_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/keepalive_interval (decimal64)

    YANG Description: Time interval in seconds between transmission of keepalive
messages to the neighbor.  Typically set to 1/3 the
hold-time.
    """
    return self.__keepalive_interval
      
  def _set_keepalive_interval(self, v, load=False):
    """
    Setter method for keepalive_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/keepalive_interval (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_keepalive_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_keepalive_interval() directly.

    YANG Description: Time interval in seconds between transmission of keepalive
messages to the neighbor.  Typically set to 1/3 the
hold-time.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="keepalive-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """keepalive_interval must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="keepalive-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)""",
        })

    self.__keepalive_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_keepalive_interval(self):
    self.__keepalive_interval = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="keepalive-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)


  def _get_minimum_advertisement_interval(self):
    """
    Getter method for minimum_advertisement_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/minimum_advertisement_interval (decimal64)

    YANG Description: Minimum time which must elapse between subsequent UPDATE
messages relating to a common set of NLRI being transmitted
to a peer. This timer is referred to as
MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to
reduce the number of UPDATE messages transmitted when a
particular set of NLRI exhibit instability.
    """
    return self.__minimum_advertisement_interval
      
  def _set_minimum_advertisement_interval(self, v, load=False):
    """
    Setter method for minimum_advertisement_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/minimum_advertisement_interval (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_minimum_advertisement_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_minimum_advertisement_interval() directly.

    YANG Description: Minimum time which must elapse between subsequent UPDATE
messages relating to a common set of NLRI being transmitted
to a peer. This timer is referred to as
MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to
reduce the number of UPDATE messages transmitted when a
particular set of NLRI exhibit instability.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="minimum-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """minimum_advertisement_interval must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="minimum-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)""",
        })

    self.__minimum_advertisement_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_minimum_advertisement_interval(self):
    self.__minimum_advertisement_interval = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), default=Decimal(30), is_leaf=True, yang_name="minimum-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='decimal64', is_config=False)


  def _get_negotiated_hold_time(self):
    """
    Getter method for negotiated_hold_time, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/negotiated_hold_time (decimal64)

    YANG Description: The negotiated hold-time for the BGP session
    """
    return self.__negotiated_hold_time
      
  def _set_negotiated_hold_time(self, v, load=False):
    """
    Setter method for negotiated_hold_time, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/timers/state/negotiated_hold_time (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_negotiated_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_negotiated_hold_time() directly.

    YANG Description: The negotiated hold-time for the BGP session
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="negotiated-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-neighbor', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """negotiated_hold_time must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="negotiated-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-neighbor', yang_type='decimal64', is_config=False)""",
        })

    self.__negotiated_hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_negotiated_hold_time(self):
    self.__negotiated_hold_time = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="negotiated-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-neighbor', yang_type='decimal64', is_config=False)

  connect_retry = __builtin__.property(_get_connect_retry)
  hold_time = __builtin__.property(_get_hold_time)
  keepalive_interval = __builtin__.property(_get_keepalive_interval)
  minimum_advertisement_interval = __builtin__.property(_get_minimum_advertisement_interval)
  negotiated_hold_time = __builtin__.property(_get_negotiated_hold_time)


  _pyangbind_elements = {'connect_retry': connect_retry, 'hold_time': hold_time, 'keepalive_interval': keepalive_interval, 'minimum_advertisement_interval': minimum_advertisement_interval, 'negotiated_hold_time': negotiated_hold_time, }



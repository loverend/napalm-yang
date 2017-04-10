
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/timers/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS global timers.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lsp_lifetime_interval','__lsp_refresh_interval',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsp_lifetime_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(1200), is_leaf=True, yang_name="lsp-lifetime-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)
    self.__lsp_refresh_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="lsp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'timers', u'state']

  def _get_lsp_lifetime_interval(self):
    """
    Getter method for lsp_lifetime_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/state/lsp_lifetime_interval (uint16)

    YANG Description: Time interval in seconds that specifies how long an LSP remains in
LSDB without being refreshed.
    """
    return self.__lsp_lifetime_interval
      
  def _set_lsp_lifetime_interval(self, v, load=False):
    """
    Setter method for lsp_lifetime_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/state/lsp_lifetime_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_lifetime_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_lifetime_interval() directly.

    YANG Description: Time interval in seconds that specifies how long an LSP remains in
LSDB without being refreshed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(1200), is_leaf=True, yang_name="lsp-lifetime-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_lifetime_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(1200), is_leaf=True, yang_name="lsp-lifetime-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)""",
        })

    self.__lsp_lifetime_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_lifetime_interval(self):
    self.__lsp_lifetime_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(1200), is_leaf=True, yang_name="lsp-lifetime-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)


  def _get_lsp_refresh_interval(self):
    """
    Getter method for lsp_refresh_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/state/lsp_refresh_interval (uint16)

    YANG Description: Time interval in seconds that specifies how often route topology
that a device originates is transmitted in LSPs.
    """
    return self.__lsp_refresh_interval
      
  def _set_lsp_refresh_interval(self, v, load=False):
    """
    Setter method for lsp_refresh_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/state/lsp_refresh_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_refresh_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_refresh_interval() directly.

    YANG Description: Time interval in seconds that specifies how often route topology
that a device originates is transmitted in LSPs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="lsp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_refresh_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="lsp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)""",
        })

    self.__lsp_refresh_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_refresh_interval(self):
    self.__lsp_refresh_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="lsp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)

  lsp_lifetime_interval = __builtin__.property(_get_lsp_lifetime_interval)
  lsp_refresh_interval = __builtin__.property(_get_lsp_refresh_interval)


  _pyangbind_elements = {'lsp_lifetime_interval': lsp_lifetime_interval, 'lsp_refresh_interval': lsp_refresh_interval, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/timers/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS global timers.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lsp_lifetime_interval','__lsp_refresh_interval',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsp_lifetime_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(1200), is_leaf=True, yang_name="lsp-lifetime-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)
    self.__lsp_refresh_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="lsp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'timers', u'state']

  def _get_lsp_lifetime_interval(self):
    """
    Getter method for lsp_lifetime_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/state/lsp_lifetime_interval (uint16)

    YANG Description: Time interval in seconds that specifies how long an LSP remains in
LSDB without being refreshed.
    """
    return self.__lsp_lifetime_interval
      
  def _set_lsp_lifetime_interval(self, v, load=False):
    """
    Setter method for lsp_lifetime_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/state/lsp_lifetime_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_lifetime_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_lifetime_interval() directly.

    YANG Description: Time interval in seconds that specifies how long an LSP remains in
LSDB without being refreshed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(1200), is_leaf=True, yang_name="lsp-lifetime-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_lifetime_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(1200), is_leaf=True, yang_name="lsp-lifetime-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)""",
        })

    self.__lsp_lifetime_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_lifetime_interval(self):
    self.__lsp_lifetime_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(1200), is_leaf=True, yang_name="lsp-lifetime-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)


  def _get_lsp_refresh_interval(self):
    """
    Getter method for lsp_refresh_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/state/lsp_refresh_interval (uint16)

    YANG Description: Time interval in seconds that specifies how often route topology
that a device originates is transmitted in LSPs.
    """
    return self.__lsp_refresh_interval
      
  def _set_lsp_refresh_interval(self, v, load=False):
    """
    Setter method for lsp_refresh_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/state/lsp_refresh_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_refresh_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_refresh_interval() directly.

    YANG Description: Time interval in seconds that specifies how often route topology
that a device originates is transmitted in LSPs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="lsp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_refresh_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="lsp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)""",
        })

    self.__lsp_refresh_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_refresh_interval(self):
    self.__lsp_refresh_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="lsp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-isis', yang_type='uint16', is_config=False)

  lsp_lifetime_interval = __builtin__.property(_get_lsp_lifetime_interval)
  lsp_refresh_interval = __builtin__.property(_get_lsp_refresh_interval)


  _pyangbind_elements = {'lsp_lifetime_interval': lsp_lifetime_interval, 'lsp_refresh_interval': lsp_refresh_interval, }



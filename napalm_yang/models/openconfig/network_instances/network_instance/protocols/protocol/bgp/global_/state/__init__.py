
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the global BGP router
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__as_','__router_id','__total_paths','__total_prefixes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-yang:dotted-quad', is_config=False)
    self.__total_paths = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-inet:as-number', is_config=False)
    self.__total_prefixes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'state']

  def _get_as_(self):
    """
    Getter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/as (oc-inet:as-number)

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    return self.__as_
      
  def _set_as_(self, v, load=False):
    """
    Setter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/as (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_() directly.

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-inet:as-number', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_ must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-inet:as-number', is_config=False)""",
        })

    self.__as_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_(self):
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-inet:as-number', is_config=False)


  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/router_id (oc-yang:dotted-quad)

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/router_id (oc-yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-yang:dotted-quad', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with oc-yang:dotted-quad""",
          'defined-type': "oc-yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-yang:dotted-quad', is_config=False)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-yang:dotted-quad', is_config=False)


  def _get_total_paths(self):
    """
    Getter method for total_paths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/total_paths (uint32)

    YANG Description: Total number of BGP paths within the context
    """
    return self.__total_paths
      
  def _set_total_paths(self, v, load=False):
    """
    Setter method for total_paths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/total_paths (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_paths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_paths() directly.

    YANG Description: Total number of BGP paths within the context
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_paths must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)""",
        })

    self.__total_paths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_paths(self):
    self.__total_paths = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)


  def _get_total_prefixes(self):
    """
    Getter method for total_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/total_prefixes (uint32)

    YANG Description: Total number of BGP prefixes received within the context
    """
    return self.__total_prefixes
      
  def _set_total_prefixes(self, v, load=False):
    """
    Setter method for total_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/total_prefixes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_prefixes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_prefixes() directly.

    YANG Description: Total number of BGP prefixes received within the context
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_prefixes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)""",
        })

    self.__total_prefixes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_prefixes(self):
    self.__total_prefixes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)

  as_ = __builtin__.property(_get_as_)
  router_id = __builtin__.property(_get_router_id)
  total_paths = __builtin__.property(_get_total_paths)
  total_prefixes = __builtin__.property(_get_total_prefixes)


  _pyangbind_elements = {'as_': as_, 'router_id': router_id, 'total_paths': total_paths, 'total_prefixes': total_prefixes, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the global BGP router
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__as_','__router_id','__total_paths','__total_prefixes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-yang:dotted-quad', is_config=False)
    self.__total_paths = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-inet:as-number', is_config=False)
    self.__total_prefixes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'state']

  def _get_as_(self):
    """
    Getter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/as (oc-inet:as-number)

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    return self.__as_
      
  def _set_as_(self, v, load=False):
    """
    Setter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/as (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_() directly.

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-inet:as-number', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_ must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-inet:as-number', is_config=False)""",
        })

    self.__as_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_(self):
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-inet:as-number', is_config=False)


  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/router_id (oc-yang:dotted-quad)

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/router_id (oc-yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-yang:dotted-quad', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with oc-yang:dotted-quad""",
          'defined-type': "oc-yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-yang:dotted-quad', is_config=False)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-global', yang_type='oc-yang:dotted-quad', is_config=False)


  def _get_total_paths(self):
    """
    Getter method for total_paths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/total_paths (uint32)

    YANG Description: Total number of BGP paths within the context
    """
    return self.__total_paths
      
  def _set_total_paths(self, v, load=False):
    """
    Setter method for total_paths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/total_paths (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_paths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_paths() directly.

    YANG Description: Total number of BGP paths within the context
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_paths must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)""",
        })

    self.__total_paths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_paths(self):
    self.__total_paths = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)


  def _get_total_prefixes(self):
    """
    Getter method for total_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/total_prefixes (uint32)

    YANG Description: Total number of BGP prefixes received within the context
    """
    return self.__total_prefixes
      
  def _set_total_prefixes(self, v, load=False):
    """
    Setter method for total_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/state/total_prefixes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_prefixes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_prefixes() directly.

    YANG Description: Total number of BGP prefixes received within the context
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_prefixes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)""",
        })

    self.__total_prefixes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_prefixes(self):
    self.__total_prefixes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-bgp-common', yang_type='uint32', is_config=False)

  as_ = __builtin__.property(_get_as_)
  router_id = __builtin__.property(_get_router_id)
  total_paths = __builtin__.property(_get_total_paths)
  total_prefixes = __builtin__.property(_get_total_prefixes)


  _pyangbind_elements = {'as_': as_, 'router_id': router_id, 'total_paths': total_paths, 'total_prefixes': total_prefixes, }



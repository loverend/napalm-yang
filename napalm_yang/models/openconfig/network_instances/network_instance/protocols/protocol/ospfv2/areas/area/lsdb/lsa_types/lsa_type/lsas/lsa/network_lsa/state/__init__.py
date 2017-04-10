
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/network-lsa/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the network LSA
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__network_mask','__attached_router',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__network_mask = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="network-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='uint8', is_config=False)
    self.__attached_router = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'})), is_leaf=False, yang_name="attached-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='yang:dotted-quad', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'network-lsa', u'state']

  def _get_network_mask(self):
    """
    Getter method for network_mask, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/network_lsa/state/network_mask (uint8)

    YANG Description: The mask of the network described by the Network LSA
represented as a CIDR mask.
    """
    return self.__network_mask
      
  def _set_network_mask(self, v, load=False):
    """
    Setter method for network_mask, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/network_lsa/state/network_mask (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_mask() directly.

    YANG Description: The mask of the network described by the Network LSA
represented as a CIDR mask.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="network-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_mask must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="network-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='uint8', is_config=False)""",
        })

    self.__network_mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_mask(self):
    self.__network_mask = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="network-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='uint8', is_config=False)


  def _get_attached_router(self):
    """
    Getter method for attached_router, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/network_lsa/state/attached_router (yang:dotted-quad)

    YANG Description: A list of the router ID of the routers that are attached to
the network described by the Network LSA
    """
    return self.__attached_router
      
  def _set_attached_router(self, v, load=False):
    """
    Setter method for attached_router, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/network_lsa/state/attached_router (yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attached_router is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attached_router() directly.

    YANG Description: A list of the router ID of the routers that are attached to
the network described by the Network LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'})), is_leaf=False, yang_name="attached-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='yang:dotted-quad', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attached_router must be of a type compatible with yang:dotted-quad""",
          'defined-type': "yang:dotted-quad",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'})), is_leaf=False, yang_name="attached-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='yang:dotted-quad', is_config=False)""",
        })

    self.__attached_router = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attached_router(self):
    self.__attached_router = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'})), is_leaf=False, yang_name="attached-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='yang:dotted-quad', is_config=False)

  network_mask = __builtin__.property(_get_network_mask)
  attached_router = __builtin__.property(_get_attached_router)


  _pyangbind_elements = {'network_mask': network_mask, 'attached_router': attached_router, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/network-lsa/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the network LSA
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__network_mask','__attached_router',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__network_mask = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="network-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='uint8', is_config=False)
    self.__attached_router = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'})), is_leaf=False, yang_name="attached-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='yang:dotted-quad', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'network-lsa', u'state']

  def _get_network_mask(self):
    """
    Getter method for network_mask, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/network_lsa/state/network_mask (uint8)

    YANG Description: The mask of the network described by the Network LSA
represented as a CIDR mask.
    """
    return self.__network_mask
      
  def _set_network_mask(self, v, load=False):
    """
    Setter method for network_mask, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/network_lsa/state/network_mask (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_mask() directly.

    YANG Description: The mask of the network described by the Network LSA
represented as a CIDR mask.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="network-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_mask must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="network-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='uint8', is_config=False)""",
        })

    self.__network_mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_mask(self):
    self.__network_mask = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="network-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='uint8', is_config=False)


  def _get_attached_router(self):
    """
    Getter method for attached_router, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/network_lsa/state/attached_router (yang:dotted-quad)

    YANG Description: A list of the router ID of the routers that are attached to
the network described by the Network LSA
    """
    return self.__attached_router
      
  def _set_attached_router(self, v, load=False):
    """
    Setter method for attached_router, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/network_lsa/state/attached_router (yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attached_router is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attached_router() directly.

    YANG Description: A list of the router ID of the routers that are attached to
the network described by the Network LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'})), is_leaf=False, yang_name="attached-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='yang:dotted-quad', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attached_router must be of a type compatible with yang:dotted-quad""",
          'defined-type': "yang:dotted-quad",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'})), is_leaf=False, yang_name="attached-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='yang:dotted-quad', is_config=False)""",
        })

    self.__attached_router = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attached_router(self):
    self.__attached_router = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'})), is_leaf=False, yang_name="attached-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='yang:dotted-quad', is_config=False)

  network_mask = __builtin__.property(_get_network_mask)
  attached_router = __builtin__.property(_get_attached_router)


  _pyangbind_elements = {'network_mask': network_mask, 'attached_router': attached_router, }



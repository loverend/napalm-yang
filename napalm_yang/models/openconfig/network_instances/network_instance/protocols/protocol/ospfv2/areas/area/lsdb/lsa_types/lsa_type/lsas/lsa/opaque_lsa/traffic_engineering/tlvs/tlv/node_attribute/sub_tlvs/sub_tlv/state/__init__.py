
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/node-attribute/sub-tlvs/sub-tlv/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the Node Attribute TLV sub-TLV
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__type','__local_ipv4_addresses','__local_ipv6_addresses',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_ipv4_addresses = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="local-ipv4-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv4-prefix', is_config=False)
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='union', is_config=False)
    self.__local_ipv6_addresses = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="local-ipv6-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv6-prefix', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'traffic-engineering', u'tlvs', u'tlv', u'node-attribute', u'sub-tlvs', u'sub-tlv', u'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/type (union)

    YANG Description: The type of the sub-TLV of the Node Attribute TLV contained within
the TE LSA. If the local system can interpret the value received the
canonical name of the type is utilised, otherwise the special UNKNOWN
value is used
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/type (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of the sub-TLV of the Node Attribute TLV contained within
the TE LSA. If the local system can interpret the value received the
canonical name of the type is utilised, otherwise the special UNKNOWN
value is used
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='union', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='union', is_config=False)


  def _get_local_ipv4_addresses(self):
    """
    Getter method for local_ipv4_addresses, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/local_ipv4_addresses (inet:ipv4-prefix)

    YANG Description: The local IPv4 addresses of the node expressed in CIDR notation
    """
    return self.__local_ipv4_addresses
      
  def _set_local_ipv4_addresses(self, v, load=False):
    """
    Setter method for local_ipv4_addresses, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/local_ipv4_addresses (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ipv4_addresses is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_ipv4_addresses() directly.

    YANG Description: The local IPv4 addresses of the node expressed in CIDR notation
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="local-ipv4-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv4-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ipv4_addresses must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="local-ipv4-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv4-prefix', is_config=False)""",
        })

    self.__local_ipv4_addresses = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_ipv4_addresses(self):
    self.__local_ipv4_addresses = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="local-ipv4-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv4-prefix', is_config=False)


  def _get_local_ipv6_addresses(self):
    """
    Getter method for local_ipv6_addresses, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/local_ipv6_addresses (inet:ipv6-prefix)

    YANG Description: The local IPv6 addreses of the node
    """
    return self.__local_ipv6_addresses
      
  def _set_local_ipv6_addresses(self, v, load=False):
    """
    Setter method for local_ipv6_addresses, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/local_ipv6_addresses (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ipv6_addresses is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_ipv6_addresses() directly.

    YANG Description: The local IPv6 addreses of the node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="local-ipv6-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv6-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ipv6_addresses must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="local-ipv6-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv6-prefix', is_config=False)""",
        })

    self.__local_ipv6_addresses = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_ipv6_addresses(self):
    self.__local_ipv6_addresses = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="local-ipv6-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv6-prefix', is_config=False)

  type = __builtin__.property(_get_type)
  local_ipv4_addresses = __builtin__.property(_get_local_ipv4_addresses)
  local_ipv6_addresses = __builtin__.property(_get_local_ipv6_addresses)


  _pyangbind_elements = {'type': type, 'local_ipv4_addresses': local_ipv4_addresses, 'local_ipv6_addresses': local_ipv6_addresses, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/node-attribute/sub-tlvs/sub-tlv/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the Node Attribute TLV sub-TLV
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__type','__local_ipv4_addresses','__local_ipv6_addresses',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_ipv4_addresses = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="local-ipv4-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv4-prefix', is_config=False)
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='union', is_config=False)
    self.__local_ipv6_addresses = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="local-ipv6-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv6-prefix', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'traffic-engineering', u'tlvs', u'tlv', u'node-attribute', u'sub-tlvs', u'sub-tlv', u'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/type (union)

    YANG Description: The type of the sub-TLV of the Node Attribute TLV contained within
the TE LSA. If the local system can interpret the value received the
canonical name of the type is utilised, otherwise the special UNKNOWN
value is used
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/type (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of the sub-TLV of the Node Attribute TLV contained within
the TE LSA. If the local system can interpret the value received the
canonical name of the type is utilised, otherwise the special UNKNOWN
value is used
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='union', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV6_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:NODE_IPV4_LOCAL_ADDRESS': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='union', is_config=False)


  def _get_local_ipv4_addresses(self):
    """
    Getter method for local_ipv4_addresses, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/local_ipv4_addresses (inet:ipv4-prefix)

    YANG Description: The local IPv4 addresses of the node expressed in CIDR notation
    """
    return self.__local_ipv4_addresses
      
  def _set_local_ipv4_addresses(self, v, load=False):
    """
    Setter method for local_ipv4_addresses, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/local_ipv4_addresses (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ipv4_addresses is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_ipv4_addresses() directly.

    YANG Description: The local IPv4 addresses of the node expressed in CIDR notation
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="local-ipv4-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv4-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ipv4_addresses must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="local-ipv4-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv4-prefix', is_config=False)""",
        })

    self.__local_ipv4_addresses = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_ipv4_addresses(self):
    self.__local_ipv4_addresses = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="local-ipv4-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv4-prefix', is_config=False)


  def _get_local_ipv6_addresses(self):
    """
    Getter method for local_ipv6_addresses, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/local_ipv6_addresses (inet:ipv6-prefix)

    YANG Description: The local IPv6 addreses of the node
    """
    return self.__local_ipv6_addresses
      
  def _set_local_ipv6_addresses(self, v, load=False):
    """
    Setter method for local_ipv6_addresses, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state/local_ipv6_addresses (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ipv6_addresses is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_ipv6_addresses() directly.

    YANG Description: The local IPv6 addreses of the node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="local-ipv6-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv6-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ipv6_addresses must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="local-ipv6-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv6-prefix', is_config=False)""",
        })

    self.__local_ipv6_addresses = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_ipv6_addresses(self):
    self.__local_ipv6_addresses = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="local-ipv6-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-ospfv2-lsdb', yang_type='inet:ipv6-prefix', is_config=False)

  type = __builtin__.property(_get_type)
  local_ipv4_addresses = __builtin__.property(_get_local_ipv4_addresses)
  local_ipv6_addresses = __builtin__.property(_get_local_ipv6_addresses)


  _pyangbind_elements = {'type': type, 'local_ipv4_addresses': local_ipv4_addresses, 'local_ipv6_addresses': local_ipv6_addresses, }



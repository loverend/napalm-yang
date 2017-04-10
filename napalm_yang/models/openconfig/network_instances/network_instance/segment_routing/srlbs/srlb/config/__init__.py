
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/segment-routing/srlbs/srlb/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the SRLB.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_id','__dataplane_type','__mpls_label_block','__ipv6_prefix',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mpls_label_block = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='string', is_config=True)
    self.__dataplane_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='sr-dataplane-type', is_config=True)
    self.__ipv6_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='inet:ipv6-prefix', is_config=True)

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
      return [u'network-instances', u'network-instance', u'segment-routing', u'srlbs', u'srlb', u'config']

  def _get_local_id(self):
    """
    Getter method for local_id, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/local_id (string)

    YANG Description: A unique local identifier used for the Segment Routing Local Block.
The identifier is used when referencing the SRLB within other
contexts.
    """
    return self.__local_id
      
  def _set_local_id(self, v, load=False):
    """
    Setter method for local_id, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/local_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_id() directly.

    YANG Description: A unique local identifier used for the Segment Routing Local Block.
The identifier is used when referencing the SRLB within other
contexts.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='string', is_config=True)""",
        })

    self.__local_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_id(self):
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='string', is_config=True)


  def _get_dataplane_type(self):
    """
    Getter method for dataplane_type, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/dataplane_type (sr-dataplane-type)

    YANG Description: The dataplane that is to be used for the Segment Routing Local Block.
When MPLS is specified, the local block corresponds to a block of MPLS
labels; when IPv6 is specified it corresponds to an IPv6 prefix.
    """
    return self.__dataplane_type
      
  def _set_dataplane_type(self, v, load=False):
    """
    Setter method for dataplane_type, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/dataplane_type (sr-dataplane-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dataplane_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dataplane_type() directly.

    YANG Description: The dataplane that is to be used for the Segment Routing Local Block.
When MPLS is specified, the local block corresponds to a block of MPLS
labels; when IPv6 is specified it corresponds to an IPv6 prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='sr-dataplane-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dataplane_type must be of a type compatible with sr-dataplane-type""",
          'defined-type': "openconfig-network-instance:sr-dataplane-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='sr-dataplane-type', is_config=True)""",
        })

    self.__dataplane_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dataplane_type(self):
    self.__dataplane_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='sr-dataplane-type', is_config=True)


  def _get_mpls_label_block(self):
    """
    Getter method for mpls_label_block, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/mpls_label_block (leafref)

    YANG Description: A reference to the MPLS label block that is used to contain the
SIDs of the SRLB.
    """
    return self.__mpls_label_block
      
  def _set_mpls_label_block(self, v, load=False):
    """
    Setter method for mpls_label_block, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/mpls_label_block (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_label_block is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_label_block() directly.

    YANG Description: A reference to the MPLS label block that is used to contain the
SIDs of the SRLB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_label_block must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)""",
        })

    self.__mpls_label_block = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_label_block(self):
    self.__mpls_label_block = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)


  def _get_ipv6_prefix(self):
    """
    Getter method for ipv6_prefix, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/ipv6_prefix (inet:ipv6-prefix)

    YANG Description: The IPv6 prefix that is used for the SRLB.
    """
    return self.__ipv6_prefix
      
  def _set_ipv6_prefix(self, v, load=False):
    """
    Setter method for ipv6_prefix, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/ipv6_prefix (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_prefix() directly.

    YANG Description: The IPv6 prefix that is used for the SRLB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_prefix must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__ipv6_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_prefix(self):
    self.__ipv6_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='inet:ipv6-prefix', is_config=True)

  local_id = __builtin__.property(_get_local_id, _set_local_id)
  dataplane_type = __builtin__.property(_get_dataplane_type, _set_dataplane_type)
  mpls_label_block = __builtin__.property(_get_mpls_label_block, _set_mpls_label_block)
  ipv6_prefix = __builtin__.property(_get_ipv6_prefix, _set_ipv6_prefix)


  _pyangbind_elements = {'local_id': local_id, 'dataplane_type': dataplane_type, 'mpls_label_block': mpls_label_block, 'ipv6_prefix': ipv6_prefix, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/segment-routing/srlbs/srlb/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the SRLB.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_id','__dataplane_type','__mpls_label_block','__ipv6_prefix',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mpls_label_block = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='string', is_config=True)
    self.__dataplane_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='sr-dataplane-type', is_config=True)
    self.__ipv6_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='inet:ipv6-prefix', is_config=True)

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
      return [u'network-instances', u'network-instance', u'segment-routing', u'srlbs', u'srlb', u'config']

  def _get_local_id(self):
    """
    Getter method for local_id, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/local_id (string)

    YANG Description: A unique local identifier used for the Segment Routing Local Block.
The identifier is used when referencing the SRLB within other
contexts.
    """
    return self.__local_id
      
  def _set_local_id(self, v, load=False):
    """
    Setter method for local_id, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/local_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_id() directly.

    YANG Description: A unique local identifier used for the Segment Routing Local Block.
The identifier is used when referencing the SRLB within other
contexts.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='string', is_config=True)""",
        })

    self.__local_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_id(self):
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='string', is_config=True)


  def _get_dataplane_type(self):
    """
    Getter method for dataplane_type, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/dataplane_type (sr-dataplane-type)

    YANG Description: The dataplane that is to be used for the Segment Routing Local Block.
When MPLS is specified, the local block corresponds to a block of MPLS
labels; when IPv6 is specified it corresponds to an IPv6 prefix.
    """
    return self.__dataplane_type
      
  def _set_dataplane_type(self, v, load=False):
    """
    Setter method for dataplane_type, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/dataplane_type (sr-dataplane-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dataplane_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dataplane_type() directly.

    YANG Description: The dataplane that is to be used for the Segment Routing Local Block.
When MPLS is specified, the local block corresponds to a block of MPLS
labels; when IPv6 is specified it corresponds to an IPv6 prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='sr-dataplane-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dataplane_type must be of a type compatible with sr-dataplane-type""",
          'defined-type': "openconfig-network-instance:sr-dataplane-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='sr-dataplane-type', is_config=True)""",
        })

    self.__dataplane_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dataplane_type(self):
    self.__dataplane_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='sr-dataplane-type', is_config=True)


  def _get_mpls_label_block(self):
    """
    Getter method for mpls_label_block, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/mpls_label_block (leafref)

    YANG Description: A reference to the MPLS label block that is used to contain the
SIDs of the SRLB.
    """
    return self.__mpls_label_block
      
  def _set_mpls_label_block(self, v, load=False):
    """
    Setter method for mpls_label_block, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/mpls_label_block (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_label_block is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_label_block() directly.

    YANG Description: A reference to the MPLS label block that is used to contain the
SIDs of the SRLB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_label_block must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)""",
        })

    self.__mpls_label_block = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_label_block(self):
    self.__mpls_label_block = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)


  def _get_ipv6_prefix(self):
    """
    Getter method for ipv6_prefix, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/ipv6_prefix (inet:ipv6-prefix)

    YANG Description: The IPv6 prefix that is used for the SRLB.
    """
    return self.__ipv6_prefix
      
  def _set_ipv6_prefix(self, v, load=False):
    """
    Setter method for ipv6_prefix, mapped from YANG variable /network_instances/network_instance/segment_routing/srlbs/srlb/config/ipv6_prefix (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_prefix() directly.

    YANG Description: The IPv6 prefix that is used for the SRLB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_prefix must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__ipv6_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_prefix(self):
    self.__ipv6_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='inet:ipv6-prefix', is_config=True)

  local_id = __builtin__.property(_get_local_id, _set_local_id)
  dataplane_type = __builtin__.property(_get_dataplane_type, _set_dataplane_type)
  mpls_label_block = __builtin__.property(_get_mpls_label_block, _set_mpls_label_block)
  ipv6_prefix = __builtin__.property(_get_ipv6_prefix, _set_ipv6_prefix)


  _pyangbind_elements = {'local_id': local_id, 'dataplane_type': dataplane_type, 'mpls_label_block': mpls_label_block, 'ipv6_prefix': ipv6_prefix, }



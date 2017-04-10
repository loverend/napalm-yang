
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/admin-groups/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__exclude_group','__include_all_group','__include_any_group',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__include_all_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-all-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    self.__include_any_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-any-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    self.__exclude_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="exclude-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'p2p-tunnel-attributes', u'p2p-primary-path', u'p2p-primary-path', u'admin-groups', u'config']

  def _get_exclude_group(self):
    """
    Getter method for exclude_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/exclude_group (leafref)

    YANG Description: list of references to named admin-groups to exclude in
path calculation.
    """
    return self.__exclude_group
      
  def _set_exclude_group(self, v, load=False):
    """
    Setter method for exclude_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/exclude_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exclude_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exclude_group() directly.

    YANG Description: list of references to named admin-groups to exclude in
path calculation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="exclude-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exclude_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="exclude-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)""",
        })

    self.__exclude_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exclude_group(self):
    self.__exclude_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="exclude-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)


  def _get_include_all_group(self):
    """
    Getter method for include_all_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/include_all_group (leafref)

    YANG Description: list of references to named admin-groups of which all must
be included
    """
    return self.__include_all_group
      
  def _set_include_all_group(self, v, load=False):
    """
    Setter method for include_all_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/include_all_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_include_all_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_include_all_group() directly.

    YANG Description: list of references to named admin-groups of which all must
be included
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-all-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """include_all_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-all-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)""",
        })

    self.__include_all_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_include_all_group(self):
    self.__include_all_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-all-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)


  def _get_include_any_group(self):
    """
    Getter method for include_any_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/include_any_group (leafref)

    YANG Description: list of references to named admin-groups of which one must
be included
    """
    return self.__include_any_group
      
  def _set_include_any_group(self, v, load=False):
    """
    Setter method for include_any_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/include_any_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_include_any_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_include_any_group() directly.

    YANG Description: list of references to named admin-groups of which one must
be included
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-any-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """include_any_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-any-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)""",
        })

    self.__include_any_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_include_any_group(self):
    self.__include_any_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-any-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)

  exclude_group = __builtin__.property(_get_exclude_group, _set_exclude_group)
  include_all_group = __builtin__.property(_get_include_all_group, _set_include_all_group)
  include_any_group = __builtin__.property(_get_include_any_group, _set_include_any_group)


  _pyangbind_elements = {'exclude_group': exclude_group, 'include_all_group': include_all_group, 'include_any_group': include_any_group, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/admin-groups/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__exclude_group','__include_all_group','__include_any_group',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__include_all_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-all-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    self.__include_any_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-any-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    self.__exclude_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="exclude-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'p2p-tunnel-attributes', u'p2p-primary-path', u'p2p-primary-path', u'admin-groups', u'config']

  def _get_exclude_group(self):
    """
    Getter method for exclude_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/exclude_group (leafref)

    YANG Description: list of references to named admin-groups to exclude in
path calculation.
    """
    return self.__exclude_group
      
  def _set_exclude_group(self, v, load=False):
    """
    Setter method for exclude_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/exclude_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exclude_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exclude_group() directly.

    YANG Description: list of references to named admin-groups to exclude in
path calculation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="exclude-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exclude_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="exclude-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)""",
        })

    self.__exclude_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exclude_group(self):
    self.__exclude_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="exclude-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)


  def _get_include_all_group(self):
    """
    Getter method for include_all_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/include_all_group (leafref)

    YANG Description: list of references to named admin-groups of which all must
be included
    """
    return self.__include_all_group
      
  def _set_include_all_group(self, v, load=False):
    """
    Setter method for include_all_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/include_all_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_include_all_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_include_all_group() directly.

    YANG Description: list of references to named admin-groups of which all must
be included
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-all-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """include_all_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-all-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)""",
        })

    self.__include_all_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_include_all_group(self):
    self.__include_all_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-all-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)


  def _get_include_any_group(self):
    """
    Getter method for include_any_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/include_any_group (leafref)

    YANG Description: list of references to named admin-groups of which one must
be included
    """
    return self.__include_any_group
      
  def _set_include_any_group(self, v, load=False):
    """
    Setter method for include_any_group, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/admin_groups/config/include_any_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_include_any_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_include_any_group() directly.

    YANG Description: list of references to named admin-groups of which one must
be included
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-any-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """include_any_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-any-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)""",
        })

    self.__include_any_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_include_any_group(self):
    self.__include_any_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="include-any-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-mpls-te', yang_type='leafref', is_config=True)

  exclude_group = __builtin__.property(_get_exclude_group, _set_exclude_group)
  include_all_group = __builtin__.property(_get_include_all_group, _set_include_all_group)
  include_any_group = __builtin__.property(_get_include_any_group, _set_include_any_group)


  _pyangbind_elements = {'exclude_group': exclude_group, 'include_all_group': include_all_group, 'include_any_group': include_any_group, }



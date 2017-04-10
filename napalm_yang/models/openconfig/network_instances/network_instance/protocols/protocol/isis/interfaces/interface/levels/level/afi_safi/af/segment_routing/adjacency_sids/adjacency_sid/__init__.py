
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import config
import state
class adjacency_sid(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/afi-safi/af/segment-routing/adjacency-sids/adjacency-sid. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__sid_id','__neighbor','__config','__state',)

  _yang_name = 'adjacency-sid'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sid_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="sid-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)
    self.__neighbor = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'levels', u'level', u'afi-safi', u'af', u'segment-routing', u'adjacency-sids', u'adjacency-sid']

  def _get_sid_id(self):
    """
    Getter method for sid_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/sid_id (leafref)

    YANG Description: Reference to the segment identifier to be used by the local
system.
    """
    return self.__sid_id
      
  def _set_sid_id(self, v, load=False):
    """
    Setter method for sid_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/sid_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_id() directly.

    YANG Description: Reference to the segment identifier to be used by the local
system.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="sid-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="sid-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)""",
        })

    self.__sid_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_id(self):
    self.__sid_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="sid-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)


  def _get_neighbor(self):
    """
    Getter method for neighbor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/neighbor (leafref)

    YANG Description: Reference to the neighbor with which the Adjacency SID is
associated.
    """
    return self.__neighbor
      
  def _set_neighbor(self, v, load=False):
    """
    Setter method for neighbor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/neighbor (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor() directly.

    YANG Description: Reference to the neighbor with which the Adjacency SID is
associated.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)""",
        })

    self.__neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor(self):
    self.__neighbor = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/config (container)

    YANG Description: Configuraton parameters relating to the AdjSID.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuraton parameters relating to the AdjSID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/state (container)

    YANG Description: Operational state parameters relating to the AdjSID.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters relating to the AdjSID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)

  sid_id = __builtin__.property(_get_sid_id, _set_sid_id)
  neighbor = __builtin__.property(_get_neighbor, _set_neighbor)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = {'sid_id': sid_id, 'neighbor': neighbor, 'config': config, 'state': state, }


import config
import state
class adjacency_sid(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/afi-safi/af/segment-routing/adjacency-sids/adjacency-sid. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__sid_id','__neighbor','__config','__state',)

  _yang_name = 'adjacency-sid'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sid_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="sid-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)
    self.__neighbor = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'levels', u'level', u'afi-safi', u'af', u'segment-routing', u'adjacency-sids', u'adjacency-sid']

  def _get_sid_id(self):
    """
    Getter method for sid_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/sid_id (leafref)

    YANG Description: Reference to the segment identifier to be used by the local
system.
    """
    return self.__sid_id
      
  def _set_sid_id(self, v, load=False):
    """
    Setter method for sid_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/sid_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_id() directly.

    YANG Description: Reference to the segment identifier to be used by the local
system.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="sid-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="sid-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)""",
        })

    self.__sid_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_id(self):
    self.__sid_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="sid-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)


  def _get_neighbor(self):
    """
    Getter method for neighbor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/neighbor (leafref)

    YANG Description: Reference to the neighbor with which the Adjacency SID is
associated.
    """
    return self.__neighbor
      
  def _set_neighbor(self, v, load=False):
    """
    Setter method for neighbor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/neighbor (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor() directly.

    YANG Description: Reference to the neighbor with which the Adjacency SID is
associated.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)""",
        })

    self.__neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor(self):
    self.__neighbor = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/config (container)

    YANG Description: Configuraton parameters relating to the AdjSID.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuraton parameters relating to the AdjSID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/state (container)

    YANG Description: Operational state parameters relating to the AdjSID.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters relating to the AdjSID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-segment-routing', yang_type='container', is_config=True)

  sid_id = __builtin__.property(_get_sid_id, _set_sid_id)
  neighbor = __builtin__.property(_get_neighbor, _set_neighbor)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = {'sid_id': sid_id, 'neighbor': neighbor, 'config': config, 'state': state, }



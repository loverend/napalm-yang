
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class openconfig_platform_types(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform-types - based on the path /openconfig-platform-types. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.
  """
  _pyangbind_elements = {}

  

class openconfig_if_ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-if-ip - based on the path /openconfig-if-ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Model for managing IP interfaces.

This model reuses most of the IETF YANG model for IP management
described by RFC 7277.  The primary differences are in the
structure of configuration and state data.
  """
  _pyangbind_elements = {}

  

import interfaces
class openconfig_interfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /openconfig-interfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Model for managing network interfaces and subinterfaces.  This
module also defines convenience types / groupings for other
models to create references to interfaces:

 base-interface-ref (type) -  reference to a base interface
 interface-ref (grouping) -  container for reference to a
   interface + subinterface
 interface-ref-state (grouping) - container for read-only
   (opstate) reference to interface + subinterface

This model reuses data items defined in the IETF YANG model for
interfaces described by RFC 7223 with an alternate structure
(particularly for operational state data) and and with
additional configuration items.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interfaces',)

  _yang_name = 'openconfig-interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='container', is_config=True)

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
      return []

  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /interfaces (container)

    YANG Description: Top level container for interfaces, including configuration
and state data.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Top level container for interfaces, including configuration
and state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='container', is_config=True)

  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = {'interfaces': interfaces, }


class openconfig_if_ip_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-if-ip-ext - based on the path /openconfig-if-ip-ext. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module adds extensions to the base IP configuration and
operational state model to support additional use cases.
  """
  _pyangbind_elements = {}

  

class openconfig_if_aggregate(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-if-aggregate - based on the path /openconfig-if-aggregate. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Model for managing aggregated (aka bundle, LAG) interfaces.
  """
  _pyangbind_elements = {}

  

import components
class openconfig_platform(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /openconfig-platform. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines a data model for representing a system
component inventory, which can include hardware or software
elements arranged in an arbitrary structure. The primary
relationship supported by the model is containment, e.g.,
components containing subcomponents.

It is expected that this model reflects every field replacable
unit on the device at a minimum (i.e., additional information
may be supplied about non-replacable components).

Every element in the inventory is termed a 'component' with each
component expected to have a unique name and type, and optionally
a unique system-assigned identifier and FRU number.  The
uniqueness is guaranteed by the system within the device.

Components may have properties defined by the system that are
modeled as a list of key-value pairs. These may or may not be
user-configurable.  The model provides a flag for the system
to optionally indicate which properties are user configurable.

Each component also has a list of 'subcomponents' which are
references to other components. Appearance in a list of
subcomponents indicates a containment relationship as described
above.  For example, a linecard component may have a list of
references to port components that reside on the linecard.

This schema is generic to allow devices to express their own
platform-specific structure.  It may be augmented by additional
component type-specific schemas that provide a common structure
for well-known component types.  In these cases, the system is
expected to populate the common component schema, and may
optionally also represent the component and its properties in the
generic structure.

The properties for each component may include dynamic values,
e.g., in the 'state' part of the schema.  For example, a CPU
component may report its utilization, temperature, or other
physical properties.  The intent is to capture all platform-
specific physical data in one location, including inventory
(presence or absence of a component) and state (physical
attributes or status).
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__components',)

  _yang_name = 'openconfig-platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__components = YANGDynClass(base=components.components, is_container='container', yang_name="components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='container', is_config=True)

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
      return []

  def _get_components(self):
    """
    Getter method for components, mapped from YANG variable /components (container)

    YANG Description: Enclosing container for the components in the system.
    """
    return self.__components
      
  def _set_components(self, v, load=False):
    """
    Setter method for components, mapped from YANG variable /components (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_components is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_components() directly.

    YANG Description: Enclosing container for the components in the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=components.components, is_container='container', yang_name="components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """components must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=components.components, is_container='container', yang_name="components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='container', is_config=True)""",
        })

    self.__components = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_components(self):
    self.__components = YANGDynClass(base=components.components, is_container='container', yang_name="components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='container', is_config=True)

  components = __builtin__.property(_get_components, _set_components)


  _pyangbind_elements = {'components': components, }


import network_instances
class openconfig_network_instance(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /openconfig-network-instance. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: An OpenConfig description of a network-instance. This may be
a Layer 3 forwarding construct such as a virtual routing and
forwarding (VRF) instance, or a Layer 2 instance such as a
virtual switch instance (VSI). Mixed Layer 2 and Layer 3
instances are also supported.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__network_instances',)

  _yang_name = 'openconfig-network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__network_instances = YANGDynClass(base=network_instances.network_instances, is_container='container', yang_name="network-instances", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return []

  def _get_network_instances(self):
    """
    Getter method for network_instances, mapped from YANG variable /network_instances (container)

    YANG Description: The L2, L3, or L2+L3 forwarding instances that are
configured on the local system
    """
    return self.__network_instances
      
  def _set_network_instances(self, v, load=False):
    """
    Setter method for network_instances, mapped from YANG variable /network_instances (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_instances is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_instances() directly.

    YANG Description: The L2, L3, or L2+L3 forwarding instances that are
configured on the local system
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=network_instances.network_instances, is_container='container', yang_name="network-instances", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_instances must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=network_instances.network_instances, is_container='container', yang_name="network-instances", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__network_instances = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_instances(self):
    self.__network_instances = YANGDynClass(base=network_instances.network_instances, is_container='container', yang_name="network-instances", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  network_instances = __builtin__.property(_get_network_instances, _set_network_instances)


  _pyangbind_elements = {'network_instances': network_instances, }


import network_instances
class openconfig_network_instance_l2(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /openconfig-network-instance-l2. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module contains groupings which specifically relate to
Layer 2 network instance configuration and operational state
parameters.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__network_instances',)

  _yang_name = 'openconfig-network-instance-l2'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__network_instances = YANGDynClass(base=network_instances.network_instances, is_container='container', yang_name="network-instances", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return []

  def _get_network_instances(self):
    """
    Getter method for network_instances, mapped from YANG variable /network_instances (container)

    YANG Description: The L2, L3, or L2+L3 forwarding instances that are
configured on the local system
    """
    return self.__network_instances
      
  def _set_network_instances(self, v, load=False):
    """
    Setter method for network_instances, mapped from YANG variable /network_instances (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_instances is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_instances() directly.

    YANG Description: The L2, L3, or L2+L3 forwarding instances that are
configured on the local system
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=network_instances.network_instances, is_container='container', yang_name="network-instances", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_instances must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=network_instances.network_instances, is_container='container', yang_name="network-instances", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__network_instances = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_instances(self):
    self.__network_instances = YANGDynClass(base=network_instances.network_instances, is_container='container', yang_name="network-instances", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  network_instances = __builtin__.property(_get_network_instances, _set_network_instances)


  _pyangbind_elements = {'network_instances': network_instances, }


class openconfig_vlan_types(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-vlan-types - based on the path /openconfig-vlan-types. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines configuration and state variables for VLANs,
in addition to VLAN parameters associated with interfaces
  """
  _pyangbind_elements = {}

  

class openconfig_platform_transceiver(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform-transceiver - based on the path /openconfig-platform-transceiver. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines configuration and operational state data
for transceivers (i.e., pluggable optics).  The module should be
used in conjunction with the platform model where other
physical entity data are represented.

In the platform model, a component of type=TRANSCEIVER is
expected to be a subcomponent of a PORT component.  This
module defines a concrete schema for the associated data for
components with type=TRANSCEIVER.
  """
  _pyangbind_elements = {}

  

import vlans
class openconfig_vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-vlan - based on the path /openconfig-vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines configuration and state variables for VLANs,
in addition to VLAN parameters associated with interfaces
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__vlans',)

  _yang_name = 'openconfig-vlan'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlans = YANGDynClass(base=vlans.vlans, is_container='container', yang_name="vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)

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
      return []

  def _get_vlans(self):
    """
    Getter method for vlans, mapped from YANG variable /vlans (container)

    YANG Description: Container for VLAN configuration and state
variables
    """
    return self.__vlans
      
  def _set_vlans(self, v, load=False):
    """
    Setter method for vlans, mapped from YANG variable /vlans (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlans() directly.

    YANG Description: Container for VLAN configuration and state
variables
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlans.vlans, is_container='container', yang_name="vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlans must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlans.vlans, is_container='container', yang_name="vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlans(self):
    self.__vlans = YANGDynClass(base=vlans.vlans, is_container='container', yang_name="vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)

  vlans = __builtin__.property(_get_vlans, _set_vlans)


  _pyangbind_elements = {'vlans': vlans, }


class openconfig_if_ethernet(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-if-ethernet - based on the path /openconfig-if-ethernet. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Model for managing Ethernet interfaces -- augments the IETF YANG
model for interfaces described by RFC 7223
  """
  _pyangbind_elements = {}

  

class napalm_if_ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module napalm-if-ip - based on the path /napalm-if-ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines some augmentations to the interface's IP model of OC
  """
  _pyangbind_elements = {}

  


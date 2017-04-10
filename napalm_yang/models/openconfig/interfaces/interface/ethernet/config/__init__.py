
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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/ethernet/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for ethernet interfaces
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__mac_address','__auto_negotiate','__duplex_mode','__port_speed','__enable_flow_control','__aggregate_id',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__duplex_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FULL': {}, u'HALF': {}},), is_leaf=True, yang_name="duplex-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='enumeration', is_config=True)
    self.__mac_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='yang:mac-address', is_config=True)
    self.__aggregate_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="aggregate-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', original_module='openconfig-if-aggregate', yang_type='leafref', is_config=True)
    self.__auto_negotiate = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="auto-negotiate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='boolean', is_config=True)
    self.__port_speed = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}},), is_leaf=True, yang_name="port-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='identityref', is_config=True)
    self.__enable_flow_control = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-flow-control", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='boolean', is_config=True)

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
      return [u'interfaces', u'interface', u'ethernet', u'config']

  def _get_mac_address(self):
    """
    Getter method for mac_address, mapped from YANG variable /interfaces/interface/ethernet/config/mac_address (yang:mac-address)

    YANG Description: Assigns a MAC address to the Ethernet interface.  If not
specified, the corresponding operational state leaf is
expected to show the system-assigned MAC address.
    """
    return self.__mac_address
      
  def _set_mac_address(self, v, load=False):
    """
    Setter method for mac_address, mapped from YANG variable /interfaces/interface/ethernet/config/mac_address (yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address() directly.

    YANG Description: Assigns a MAC address to the Ethernet interface.  If not
specified, the corresponding operational state leaf is
expected to show the system-assigned MAC address.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='yang:mac-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address must be of a type compatible with yang:mac-address""",
          'defined-type': "yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='yang:mac-address', is_config=True)""",
        })

    self.__mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address(self):
    self.__mac_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='yang:mac-address', is_config=True)


  def _get_auto_negotiate(self):
    """
    Getter method for auto_negotiate, mapped from YANG variable /interfaces/interface/ethernet/config/auto_negotiate (boolean)

    YANG Description: Set to TRUE to request the interface to auto-negotiate
transmission parameters with its peer interface.  When
set to FALSE, the transmission parameters are specified
manually.
    """
    return self.__auto_negotiate
      
  def _set_auto_negotiate(self, v, load=False):
    """
    Setter method for auto_negotiate, mapped from YANG variable /interfaces/interface/ethernet/config/auto_negotiate (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auto_negotiate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auto_negotiate() directly.

    YANG Description: Set to TRUE to request the interface to auto-negotiate
transmission parameters with its peer interface.  When
set to FALSE, the transmission parameters are specified
manually.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="auto-negotiate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auto_negotiate must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="auto-negotiate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='boolean', is_config=True)""",
        })

    self.__auto_negotiate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auto_negotiate(self):
    self.__auto_negotiate = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="auto-negotiate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='boolean', is_config=True)


  def _get_duplex_mode(self):
    """
    Getter method for duplex_mode, mapped from YANG variable /interfaces/interface/ethernet/config/duplex_mode (enumeration)

    YANG Description: When auto-negotiate is TRUE, this optionally sets the
duplex mode that will be advertised to the peer.  If
unspecified, the interface should negotiate the duplex mode
directly (typically full-duplex).  When auto-negotiate is
FALSE, this sets the duplex mode on the interface directly.
    """
    return self.__duplex_mode
      
  def _set_duplex_mode(self, v, load=False):
    """
    Setter method for duplex_mode, mapped from YANG variable /interfaces/interface/ethernet/config/duplex_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_duplex_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_duplex_mode() directly.

    YANG Description: When auto-negotiate is TRUE, this optionally sets the
duplex mode that will be advertised to the peer.  If
unspecified, the interface should negotiate the duplex mode
directly (typically full-duplex).  When auto-negotiate is
FALSE, this sets the duplex mode on the interface directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FULL': {}, u'HALF': {}},), is_leaf=True, yang_name="duplex-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """duplex_mode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-if-ethernet:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FULL': {}, u'HALF': {}},), is_leaf=True, yang_name="duplex-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='enumeration', is_config=True)""",
        })

    self.__duplex_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_duplex_mode(self):
    self.__duplex_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FULL': {}, u'HALF': {}},), is_leaf=True, yang_name="duplex-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='enumeration', is_config=True)


  def _get_port_speed(self):
    """
    Getter method for port_speed, mapped from YANG variable /interfaces/interface/ethernet/config/port_speed (identityref)

    YANG Description: When auto-negotiate is TRUE, this optionally sets the
port-speed mode that will be advertised to the peer for
negotiation.  If unspecified, it is expected that the
interface will select the highest speed available based on
negotiation.  When auto-negotiate is set to FALSE, sets the
link speed to a fixed value -- supported values are defined
by ETHERNET_SPEED identities
    """
    return self.__port_speed
      
  def _set_port_speed(self, v, load=False):
    """
    Setter method for port_speed, mapped from YANG variable /interfaces/interface/ethernet/config/port_speed (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_speed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_speed() directly.

    YANG Description: When auto-negotiate is TRUE, this optionally sets the
port-speed mode that will be advertised to the peer for
negotiation.  If unspecified, it is expected that the
interface will select the highest speed available based on
negotiation.  When auto-negotiate is set to FALSE, sets the
link speed to a fixed value -- supported values are defined
by ETHERNET_SPEED identities
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}},), is_leaf=True, yang_name="port-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_speed must be of a type compatible with identityref""",
          'defined-type': "openconfig-if-ethernet:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}},), is_leaf=True, yang_name="port-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='identityref', is_config=True)""",
        })

    self.__port_speed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_speed(self):
    self.__port_speed = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}},), is_leaf=True, yang_name="port-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='identityref', is_config=True)


  def _get_enable_flow_control(self):
    """
    Getter method for enable_flow_control, mapped from YANG variable /interfaces/interface/ethernet/config/enable_flow_control (boolean)

    YANG Description: Enable or disable flow control for this interface.
Ethernet flow control is a mechanism by which a receiver
may send PAUSE frames to a sender to stop transmission for
a specified time.

This setting should override auto-negotiated flow control
settings.  If left unspecified, and auto-negotiate is TRUE,
flow control mode is negotiated with the peer interface.
    """
    return self.__enable_flow_control
      
  def _set_enable_flow_control(self, v, load=False):
    """
    Setter method for enable_flow_control, mapped from YANG variable /interfaces/interface/ethernet/config/enable_flow_control (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_flow_control is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_flow_control() directly.

    YANG Description: Enable or disable flow control for this interface.
Ethernet flow control is a mechanism by which a receiver
may send PAUSE frames to a sender to stop transmission for
a specified time.

This setting should override auto-negotiated flow control
settings.  If left unspecified, and auto-negotiate is TRUE,
flow control mode is negotiated with the peer interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-flow-control", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_flow_control must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-flow-control", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='boolean', is_config=True)""",
        })

    self.__enable_flow_control = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_flow_control(self):
    self.__enable_flow_control = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-flow-control", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet', defining_module='openconfig-if-ethernet', original_module='openconfig-if-ethernet', yang_type='boolean', is_config=True)


  def _get_aggregate_id(self):
    """
    Getter method for aggregate_id, mapped from YANG variable /interfaces/interface/ethernet/config/aggregate_id (leafref)

    YANG Description: Specify the logical aggregate interface to which
this interface belongs
    """
    return self.__aggregate_id
      
  def _set_aggregate_id(self, v, load=False):
    """
    Setter method for aggregate_id, mapped from YANG variable /interfaces/interface/ethernet/config/aggregate_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aggregate_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aggregate_id() directly.

    YANG Description: Specify the logical aggregate interface to which
this interface belongs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="aggregate-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', original_module='openconfig-if-aggregate', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aggregate_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="aggregate-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', original_module='openconfig-if-aggregate', yang_type='leafref', is_config=True)""",
        })

    self.__aggregate_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aggregate_id(self):
    self.__aggregate_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="aggregate-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', original_module='openconfig-if-aggregate', yang_type='leafref', is_config=True)

  mac_address = __builtin__.property(_get_mac_address, _set_mac_address)
  auto_negotiate = __builtin__.property(_get_auto_negotiate, _set_auto_negotiate)
  duplex_mode = __builtin__.property(_get_duplex_mode, _set_duplex_mode)
  port_speed = __builtin__.property(_get_port_speed, _set_port_speed)
  enable_flow_control = __builtin__.property(_get_enable_flow_control, _set_enable_flow_control)
  aggregate_id = __builtin__.property(_get_aggregate_id, _set_aggregate_id)


  _pyangbind_elements = {'mac_address': mac_address, 'auto_negotiate': auto_negotiate, 'duplex_mode': duplex_mode, 'port_speed': port_speed, 'enable_flow_control': enable_flow_control, 'aggregate_id': aggregate_id, }



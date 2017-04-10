
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rule
class rules(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The criteria that should be matched for a packet to be
forwarded according to the policy action.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__rule',)

  _yang_name = 'rules'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__rule = YANGDynClass(base=YANGListType("sequence_id",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence-id', extensions=None), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-pf-forwarding-policies', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'policy-forwarding', u'policies', u'policy', u'rules']

  def _get_rule(self):
    """
    Getter method for rule, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule (list)

    YANG Description: A match rule for the policy. In the case that multiple
criteria are specified within a single 
    """
    return self.__rule
      
  def _set_rule(self, v, load=False):
    """
    Setter method for rule, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rule is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rule() directly.

    YANG Description: A match rule for the policy. In the case that multiple
criteria are specified within a single 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sequence_id",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence-id', extensions=None), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-pf-forwarding-policies', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rule must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sequence_id",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence-id', extensions=None), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-pf-forwarding-policies', yang_type='list', is_config=True)""",
        })

    self.__rule = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rule(self):
    self.__rule = YANGDynClass(base=YANGListType("sequence_id",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence-id', extensions=None), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-pf-forwarding-policies', yang_type='list', is_config=True)

  rule = __builtin__.property(_get_rule, _set_rule)


  _pyangbind_elements = {'rule': rule, }


import rule
class rules(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The criteria that should be matched for a packet to be
forwarded according to the policy action.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__rule',)

  _yang_name = 'rules'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__rule = YANGDynClass(base=YANGListType("sequence_id",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence-id', extensions=None), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-pf-forwarding-policies', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'policy-forwarding', u'policies', u'policy', u'rules']

  def _get_rule(self):
    """
    Getter method for rule, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule (list)

    YANG Description: A match rule for the policy. In the case that multiple
criteria are specified within a single 
    """
    return self.__rule
      
  def _set_rule(self, v, load=False):
    """
    Setter method for rule, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rule is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rule() directly.

    YANG Description: A match rule for the policy. In the case that multiple
criteria are specified within a single 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sequence_id",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence-id', extensions=None), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-pf-forwarding-policies', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rule must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sequence_id",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence-id', extensions=None), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-pf-forwarding-policies', yang_type='list', is_config=True)""",
        })

    self.__rule = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rule(self):
    self.__rule = YANGDynClass(base=YANGListType("sequence_id",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence-id', extensions=None), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', original_module='openconfig-pf-forwarding-policies', yang_type='list', is_config=True)

  rule = __builtin__.property(_get_rule, _set_rule)


  _pyangbind_elements = {'rule': rule, }



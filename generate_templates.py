from collections import defaultdict

import os


import napalm_yang

import yaml

models = [
    napalm_yang.models.openconfig_network_instance,
    #  napalm_yang.models.openconfig_interfaces,
    #  napalm_yang.models.openconfig_platform,
    #  napalm_yang.models.openconfig_vlan,
]

profile = "dummy"


def nested_dd():
    return defaultdict(nested_dd)


def process(model, r):
    if model._yang_type in ("container", ):
        ctr = model
    elif model._yang_type in ("list", None):
        ctr = model._contained_class()
    else:
        r[model._yang_name] = {"_process": "not_implemented"}
        return

    for k, v in ctr:
        rr = r[model._yang_name]
        rr["_process"] = "not_implemented"
        process_module(v, model._original_module, rr)


def process_module(model, module, r):
    if model._original_module != module:
        r = result[os.path.join(model._original_module,
                                "{}.yaml".format(model._yang_name))]

    process(model, r)


def ddict2dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = ddict2dict(v)
    return dict(d)


def main():
    global result
    result = nested_dd()

    for model in models:
        m = model()
        for _, v in m:
            process_module(v, None, result)

    for module, model in result.items():
        module, filename = module.split("/")
        for action in ["parsers", "translators"]:
            directory = os.path.join("napalm_yang", "mappings", "dummy", action, module)

            if not os.path.exists(directory):
                os.makedirs(directory)

            model = ddict2dict(model)
            metadata = "---\nmetadata:\n    processor: unset\n\n"
            with open(os.path.join(directory, filename), 'w+') as f:
                f.write(metadata + yaml.safe_dump(model, indent=4, default_flow_style=False))


if __name__ == "__main__":
    main()

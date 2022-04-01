#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
samconfigをparseする
"""


import shlex

import boto3
import toml


def read_samconfig(samconfig: str, profile) -> dict:
    """Read parameters from samconfig.toml."""
    sam = toml.load(open(samconfig))
    return sam[profile]["deploy"]["parameters"]


def decode_parameter_overrides(s: str) -> dict:
    return dict(token.split("=") for token in shlex.split(s))


def parse_samconfig(
    samconfig: str = "./samconfig.toml", profile: str = "default"
) -> dict:
    # samconfig.tomlを読む
    sam = read_samconfig(samconfig, profile)

    # samからparameter_overridesを抽出する
    if "parameter_overrides" not in sam:
        po = {}
    else:
        po = decode_parameter_overrides(sam.pop("parameter_overrides"))

    # stackからoutputを得てdictにする
    CFn = boto3.client("cloudformation", region_name=sam["region"])
    res = CFn.describe_stacks(StackName=sam["stack_name"])
    output = {k["OutputKey"]: k["OutputValue"] for k in res["Stacks"][0]["Outputs"]}

    return {"s": sam, "p": po, "o": output}


if __name__ == "__main__":
    # samconfig.tomlを読む
    data = parse_samconfig()
    print(data)

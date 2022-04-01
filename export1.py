#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
毎回stackにアクセスするのが面倒なので
必要な情報を.export.ymlとして書き出す
"""


from ruamel.yaml import YAML

from pylib import samconfig as sc


def main():
    """main"""
    # samconfig.tomlを読む
    data = sc.parse_samconfig()
    # print(data)

    # 適当にフォーマットしてYAMLで出力
    with open(".export.yml", "w") as f:
        yaml = YAML()
        yaml.dump(data, f)

    # shellscriptで処理できるような出力
    s = f"""
StateMachineArn={data["o"]["FullNameStateMachineArn"]}
ActivityArn={data["o"]["NameActivityArn"]}
"""
    with open(".export.sh", "w") as f:
        f.write(s)


if __name__ == "__main__":
    main()

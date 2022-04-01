#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
import json

import boto3
from ruamel.yaml import YAML


def main():
    """main"""
    # ./.export.ymlを読む
    with open("./.export.yml") as f:
        yaml = YAML()
        conf = yaml.load(f)

    SF = boto3.client("stepfunctions", region_name=conf["s"]["region"])

    res = SF.get_activity_task(activityArn=conf["o"]["NameActivityArn"])
    # TODO: タイムアウトしたら例外来るので、loopするとか工夫する。

    # print(res)
    taskToken = res["taskToken"]

    # 前段からもらったJSONを入力として結果を作る
    i1 = json.loads(res.get("input", "{}"))
    surname = i1.get("surname", None)
    givenname = i1.get("givenname", None)
    # givenname = None

    # 結果をステートマシンに返す
    if (surname is not None) and (givenname is not None):
        # 正常
        res = SF.send_task_success(
            taskToken=taskToken,
            output=json.dumps({"fullname": f"{givenname} {surname}"}),
        )
    else:
        # 異常発生
        res = SF.send_task_failure(
            taskToken=taskToken, error="ERRORCODE", cause="wrong input"
        )  # ERRORCODEは好きなこと書いていいらしい。

    print(res)


if __name__ == "__main__":
    main()

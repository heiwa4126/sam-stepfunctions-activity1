#!/bin/sh -ue
# ステートマシンの状態を得る

. ./.export.sh
. ./tmp_name1.sh
aws stepfunctions describe-execution --execution-arn "$executionArn"

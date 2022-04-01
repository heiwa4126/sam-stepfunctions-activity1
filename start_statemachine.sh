#!/bin/sh -ue
# ステートマシンを実行するサンプル。
# デプロイ後、準備として
# pip3 install -U -r requirements.txt
# ./export1.py
# で、./export.{yaml,sh} ファイルを生成の後
# このスクリプトを実行すること

. ./.export.sh
NAME1=$(date -u +%Y-%m-%d-%H-%M-%S.%N)

RES=$(
  aws stepfunctions start-execution \
    --state-machine-arn "$StateMachineArn" \
    --name "$NAME1" \
    --input "{\"surname\":\"Smithee\",\"givenname\":\"Alan\"}"
)
echo "$RES"

executionArn=$(echo "$RES" | jq -r .executionArn)

echo "executionArn=${executionArn}
NAME1=$NAME1" >tmp_name1.sh

# sam-stepfunctions-activity1

AWS Step Functionsのactivityのテスト

## 参考

- [Step Function Activity with Python | by Yuvaraj Ravikumar | Medium](https://medium.com/@yuvarajmailme/step-function-activity-with-python-c007178037af)


# 概要

前段から
```JSON
{"surname":"Smithee", "givenname":"Alan"}
```

みたいのを受けて

```JSON
{"fullname":"Alan Smithee"}
```

のようなのを返すworkerをPythonで作ってみた。


# ステートマシンのデプロイ

SAMなので

```sh
sam build
sam deploy --guided # --guidedは2回め以降は不要
```

# 準備

デプロイ成功後、準備として
```sh
pip3 install -U -r requirements.txt
./export1.py
```
を1回実行。


# 実行

```sh
./start_statemachine.sh
./get_statemachine_status.sh
./worker1.py
./get_statemachine_status.sh
```

workerを先に実行するとどうなるかも試して。
```sh
./worker1.py &
./start_statemachine.sh
./get_statemachine_status.sh
```

こういうのも試して。
```sh
./start_statemachine.sh &
./start_statemachine.sh &
./start_statemachine.sh
./worker1.py &
./worker1.py &
./worker1.py
```


# 削除

```sh
sam delete --no-prompts
```


# メモ

## 「実行」を消す方法

ステートマシンのコンソール見てると、「実行」がどんどん溜まっていくのが見える。
「実行」を消す方法はないらしい。

[aws step functions - How to Delete State Machine Executions? - Stack Overflow](https://stackoverflow.com/questions/59168923/how-to-delete-state-machine-executions)

APIにDeleteExecutionがない。

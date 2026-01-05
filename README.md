# 経過時間表示パッケージ
![test](https://github.com/jumakonana/rbsys25_as2/actions/workflows/test.yml/badge.svg)

[分]：[秒]単位で経過時間を計測するパッケージ

## 各ノード, ファイルの機能
### Count.msg
以下2つのノードが利用するメッセージファイル

2つのuint8型のデータを扱う
minuteを分, secondが秒の値となる
```
uint8 minute
uint8 second
```

### pub_etime
Count.msgのデータを流すパブリッシャを持つ

secondが60になった際, 値を0に変えminuteの値を増加させる

### sub_etime
Count.msgのデータを受け取るサブスクライバを持つ

受け取ったデータをminute, secondの順で表示する

### etime.launch.py
pub_etimeとsub_etimeを立ち上げるローンチファイル

### パッケージの構造

```
rbsys25_as2/
├── LICENSE
├── README.md
├── launch
│   └── etime.launch.py
├── package.xml
├── rbsys25_as2
│   ├── __init__.py
│   ├── pub_etime.py
│   └── sub_etime.py
├── resource
│   └── rbsys25_as2
├── setup.cfg
├── setup.py
└── test
    ├── test.bash
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```

## 動作例
### pub_etime
標準出力には何も出ない
```
$ ros2 run rbsys25_as2 pub_etime 

```

### sub_etime
sub_etimeを立ち上げた後にpub_etimeを立ち上げた際の動作

以下は1分2秒以上経過した時点の出力である
```
$ ros2 run rbsys25_as2 sub_etime
[INFO] [1767613647.196071738] [sub_etime]:  0 : 0
[INFO] [1767613648.179546596] [sub_etime]:  0 : 1
[INFO] [1767613649.192466834] [sub_etime]:  0 : 2
(中略)
[INFO] [1767613865.335443376] [sub_etime]:  0 : 57
[INFO] [1767613866.336463348] [sub_etime]:  0 : 58
[INFO] [1767613867.337530843] [sub_etime]:  0 : 59
[INFO] [1767613868.336329557] [sub_etime]:  1 : 0
[INFO] [1767613869.332994804] [sub_etime]:  1 : 1
[INFO] [1767613870.333520614] [sub_etime]:  1 : 2
(以下略)
```

### etime.launch.py
```
$ ros2 launch rbsys25_as2 etime.launch.py
[INFO] [launch]: (中略)
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [pub_etime-1]: process started with pid [11109]
[INFO] [sub_etime-2]: process started with pid [11111]
[sub_etime-2] [INFO] [1767615544.696885071] [sub_etime]:  0 : 0
[sub_etime-2] [INFO] [1767615545.673830359] [sub_etime]:  0 : 1
[sub_etime-2] [INFO] [1767615546.688745423] [sub_etime]:  0 : 2
[sub_etime-2] [INFO] [1767615547.673776452] [sub_etime]:  0 : 3
[sub_etime-2] [INFO] [1767615548.695054454] [sub_etime]:  0 : 4
[sub_etime-2] [INFO] [1767615549.672213309] [sub_etime]:  0 : 5
(以下略)
```


## 必要なソフト
- Python
- ROS 2

## テスト環境
- Ubuntu 22.04 LTS
### GitHub Actionsでのテスト
- Ubuntu 22.04 LTS

このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.

© 2026 Kyohei Tanaka

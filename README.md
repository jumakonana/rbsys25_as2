# 経過時間表示パッケージ
![test](https://github.com/jumakonana/rbsys25_as2/actions/workflows/test.yml/badge.svg)

ROS2で[分]：[秒]の形式で経過時間を計測・表示するパッケージ

パブリッシャとサブスクライバによる通信を行い, 独自メッセージ型`Count`を使用する

## 各ノード, ファイルの機能

### pub_etime
Count型のメッセージをパブリッシュするノード

secondを1秒毎に1増加させ, 60になった際値を0に変えminuteの値を1増加させる

### sub_etime
Count型のメッセージをサブスクライブするノード

受け取ったデータをminute, secondの順で表示する

### etime.launch.py
`pub_etime`と`sub_etime`を立ち上げるローンチファイル


### Count.msg

本パッケージで使用する独自メッセージ型`Count`を定義するファイル(他のリポジトリに位置)

以下のデータを生成する
```
minute　(分)
second  (秒)　
```

`Count.msg`の詳細やインストールは以下のリポジトリを参照

- count_msgs [https://github.com/jumakonana/count_msgs.git]


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
- ノードの立ち上げやファイルの実行の前に, `count_msgs`の設置と`colcon build`及び`source`の実行が必要である
### pub_etime
```
$ ros2 run rbsys25_as2 pub_etime 
<標準出力無し>
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

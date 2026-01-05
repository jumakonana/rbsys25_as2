# 経過時間表示パッケージ
![test](https://github.com/jumakonana/rbsys25_as2/actions/workflows/test.yml/badge.svg)

[分]：[秒]単位で経過時間を計測するパッケージ

## 各ノード, ファイルの機能
### Count.msg
以下2つのノードが利用するメッセージファイル

2つのuint8型のデータを扱う
```
uint8 minute
uint8 second
```

### pub_etime
Count.msgのデータを流すパブリッシャを持つ

secondが60になった際, 値を0に変えminuteの値を増加させる

### sub_etime
Count.msgのデータを受け取るサブスクライバを持つ

受け取ったデータを表示する

### etime.launch.py
pub_etimeとsub_etimeを立ち上げるローンチファイル

### パッケージの構造

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


## 動作
### pub_etime

```
$ ros2 run rbsys25_as2 pub_etime 

```

### sub_etime
```
$ ros2 run rbsys25_as2 sub_etime

```

### etime.launch.py
```
$ ros2 launch rbsys25_as2 etime.launch.py

```

## テスト環境
- Ubuntu 22.04 LTS
### GitHub Actionsでのテスト
- Ubuntu 22.04 LTS

このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.

© 2026 Kyohei Tanaka

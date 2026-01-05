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

### sub_etime
Count.msgのデータを受け取るサブスクライバを持つ

### etime.launch.py
pub_etimeとsub_etimeを立ち上げるローンチファイル

## 動作
### それぞれ



## テスト環境
- Ubuntu 22.04 LTS
### GitHub Actionsでのテスト
- Ubuntu 22.04 LTS

このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.

© 2026 Kyohei Tanaka

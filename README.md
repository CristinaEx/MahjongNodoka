# MahjongNodoka
A simple test of Mahjong AI

## Class

- MahjongGame
- - 设定游戏基本流程
- - 提供接口操控流程进行状态
- - 拥有四个MahjongPlayer对象作为玩家或AI
- - 拥有MahjongTable对象控制桌面活动

- MahjongGameRunner
- - 拥有MmahjongGame对象控制游戏进程
- - 自定义游戏进程控制

- MahjongPlayer
- - 提供操作接口

- MahjongAI(MahjongPlayer)
- - AI模型的搭建，拥有控制部分游戏进程的权限

- MahjongAIPreTrainer(MahjongPlayer)
- - 预训练AI模型

- MahjongTable
- - 拥有MahjongMountain对象控制牌山（发牌和岭上牌，杠/里宝牌）
- - 拥有MahjongRiver对象控制牌河
- - 控制四个MahjongPlayer的手牌和明牌区
- - 记录立直棒
- - 控制场风和场次
- - 记录当前MahjongPlayer状态（\[振听 立直 摸牌 大明杠摸牌\]）

- MahjongScoreCounter
- - 计算提供的手牌得点（需提供MahjongTable）
- - 计算提供的手牌得分

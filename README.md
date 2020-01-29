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

- MahjongAITrainer(MahjongPlayer)
- - 训练AI模型

- MahjongTable
- - 拥有MahjongMountain对象控制牌山（发牌和岭上牌，杠/里宝牌）
- - 拥有MahjongRiver对象控制牌河
- - 控制四个MahjongPlayer的手牌和明牌区
- - 记录立直棒
- - 控制场风和场次
- - 记录当前MahjongPlayer状态（\[振听 立直 摸牌 大明杠摸牌\]）
- 
- MahjongNet
- - CNN+LSTM->Counter->Judger
- - 拥有三个网络，第一个网络得到其他玩家已拥有的有效牌的数量和类型（牌河时间序列通过LSTM网络，上家的已拥有无效牌数量和类型单独计算），全部牌-自己拥有的牌-其他玩家已拥有的=牌山中可能剩余的牌
- - 第二个网络通过第一个网络和当前手牌情况判定手牌得分，操作后手牌得分增加则为正确操作
- - 第三个网络通过牌河和当前所出的牌来修正得分（操作得分），最终得分=手牌得分+操作得分（加入博弈环境）
  
- MahjongScoreCounter
- - 手牌得分 = Σ达成牌型的点数*达成该牌型的概率
- - 操作得分 = 操作后手牌得分增加量 - 其他玩家在你操作后手牌得分增加量/3
- - 随机替换其中的五张牌（使用牌山中的牌替换），计算得到的牌型点数和概率（完成牌型后，若再进行替换后牌型的加权值小于当前已完成牌型的加权值，则不再继续进行替换）
- - 输出得分和各个牌型分别需要的牌列表+已拥有有效牌列表+各个牌型的单独得分+概率
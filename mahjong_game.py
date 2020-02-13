import random
from MahjongUtils import mahjong_utils

DEBUG = True

class MahjongGame:

    def __init__(self,player_list = [],wind = [1,0,0,0],init_score = 25000,red = True,top = 30000):
        """
        player_list:可以在游戏进行前添加
        wind:默认为东风场([1 0 0 0]),南风场为[0 1 0 0]，以此类推
        init_score:默认点棒为25000
        red:是否存在赤宝牌（3赤/无赤）
        top:一位必要点数，若不足该点数将南入/西入
        默认食断，一番缚，无古役
        """
        self.player_list = player_list
        # 规则制定
        self.wind = wind # 默认东风场开局
        self.banker = [0,0,0,0]
        self.banker[random.randint(0,3)] = 1 # 随机庄家
        self.bao = 1 # 当前宝牌数量
        self.lizhi = [0]*4 # 当前立直条件
        self.lizhi_point = 0 # 剩余立直棒点数
        self.ben = 0 # 第几本场
        self.scores = [init_score] * 4 # 玩家点数
        self.red = red # 是否存在赤宝牌
        self.stack = None # 牌山
        self.cards = None # 每个玩家的手牌区
        self.river = None # 每个玩家的牌河
        self.open_cards = None # 每个玩家的明牌区
        self.msg = None # 当前流程信息

    def run(self):
        while self.__runOne():
            pass
        self.__finish()

    def __runOne(self):
        """
        进行一场游戏，若终止则返回False
        """
        self.__initOne()
        # DEBUG
        if DEBUG:
            return False

    def __initOne(self):
        """
        准备开始一局游戏
        """
        self.__shuffle() # 洗牌
        self.bao = 1 # 当前宝牌数量为1
        self.lizhi = [0]*4 # 当前立直条件清零
        pass

    def __initCard(self):
        """
        初始摸牌
        """
        pass

    def __shuffle(self):
        # 0-8 一万到九万
        # 9-17 一索到九索
        # 18-26 一筒到九筒
        # 27-30 东南西北
        # 31-33 白中发
        # 34-36 五万赤宝，五索赤宝，五筒赤宝
        self.stack = list(range(34)) * 4
        if self.red:
            self.stack[4] = 34
            self.stack[13] = 35
            self.stack[22] = 36
        for i in range(134):
            j = random.randint(0,134-i)
            m = self.stack[j]
            self.stack[j] = self.stack[135-i]
            self.stack[135-i] = m
        if DEBUG:
            mahjong_utils.mahjongCardPrint(self.stack)

    def __finishOne(self):
        """
        每局游戏结束时进行的结算
        """
        pass

    def __finish(self):
        """
        游戏终止处理
        """
        pass

if __name__ == '__main__':
    game = MahjongGame()
    game.run()
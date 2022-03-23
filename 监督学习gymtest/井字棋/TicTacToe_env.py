import gym
import random
import time
import numpy as np
from gym.envs.classic_control import rendering


class TicTacToeEnv(gym.Env):
    def __init__(self):
        self.state = np.zeros([3, 3])
        self.winner = None
        WIDTH, HEIGHT = 300, 300
        self.viewer = rendering.Viewer(WIDTH, HEIGHT)

    def reset(self):
        self.state = np.zeros([3, 3])
        self.winner = None
        self.viewer.geoms.clear()  # 清空画板中需要绘制的元素
        self.viewer.onetime_geoms.clear()

    def step(self, action):
        # 动作的格式：action = {'mark':'circle'/'cross', 'pos':(x,y)}# 产生状态
        x = action['pos'][0]
        y = action['pos'][1]
        if action['mark'] == 'blue':
            self.state[x][y] = 1
        elif action['mark'] == 'red':
            self.state[x][y] = -1
        # 奖励
        done = self.judgeEnd()
        if done:
            if self.winner == 'blue':
                reward = 1
            else:
                reward = -1
        else:
            reward = 0
        # 报告
        info = {}
        return self.state, reward, done, info

    def judgeEnd(self):
        # 检查两对角
        check_diag_1 = self.state[0][0] + self.state[1][1] + self.state[2][2]
        check_diag_2 = self.state[2][0] + self.state[1][1] + self.state[0][2]
        if check_diag_1 == 3 or check_diag_2 == 3:
            self.winner = 'blue'
            return True
        elif check_diag_1 == -3 or check_diag_2 == -3:
            self.winner = 'red'
            return True
        # 检查三行三列
        state_T = self.state.T
        for i in range(3):
            check_row = sum(self.state[i])  # 检查行
            check_col = sum(state_T[i])  # 检查列
            if check_row == 3 or check_col == 3:
                self.winner = 'blue'
                return True
            elif check_row == -3 or check_col == -3:
                self.winner = 'red'
                return True
        # 检查整个棋盘是否还有空位
        empty = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0: empty.append((i, j))
        if empty == []: return True

        return False

    def render(self, mode='human'):
        SIZE = 100
        # 画分隔线
        line1 = rendering.Line((0, 100), (300, 100))
        line2 = rendering.Line((0, 200), (300, 200))
        line3 = rendering.Line((100, 0), (100, 300))
        line4 = rendering.Line((200, 0), (200, 300))
        line1.set_color(0, 0, 0)
        line2.set_color(0, 0, 0)
        line3.set_color(0, 0, 0)
        line4.set_color(0, 0, 0)
        # 将绘画元素添加至画板中
        self.viewer.add_geom(line1)
        self.viewer.add_geom(line2)
        self.viewer.add_geom(line3)
        self.viewer.add_geom(line4)
        # 根据self.state画占位符
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 1:
                    circle = rendering.make_circle(30)  # 画直径为30的圆
                    circle.set_color(135 / 255, 206 / 255, 250 / 255)  # mark = blue
                    move = rendering.Transform(translation=(i * SIZE + 50, j * SIZE + 50))  # 创建平移操作
                    circle.add_attr(move)  # 将平移操作添加至圆的属性中
                    self.viewer.add_geom(circle)  # 将圆添加至画板中
                if self.state[i][j] == -1:
                    circle = rendering.make_circle(30)
                    circle.set_color(255 / 255, 182 / 255, 193 / 255)  # mark = red
                    move = rendering.Transform(translation=(i * SIZE + 50, j * SIZE + 50))
                    circle.add_attr(move)
                    self.viewer.add_geom(circle)

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')
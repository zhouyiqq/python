# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/18 14:29
import gym
#导入MountainCar-v0环境
env = gym.make('MountainCar-v0')
#初始化环境
env.reset()
#循环1000次
for _ in range(10000):
    #绘图
    env.render()
    #进行一个动作
    env.step(env.action_space.sample()) # take a random action
#关闭
env.close()
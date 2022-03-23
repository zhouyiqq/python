import gym
import random
import time


# 步骤3：注册环境
#
# 来到目录：D:\Anaconda\envs\pytorch1.1\Lib\site-packages\gym，打开 __init__.py，添加代码：
#
# register(
#     id="TicTacToeEnv-v0",
#     entry_point="gym.envs.user:TicTacToeEnv",
#     max_episode_steps=20,
# )


# 查看所有已注册的环境
# from gym import envs
# print(envs.registry.all())

def randomAction(env_, mark): # 随机选择未占位的格子动作
    action_space = []
    for i, row in enumerate(env_.state):
        for j, one in enumerate(row):
            if one == 0: action_space.append((i,j))
    action_pos = random.choice(action_space)
    action = {'mark':mark, 'pos':action_pos}
    return action

def randomFirst():
    if random.random() > 0.5: # 随机先后手
        first_, second_ = 'blue', 'red'
    else:
        first_, second_ = 'red', 'blue'
    return first_, second_

env = gym.make('TicTacToeEnv-v0')
env.reset() # 在第一次step前要先重置环境 不然会报错
first, second = randomFirst()
while True:
    # 先手行动
    action = randomAction(env, first)
    state, reward, done, info = env.step(action)
    env.render()
    time.sleep(0.5)
    if done:
        env.reset()
        env.render()
        first, second = randomFirst()
        time.sleep(0.5)
        continue
    # 后手行动
    action = randomAction(env, second)
    state, reward, done, info = env.step(action)
    env.render()
    time.sleep(0.5)
    if done:
        env.reset()
        env.render()
        first, second = randomFirst()
        time.sleep(0.5)
        continue
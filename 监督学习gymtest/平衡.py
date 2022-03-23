# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/18 14:29
import gym
env = gym.make("CartPole-v1")#创建一个环境
observation = env.reset()#环境初始化
for _ in range(1000):
  """ render()函数在这里扮演图像引擎的角色。一个仿真环境必不可少的两部分是物理引擎和图像引擎。物理引擎模拟环境中物体的运动规律；图像引擎用来显示环境中的物体图像 """
  env.render()#图像引擎
  action = env.action_space.sample() # your agent here (this takes random actions)
  """该函数在仿真器中扮演物理引擎的角色。其输入是动作a，输出是：下一步状态，立即回报，是否终止，
  调试项。该函数描述了智能体与环境交互的所有信息，是环境文件中最重要的函数。
  在该函数中，一般利用智能体的运动学模型和动力学模型计算下一步的状态和立即回报，并判断是否达到终止状态
  """
  observation, reward, done, info = env.step(action)#物理引擎

  if done:
    observation = env.reset()
env.close()
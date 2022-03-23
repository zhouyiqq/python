import gym
from gym.envs.classic_control import rendering
class GridEnv(gym.Env):
    def __init__(self):
    	# 600*400 的窗口
        self.viewer = rendering.Viewer(600,400)

    def render(self,mode='human'):
        # 画网格
        self.viewer.draw_line((100,300),(500,300))
        self.viewer.draw_line((100,200),(500,200))
        self.viewer.draw_line((100,300),(100,100))
        self.viewer.draw_line((180,300),(180,100))
        self.viewer.draw_line((260,300),(260,100))
        self.viewer.draw_line((340,300),(340,100))
        self.viewer.draw_line((420,300),(420,100))
        self.viewer.draw_line((500,300),(500,100))
        self.viewer.draw_line((100,100),(180,100))
        self.viewer.draw_line((260,100),(340,100))
        self.viewer.draw_line((420,100),(500,100))

        # 画金币  									添加平移这个属性
        self.viewer.draw_circle(40,color=(1,0.9,0)).add_attr(rendering.Transform(translation=(300,150)))
        # 画陷阱
        self.viewer.draw_circle(40,color=(0,0,0)).add_attr(rendering.Transform(translation=(140,150)))
        self.viewer.draw_circle(40,color=(0,0,0)).add_attr(rendering.Transform(translation=(460,150)))
        # 机器人
        self.viewer.draw_circle(30,color=(0.8,0.6,0.4)).add_attr(rendering.Transform(translation=(140,250)))
        return self.viewer.render(return_rgb_array=mode == 'human')


# 测试环境
env = GridEnv()
while True:
    env.render()

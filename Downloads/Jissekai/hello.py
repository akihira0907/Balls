import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import math

class Ball():
    max_x = 7
    min_x = -7
    max_y = 7
    min_y = -7
    def __init__(self):
        self.x = 0.1 * np.random.randint(-50, 50)
        self.y = 0.1 * np.random.randint(-50, 50)
        self.vx = 0.05 * np.random.randint(-50, 50)
        self.vy = 0.05 * np.random.randint(-50, 50)

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.x > self.max_x:
            self.x = self.max_x
            self.velocity_x_update()
        elif self.x < self.min_x:
            self.x = self.min_x
            self.velocity_x_update()
        if self.y > self.max_y:
            self.y = self.max_y
            self.velocity_y_update()
        elif self.y < self.min_y:
            self.y = self.min_y
            self.velocity_y_update()
            
    def velocity_x_update(self):
        self.vx *= -0.01 * np.random.randint(90, 111)
    def velocity_y_update(self):
        self.vy *= -0.01 * np.random.randint(90, 111)

def avoidance(b1, b2):
    distance = math.sqrt((b1.x-b2.x)**2 + (b1.y-b2.y)**2)
    if distance < 2.0:
        b1.velocity_x_update()
        b1.velocity_y_update()

def update_ani(i):
    ax.cla()
    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)

    dt = 0.3
    ball1.update(dt)
    ball2.update(dt)
    ball3.update(dt)

    avoidance(ball1, ball2)
    avoidance(ball3, ball2)

    ax.scatter(ball1.x, ball1.y, color="b", s=100)
    ax.scatter(ball2.x, ball2.y, color="r", s=100)
    ax.scatter(ball3.x, ball3.y, color="b", s=100)
    
############################################################
############################################################

## plot 初期化
# グラフ仕様設定
fig = plt.figure()

# Axes インスタンスを作成
ax = fig.add_subplot(111)

# 軸
# 最大値と最小値⇒軸の範囲設定
# max_x = 5
# min_x = -5
# max_y = 5
# min_y = -5
# 
# ax.set_xlim(min_x, max_x)
# ax.set_ylim(min_y, max_y)

# 軸の縦横比, 正方形，単位あたりの長さが等しくなります
ax.set_aspect('equal')

# 軸の名前設定
ax.set_xlabel('X [m]') 
ax.set_ylabel('Y [m]') 

# その他グラフ仕様
ax.grid(True) # グリッド

# 凡例
# ax.legend()

# ステップ数表示
step_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

ball1 = Ball()
ball2 = Ball()
ball3 = Ball()

animation = ani.FuncAnimation(fig, update_ani, interval=50, frames=500)
plt.show()

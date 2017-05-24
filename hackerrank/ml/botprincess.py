
# 5 - 24 - 2017
# https://www.hackerrank.com/challenges/saveprincess

def displayPathtoPrincess(dx,dy):
    x_dir = "RIGHT" if dx < 0 else "LEFT"
    y_dir = "UP" if dy < 0 else "DOWN"
    for i in range(abs(dx)):
        print(x_dir)
    for i in range(abs(dy)):
        print(y_dir)


n = int(input())
m_cord = []
p_cord = []

for i in range(n):
    row = input().strip()
    if row.find("m") >= 0:
        m_cord = [row.find("m"),i]
    if row.find("p") >= 0:
        p_cord = [row.find("p"),i]

x_dist = p_cord[0] - m_cord[0]
y_dist = p_cord[1] - m_cord[1]


displayPathtoPrincess(x_dist,y_dist)

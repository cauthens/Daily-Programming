n = int(input().strip())
height = [int(i) for i in input().strip().split(' ')]

m_height = max(height)
count = height.count(m_height)

print(count)

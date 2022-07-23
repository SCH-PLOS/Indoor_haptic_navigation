result = [[-20,'a'],[-33,'b'],[-12,'c']]

# aver = 20
# j=['a','gw','we']

# result.append([aver,j[1]])

# a = max(result)
# print(a[0])

# ev 플래그 해제하기
# 코너 플래그 설정하고 해제하기
# 코너 판별: 전체 경로에서 계산해서 
import math

route = [(4,90,12),(4,81,12),(4,72,12),(4,65,12),(4,65,19),(6,65,13),(6,71,13)]
special = []


def want_direction(now, next):
    x1 = now[1];    y1 = now[2]
    x2 = next[1];    y2 = next[2]
    x = x1 - x2;         y = y1 - y2

    diag = math.sqrt(x**2 + y**2)
    result = math.acos(diag/abs(x))
    degree = math.degrees(result)

    if x > 0 and y == 0:         # 서측  
        return 270          
    elif x < 0 and y == 0:      # 동측
        return 90           
    elif y > 0 and x == 0:      # 남측      
        return 180          
    elif y < 0 and x == 0:      # 북측    
        return 0            
    elif x < 0 and y < 0:       # 1사분면
        return 270 - degree
    elif x < 0 and y > 0:       # 4사분면
        return 270 + degree
    elif x > 0 and y < 0:       # 2사분면
        return 90 - degree
    elif x > 0 and y > 0:       # 3사분면
        return 90 + degree

for s in len(route):
    now_x = route[s][1];    now_y = route[s][2]
    next_x = route[s+1][1];    next_y = route[s+1][2]
    if now_x-next_x != 0 or now_y-next_y != 0:
        special.append(route[s])
    want_direction(route[s],route[s+1])
    
print(special)
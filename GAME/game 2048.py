def run2048():
    print("2048 게임 시작")


'''
#### #### #### ####
#### #### #### ####
#### #### #### ####
#### #### #### ####

0008 0016 #### ####
0008 0004 0004 0008
0512 0128 0064 0008
2048 1024 0512 0128

1. 화면출력 모두 ####이고, 2와 4가 랜덤 위치에 뜨게
#### #### 0004 ####
#### 0002 #### ####
#### #### #### ####
#### #### #### ####

2. 사용자의 움직임이 있으면 그 방향으로 숫자를 밀고 빈칸 중 하나(랜덤위치)에 2, 4 중에서 하나가 뜨게
3. 블럭이 한방향으로 모일때 해당 방향에 같은 숫자가 있으면 블럭 합치기

(아랫방향 입력시)
#### #### #### ####
#### #### 0002 ####
#### #### #### ####
#### 0002 0004 ####

(왼쪽방향 입력시)
#### #### #### ####
0002 #### 0002 ####
#### #### #### ####
0002 0004 #### ####

(아랫방향 입력시)
#### #### #### ####
0002 #### #### ####
#### #### #### ####
0004 0004 #### ####


4. 최종적으로 2048이 만들어졌으면 WIN.
'''
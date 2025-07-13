input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # column을 숫자로 치환(1~8)

# 이동할 수 있는 8가지 경우의 수
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0
for step in steps:
  next_column = column + step[0]
  next_row = row + step[1]

  # row, column 모두 1~8까지만 가능
  if next_column > 8 or next_row > 8 or next_column < 1 or next_row < 1 :
   continue

  result += 1
    
print(result)

'''
처음엔 8가지 경우를 모두 별도의 함수로 정의했다.(ex) left_2_up_1) 
그런데 그렇게 하니까 시간이 오래 걸려서 20분 안에 못 풀 것 같았고
각 움직임 8개를 상세히 직접 적어줘야 돼서 실수할 여지가 너무 많았다. 
(ex) left_2_up_1면 column을 -2 하고 row를 + 1 하고, 제약조건(1 ~ 8 안에 들어와 있는지) 체크. 
     left_2_down_1이면 column을 -2 하고 row를 -1 하고, ... ...)

그래서 답안 예시를 보니 훨씬 간단하고 실수할 여지가 적은 방식이 나와 있어서,
이 방법으로 풀어보았다!

'''

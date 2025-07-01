# n: 행, m: 열
n, m = map(int, input().split())
# 행(n)만큼 입력 받기(n번)
max = 0

for i in range(n):
  # 입력받기 
  rowData = list(map(int, input().split()))
  # 각 행에서 가장 작은 숫자 찾기 
  rowMin = min(rowData)

  # 각 행의 최소값과 max 비교해서 max 업데이트
  if max < rowMin:
    max = rowMin

print('max: ', max)
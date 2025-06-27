# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
# 정렬(오름차순)
data.sort()

print('data: ', data)

first = data[n - 1]
second = data[n - 2]

print('first: ', first)
print('second: ', second)

# 가장 큰 거 2개 선택
sum = 0
mCount = 0

while True:
  # 가장 큰 수를 k번 더하기
  for i in range(k):
    # 총 횟수(m)를 넘지 않았다면 k번만큼 돌린다
    '''
    - k만큼 반복은 range(k)로 하고 있어서 애초에 같은 수를 연속 k번 초과해서 더할 수 없게 설계되어 있으니, 
      연속 k번 넘었나..? 하는 체크는 안 해줘도 됨
    - 연속 k번 돌렸으면 이제 second로 1회 막아줘야 할 차례니(for문도 종료되니) 자연스레 그 아래 코드(second 더하는 코드)가 실행된다
    '''

    # 총 횟수(m)를 넘었다면 종료
    if mCount >= m:
      break

    sum += first
    mCount += 1

    print(f'first 더한 후의 sum: {sum}, mCount: {mCount} / {m}')
  
  if mCount >= m:
    break

  # 두 번째로 큰 수를 더해주기
  sum += second
  mCount += 1

  print(f'second 더한 후의 sum: {sum}, mCount: {mCount} / {m}')
    
print('sum: ', sum)

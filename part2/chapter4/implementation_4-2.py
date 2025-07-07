# N 입력 받기(n: 0 ~ 23)
N = int(input())
count = 0

for i in range(N + 1):
  if i < 10:
    i = '0' + str(i)
    # 난 시간이 hh:mm:dd 형태의 문자열이 돼야 한다고 생각해서 이렇게 한자리 수일 때 0 붙여줬는데
    # 답안 보고 생각해 보니 그럴 필요가 없었다! (3의 개수만 세면 되니까 0이 앞에 있든 없든 결과는 똑같으니)

  for j in range(60):
    if j < 10:
      j = '0' + str(j)

    for k in range(60):
      if k < 10:
        k = '0' + str(k)

      concatTimeString = str(i) + str(j) + str(k)
      
      if '3' in concatTimeString:
        count += 1

print(f"count: {count}")


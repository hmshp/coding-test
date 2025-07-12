N = int(input())
plans = input().split()

currentX = 1
currentY = 1

# 움직임 정의

def moveRight(): 
  global currentY
  # Y를 + 1 (단, 기존 Y가 5 이상이면 움직이지 않음)
  if currentY >= 5: 
    return
  currentY += 1

def moveLeft(): 
  global currentY
  # Y를 - 1 (단, 기존 Y가 1 이하이면 움직이지 않음)
  if currentY <= 1: 
    return
  currentY -= 1

def moveUp(): 
  global currentX
  # X를 - 1 (단, 기존 X가 1 이하이면 움직이지 않음)
  if currentX <= 1: 
    return
  currentX -= 1

def moveDown(): 
  global currentX
  # X를 + 1 (단, 기존 X가 5 이상이면 움직이지 않음)
  if currentX >= 5: 
    return
  currentX += 1

for plan in plans:
  # 각 plan대로 이동
  if plan == 'R':
    moveRight()
  elif plan == 'L':
    moveLeft()
  elif plan == 'U':
    moveUp()
  else:
    moveDown()


print(f'{currentX} {currentY}')

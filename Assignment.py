print("과자집에 가는 길:", end = " ")

stack = [None, None, None, None, None, None]
top = -1

stack[top] = "주황"
print(stack[top], "-->", end=' ')
top += 1
stack[top] = "초록"
print(stack[top], "-->", end=' ')
top += 1
stack[top] = "파랑"
print(stack[top], "-->", end=' ')
top += 1
stack[top] = "보라"
print(stack[top], "-->", end=' ')
top += 1
stack[top] = "빨강"
print(stack[top], "-->", end=' ')
top += 1
stack[top] = "노랑"
print(stack[top], "-->", end=' ')

print("과자집")

print("우리집에 오는 길:", end = ' ')
for i in range(len(stack)):
    print(stack[top], "-->", end=' ')
    top -= 1

print("우리집")
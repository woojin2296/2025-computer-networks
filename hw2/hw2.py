print("문자열 “My name is 본인이름”에 대해 다음 물음에 답하라")
print()

str = "My name is Woojin Lim"

print("1. 문자열의 문자수를 출력하라.")
print(len(str))
print()

print("2. 문자열을 10번 반복한 문자열을 출력하라.")
print(str*10)
print()

print("3. 문자열의 첫 번째 문자를 출력하라.")
print(str[0])
print()

print("4. 문자열에서 처음 4문자를 출력하라.")
print(str[:4])
print()

print("5. 문자열에서 마지막 4문자를 출력하라.")
print(str[-4:])
print()

print("6. 문자열의 문자를 거꾸로 출력하라.")
print(str[::-1])
print()

print("7. 문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라.")
print(str[1:-1])
print()

print("8. 문자를 모두 대문자로 변경하여 출력하라.")
print(str.upper())
print()

print("9. 문자를 모두 소문자로 변경하여 출력하라.")
print(str.lower())
print()

print("10. 문자열에서 'a'를 'e'로 대체하여 출력하라.")
print(str.replace('a', 'e'))
print()
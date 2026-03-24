print("*   *")
print(" * *")
print("  *")

print("My second program.")
print("2")
print("programs")

print("I have")
print(3)
print("books.")

print("My age:")
print(15)
print("My weight:")
print(67.3)

print("(@) (@)"  )
print("( *~* ) ")
print(" (^^^)")

print("5 + 7 = 5 + 7")
print("5 + 7 =", 5 + 7)

print("5 + 10 =", 5 + 10)

print("Program", "number", 3)
print("Program", "number", 3)

print(10 - 5, "= 10 - 5")

print("Solved at Jungol")

print("Do you know Python?")
print("Yes I do!")

print("Animal:", "Panda")

print("  *  ")
print(" * * ")
print("*****")

print("5 + 6 = ",  5 + 6)
print("10 - 3 = ",  10 - 3)

print("Program", "number", 3)
print("Program", "number", 3)

print("kor 90")
print("mat 80")
print("eng 100")
print("hap" , 90 + 80 + 100)

print("*   * ")
print(" * *")
print("  *")

letter = 'how are YOU?'
str1 = letter.find('u')

print(letter.lower())
print(letter.upper())
print(letter.title())
print(letter.capitalize())
print(letter.swapcase())
print(letter.split())

letter = 'how are you?'
print(letter.count('o'))

#--------------------------------------------------------------------------


# 1. upper() -> 문자열 모두 대문자로 바꿈
# 2. lower() -> 문자열 모두 소문자로 바꿈
# 3. title() -> 문자열의 첫글자를 대문자로 바꿈
# 4. strip() -> 문자열 양쪽의 공백을 바꿈
# 5. replace() -> 문자열의 일부를 다른 문자로 바꿔줌
# 6. find() -> 특정 문자가 처음 나오는 위치
# 7. count() -> 특정 문자가 몇 번 나오는지 알려줌
# 8. startswitch() -> 특정 문자열로 시작하는지 확인해줌
# 9. endswitch() -> 특정 문자열로 끝나는지 확인해줌
# 10. split() -> 문자열을 잘라서 리스트로 만들어줌
# 11. join() -> 리스트에 들어있는 문자열을 하나로 합침
# 12. isalpha() -> 문자열이 문자로만 이루어져 있는지 확인
# 13. isalnum() -> 문자와 숫자로만 이루어져있는지 확인
# 14. len() -> 문자열 길이를 구해줌
# 15. isdigit ->  숫자로만 이루어져있는지 확인
# 16. capirtalize() -> 첫글자만 대문자로 바꿈
# 17. swapcase() -> 모든 문자열의 대소문자를 변환


s = '나도고등학교'

print(s.startswith('나도'))
print(s.endswith('초등학교'))

s1 = '..나도고등학교..'

print(s1.strip('.'))

s2 = '.,나도고등학교,.'

print(s2.strip('.'))

s3 = '나도고등학교'

print(s.replace('고등학교','고교'))

s4 = '나도고교너도고교'

print(s4.replace('고교','고등학교'))

s5 = '나도고등학교'

print(s5.find('학교'))
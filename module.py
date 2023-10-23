# задание 1

#def all_divisors(number):
#    divisors = []
#    for i in range(1, int(number**0.5) + 1):
#        if number % i == 0:
#            divisors.append(i)
#            if i != number // i:
#                divisors.append(number // i)
#    divisors.sort()
#    return divisors
#numbers = [23436, 190187200, 380457890232]
#for number in numbers:
#    divisors = all_divisors(number)
#    print(f"Делители числа {number}: {divisors}")




# 2 задача

#def three_args(*, var1=None, var2=None, var3=None):
#    args = {
#        'var1': var1,
#        'var2': var2,
#        'var3': var3
#    }
#    filtered_args = {key: value for key, value in args.items() if value is not None}
#    if filtered_args:
#        print("Переданы аргументы:", ", ".join(f"{key} = {value}" for key, value in filtered_args.items()))
#    else:
#        print("Нет переданных аргументов")
#three_args(var1=2, var3=10)
#three_args(var2=5)
#three_args()




# 3 задача

#def palindrome(s):
#    s = s.lower().replace(" ", "")
#    return s == s[::-1]
#print(palindrome("Папа"))
#print(palindrome("Шалаш"))





# 4 задача

#import collections
#text = 'Я построил шалаш шалаш шалаш'
#words = text.split()
#counter = collections.Counter(words)
#most_common, occurrences = counter.most_common()[0]
#longest = max(words, key=len)
#print(most_common, longest)




# 5 задача

#n, t = map(int, input().split())
#matrica = [[0] * t for _ in range(n)]
#dx, dy, x, y = 0, 1, 0, 0
#for i in range(1, n * t + 1):
#    matrica[x][y] = i
#    if matrica[(x + dx) % n][(y + dy) % t]:
#        dx, dy = dy, -dx
#    x += dx
#    y += dy
#for line in matrica:
#    print(*(f'{i:<3}' for i in line), sep='')
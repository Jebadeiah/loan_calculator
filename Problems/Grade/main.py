score = int(input())
max_score = int(input())
grade = score / max_score * 100
if 90 <= grade <= 100:
    print('A')
elif 80 <= grade < 90:
    print('B')
elif 70 <= grade < 80:
    print('C')
elif 60 <= grade < 70:
    print('D')
elif grade < 60:
    print('F')

count = int(input());
score = 0;
for item in range(count):
    score += int(input());
print(float(score/count))
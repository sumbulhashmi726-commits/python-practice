n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))

highest = max(scores)
scores.remove(highest)
runner_up = max(scores)

print("Runner-up score:", runner_up) 
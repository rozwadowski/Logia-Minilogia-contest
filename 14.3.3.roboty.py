# http://logia.oeiizk.waw.pl/logia/page.php?sr=logia14/3etap


def spotkanie(s1, s2):
    robots = [[0, 0, s1], [0, 0, s2]]
    for i in range(100):
        for robot in robots:
            if robot[2][i % len(robot[2])] == "g":
                robot[1] += 1
            elif robot[2][i % len(robot[2])] == "d":
                robot[1] -= 1
            elif robot[2][i % len(robot[2])] == "p":
                robot[0] += 1
            elif robot[2][i % len(robot[2])] == "l":
                robot[0] -= 1
        if (robots[0][0], robots[0][1]) == (robots[1][0], robots[1][1]):
            return i+1
    return 0


print(spotkanie("pd", "g"))
print(spotkanie("gp", "pg"))
print(spotkanie("dg", "ggppddll"))

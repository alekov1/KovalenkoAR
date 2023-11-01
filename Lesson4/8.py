def Steps(N):
    if 9 < N >= 0:
        return
    step = ""
    for i in range(1, N + 1):
        step += f"{i}"
        print(step)

countstep = int(input())
Steps(countstep)

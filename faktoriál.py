def faktorial(N):
    if N==0:
        return 1
    else:
        return N*faktorial(N-1)

print(faktorial(3))
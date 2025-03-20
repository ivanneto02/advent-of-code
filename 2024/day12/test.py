A = "AXAXA"
B = "AAAAA"
count = 0
found = False
for i in range(0, len(A)):
    if not found:
        if A[i] == "A" and B[i] != "A":
            found = True
            count += 1
    else:
        if A[i] == "A" and B[i] != "A": continue
        else: found = False

print(count)
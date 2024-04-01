from threading import Thread

# import sys
# n = sys.stdin.readline().strip()
#
# prev_number = int(sys.stdin.readline().strip())
#
# for i in range(1, int(n)):
#     next_number = int(sys.stdin.readline().strip())
#     if prev_number != next_number or i == int(n) - 1:
#         print(prev_number)
#     prev_number = next_number

A = 5
B = 3
print(A if B > A else B, A if B < A else B)
print(A + B, A - B < B, A - B)
print("Fine" if B + A < A else A + B if B - A < A else B - A)
print("Fine" if B + A < A else A, B if B - A < A else B - A)
print(A == B, A - B >= B, A - 2 >= B)
print("Fine" if B - A < A else A if B < A else B)
#given an array a of n integers representing transaction amount and array D of N strings representing transaction date, returns the final balance of the account at end of year

def solution(A, D):
  # write your code in Python 3.6
  balance = 0
  for i in range(len(A)):
    #print(A[i], D[i])
    if D[i] == 'D':
      balance += A[i]
    else:
      balance -= A[i]
  return balance

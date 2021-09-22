#given an array a of n integers representing transaction amount and array D of N strings representing transaction date, returns the final balance of the account at end of year 2020. Transaction number K (for K within the rang[0..N-1]) was executed on the date represented vy D[K] for the amount A[K].

def solution(A, D):
  # write your code in Python 3.6
  balance = 0
  transactions = []
  dateformat = "%Y-%m-%d"
  import datetime
  fee = 5
  for i in range(len(A)):
    transactions.append([A[i], datetime.datetime.strptime(D[i], dateformat)])
  transactions.sort(key=lambda x: x[1])
  for i in range(len(transactions)):
    balance += transactions[i][0]
    if i < len(transactions) - 1:
      if transactions[i+1][1].year != transactions[i][1].year:
        balance -= fee
  return balance











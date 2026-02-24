def sum(aList):
  sum = 0
  for v in aList:
    sum = sum + v

def avg(aList):
  try:
    s = sum(aList)
    return float(s) / len(aList)
  except TypeError as ex:
    return "Non numeric data"

def avgReport(aList):
  try:
    m = avg(aList)
    print("Average+15%=", m*1.15)
  except TypeError as ex:
    print("typeerror: ", ex.args)
  except ZeroDivisionError as ex:
    print("ZeroDivisionError: ", ex.args)

avgReport([1, 2, "hi", 4])
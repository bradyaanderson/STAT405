# There are more effient ways to do this in Python. But this best simulates how I would choose to compute these.
import math

def calcMean(data):
  data_sum = 0
  for n in data:
    data_sum += n
  return float(data_sum) / len(data)

def calcMedian(data):
  data_len = len(data)
  midpoint = (data_len - 1) / 2
  data.sort()
  if (data_len % 2 == 0):
    x1 = data[int(math.floor(midpoint))]
    x2 = data[int(math.ceil(midpoint))]
    return ((x1 + x2) / 2)
  return data[midpoint]

def calcMode(data):
  mode = []
  max_ocr = 0
  data_set = set(data)
  for n in data_set:
    ocr = data.count(n)
    if (ocr > max_ocr):
      max_ocr = ocr
      mode = []
      mode.append(n)
    elif (ocr == max_ocr):
      mode.append(n)
  return mode

def calcRange(data):
  data_max = data[0]
  data_min = data[0]
  for n in range(len(data)):
    if (data[n] < data_min):
      data_min = data[n]
    elif (data[n] > data_max):
      data_max = data[n]
  return data_max - data_min

# data_type: 1 for sample, 2 for population
def calcVariance(data, data_type):
  if (data_type != 1 and data_type != 2):
    raise Exception("Invalid input for data_type (" + str(data_type) + "). Use 1 for sample, 2 for population")
  mean = calcMean(data)
  temp_sum = 0.0
  for n in data:
    temp_sum += (n - mean)**2
  if (data_type == 1):
    return temp_sum / (len(data) - 1)
  elif (data_type == 2):
    return temp_sum / (len(data))
    
def calcStdDev(data, data_type):
  variance = calcVariance(data, data_type)
  return  math.sqrt(variance)

def printStats(data, data_type):
  print("Mean: " + str(calcMean(data)))
  print("Median: " + str(calcMedian(data)))
  print("Mode: " + str(calcMode(data)))
  print("Range: " + str(calcRange(data)))
  print("Variance: " + str(calcVariance(data, data_type)))
  print("StdDev: " + str(calcStdDev(data, data_type)))


### MAIN ###
data = [16,10,36,16,51,43,18,27,21,32,24]
printStats(data, 3)
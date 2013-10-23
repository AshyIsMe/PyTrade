import math

def crossover(seriesA, seriesB):
  if len(seriesA) != len(seriesB):
    raise Exception(0, 'seriesA and seriesB are not the same length')

  comparisons = (seriesA - seriesB) / abs(seriesA - seriesB)
  cross = [0]
  for i in range(1,len(comparisons)):
    current = comparisons[i]
    prev = comparisons[i-1]
    if (math.isnan(current) or math.isnan(prev)) or current == prev:
      # No change so no crossover.  (or NaN so no crossover)
      cross.append(0)
    elif current != prev:
      cross.append(current)

  return cross




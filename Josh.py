Investment = 250000
Rate = 10
Time = 30
print("\n{:<10} {:<15} {:<17} {:<17} ".format("Time","Investment","Rate","Total"))
counter = 0
for Time in range (Time):
  Time = Time +1
  Total = Investment*(1+Rate/100)**Time
  print("{:<10} {:<15.2f} {:<17.2f} {:<17.2f} ".format(Time, Investment, Rate, Total))

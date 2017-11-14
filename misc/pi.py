import math
import time
import sys

num = 355
den = 113

quo = num/den
sys.stdout.write("%s." % str(quo))
sys.stdout.flush()
rem = num%den
count = 0
while True:
    count = count + 1
    if rem != 0:
        rem = num%den
        num = rem*10
        quo, res = math.modf(num/den)
        quo = int(res)
    else:
        quo = 0
        rem = num
    sys.stdout.write(str(quo))
    sys.stdout.flush()
    time.sleep(0.01)
    if count > 100000:
        raw_input()
        break


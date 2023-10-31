#!/usr/bin/python3
for i in range(65, 94):
    if i == ord('e') or i == ord('q'):
        continue
    else:
        print("{:c}".format(i), end="")

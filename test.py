#file for quick code tests
import re
x = "hello world, my name is abhishek"

y = re.findall(r"[\w']+|[.,!?;]", x)

print(y)
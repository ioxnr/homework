import sys


def salary(output, rate, premium):
    return (output * rate) + premium


file, a, b, c = sys.argv

print(salary(int(a), int(b), int(c)))

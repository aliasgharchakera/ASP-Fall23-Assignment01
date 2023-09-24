import math

def test1():
    ans = 0
    for i in range(-3, 5, 1):
        ans += math.cos(i*math.pi/8)
    ans /= 8
    var = 0
    for i in range(-3, 5, 1):
        var += (math.cos(i*math.pi/8) - ans)**2
    var /= 8
    print(ans, var)
    
def test2():
    ans = 0
    for i in range(-3, 5, 1):
        ans += math.pow(math.cos(i*math.pi/8), 2)
    ans /= 8
    var = 0
    for i in range(-3, 5, 1):
        var += (math.pow(math.cos(i*math.pi/8), 2) - ans)**2
    var /= 8
    print(ans, var)
test2()
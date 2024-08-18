import matplotlib.pyplot as plt


def f(x):
    # ||x-1|-2|
    return abs(abs(x - 1) - 2)


plt.plot([i for i in range(-10, 11)], [f(i) for i in range(-10, 11)])
# plot the line
m = 40
# plot y=m/100
plt.plot([i for i in range(-10, 11)], [m / 100 for i in range(-10, 11)])

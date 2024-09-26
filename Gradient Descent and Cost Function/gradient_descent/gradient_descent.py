import numpy as np

def gradient_descent(x,y) :
    a_curr = b_curr = 0
    iteration = 10000
    n = len(x)
    # Reduce a and b until you reach the perfect line
    learning_rate = 0.08
    for i in range(iteration) :
        y_predicted = a_curr * x + b_curr
        cost = (1/n) * sum([val ** 2 for val in (y-y_predicted)])
        ad = -(2/ n) * sum(x*(y-y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        a_curr = a_curr - learning_rate * ad
        b_curr = b_curr - learning_rate * bd
        print("a {}, b {},cost {}, iteration {}".format(a_curr,b_curr,cost,i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)
# references: 
#   http://mortada.net/fibonacci-numbers-in-python.html
#   https://stackoverflow.com/questions/12986095/how-do-i-turn-a-while-loop-into-a-recursive-method
#   https://stackoverflow.com/questions/19079143/how-to-plot-time-series-in-python
#   https://matplotlib.org/users/pyplot_tutorial.html

from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

window_size = 1

# Create model
model = Sequential()
model.add(Dense(1,
                input_dim=window_size,
                activation='linear'))
model.compile(loss='mean_squared_error',
              optimizer='adam')	
model.summary()

def recursive_sequence(s, w, i, n):
	if n == 0:
		return
	else:
		values.append(w * s - w * s**2)
		# print(values[-1])
		steps.append(i)
		# print(i)
		# recursion passing next output as input
		recursive_sequence(values[-1], w, i+1, n-1)

values = []
steps = []
n = 50
i = 0
s = 0.5
w = 1
print(recursive_sequence(s, w, i, n))
# print("Values: ", len(values))
# print("Steps: ", len(steps))
plt.plot(steps, values, 'ro')

values = []
steps = []
n = 50
i = 0
s = 0.5
w = 3
print(recursive_sequence(s, w, i, n))
plt.plot(steps, values, 'b-')

values = []
steps = []
n = 50
i = 0
s = 0.0001
w = 4
print(recursive_sequence(s, w, i, n))
plt.plot(steps, values, 'g-')

plt.xlabel('Steps')
plt.ylabel('Values')
plt.axis([0, 50, 0, 1.5])
plt.show()

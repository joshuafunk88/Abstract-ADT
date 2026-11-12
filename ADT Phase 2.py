from collections import deque

class EarlyWarningWindow:

    def __init__(self, capacity):
        # to create the initial list
        self._L = deque()
        self._capacity = capacity
        self._S = 0         #initiate for mean
        self._Q = 0         #inititate for variance
        self._P = 0         #initiate for autocorrelation

    def enqueue(self, x):
        if self._L:
            self._P += self._L[-1] * x          # multiply last value in queue with incomming value

        self._L.append(x)
        self._S += x
        self._Q += x ** 2
        if len(self._L) > self._capacity:
            removed = self._L.popleft()
            self._S -= removed
            self._Q -= removed ** 2
            self._P == removed * self._L[0]

    def mean(self):
        mean = self._S / len(self._L)
        return mean

    def variance(self):
        avg_of_squares = self._Q / len(self._L)
        mean_squared = self.mean() ** 2
        return avg_of_squares - mean_squared


w = EarlyWarningWindow(4)
for x in [1,2,3,4,5]:
    w.enqueue(x)
print(w._L)
print(w.variance())
print(w.mean())
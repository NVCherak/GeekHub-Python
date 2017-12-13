class Queue():
    _queue = []

    def __init__(self, maxsize):
        self._maxsize = maxsize

    def put(self, item):
        if(len(self._queue) == self._maxsize):
            del self._queue[0]
        self._queue.append(item)

    @property
    def size(self):
        return len(self._queue)

    def get(self):
        return self._queue


class Calc():
    _queueQuantity = 5
    _queue = Queue(_queueQuantity)

    def add(self, a, b):
    # method addition two operands
        self._last_result = a + b # remember result
        self._enqueue(a, b, '+')
        return a + b

    def subtract(self, a, b):
    # method substraction two operands
        self._last_result = a - b
        self._enqueue(a, b, '-')
        return a - b

    def multiply(self, a, b):
    # method multiplication two operands
        self._last_result = a * b
        self._enqueue(a, b, '*')
        return a * b

    def divide(self, a, b):
    # method division two operands
        self._last_result = a / b
        self._enqueue(a, b, '/')
        return a / b

    @property
    def lastResult(self):
        return _last_result

    def _enqueue(self, a, b, operator):
        try:
            fileQueue = open('queue', 'a') #create a file 'queue'
            fileQueue.close()
        except Exception as e:
            print('Error!' + str(e))

        try:
            with open('queue') as fileQueue:
                for line in fileQueue:
                    self._queue.put(line)
        except Exception as e:
            print('Error!' + str(e))

        self._queue.put(str(a) + operator + str(b) + '='
            + str(self._last_result) + '\n')

        try:
            with open('queue', 'w') as fileQueue:
                for item in self._queue.get():
                    fileQueue.write(item)
        except Exception as e:
            print('Error!' + str(e))

    def get_last_actions(self):
        try:
            with open('queue') as fileQueue:
                for line in fileQueue:
                    self._queue.put(line)
        except Exception as e:
            print('Error!' + str(e))

        return self._queue.get()


calc = Calc()
calc.add(10, 4)
calc.subtract(5, 7)
calc.add(57, 13)
calc.multiply(5, 5)
calc.divide(144, 12)
calc.multiply(2, 2)
calc.add(100, 7)
calc.subtract(90, 4)
calc.add(222, 86)
calc.multiply(14, 12)
calc.divide(842, 4)
calc.multiply(7, 13)
print(calc.get_last_actions())

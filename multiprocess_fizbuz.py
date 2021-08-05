from multiprocessing import Process
import time

class MyProcessor(Process):

    def __init__(self, num):
        super().__init__()
        self.__num = num

    def fizz_buzz(self, num: int):
        result_list = []
        for i in range(1, num + 1):
            result = ''
            if i % 3 == 0:
                result += 'fizz'
            if i % 5 == 0:
                result += 'buzz'
            if not result:
                result = str(i)
            result_list.append(result)
        return result_list

    def run(self):
        self.fizz_buzz(self.__num)


start = time.time()
processes = []
num_list = [12000000, 38000000, 28000000, 2520000, 22850000]
for n in num_list:
    process = MyProcessor(n)
    process.start()
    processes.append(process)
for p in processes:
    p.join()
stop = time.time()
print(f'multi process: {stop - start:.3f} seconds')
import time

def fizz_buzz(num: int):
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


start = time.time()
num_list = [12000000, 38000000, 28000000, 2520000, 22850000]
for n in num_list:
    fizz_buzz(n)
stop = time.time()
print(f'Sequential processing: {stop - start:.3f} seconds')
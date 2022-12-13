import datetime 

min_n = 1
max_n = 100

def get_rand():
    return datetime.datetime.now().microsecond%10

n = get_rand()
print(n)
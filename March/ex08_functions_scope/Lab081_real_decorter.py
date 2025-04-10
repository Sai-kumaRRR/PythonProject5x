import time


def time_decorater(func):
    def wrapper():


start_time = time.time()
print(start_time)
func()
end_time = time.time()
print(end_time)
print("Total time take by func -> ", end_time - start_time)

return wrapper()


def print_logs(func):
    def wrapper():
        print("Starting log")
        func()
        print("ending log")

        return wrapper()


@add_decorator
def test_ui_1():
    print("Add a function , time taken by this function 1")


time.sleep(2)


@time_decorator
def test_ui_2():
    print("add a function , time taken by this function 2")


time.sleep(5)

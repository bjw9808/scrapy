# 多进程TEST
# from multiprocessing import Process
# import time
#
# def process_test():
#     for i in range(100000000):
#         i = i + 1
#     return 1
#
# def main():
#     t_1 = time.time()
#     p_1 = Process(target=process_test)
#     p_2 = Process(target=process_test)
#     p_3 = Process(target=process_test)
#     p_4 = Process(target=process_test)
#     p_1.start()
#     p_2.start()
#     p_3.start()
#     p_4.start()
#     p_1.join()
#     p_2.join()
#     p_3.join()
#     p_4.join()
#     t_2 = time.time()
#     print(t_2 - t_1)
#
# if __name__ == '__main__':
#     main()
# 输出4.78817343711853

# 单线程TEST
# import time
#
# def process_test():
#     for i in range(100000000):
#         i = i + 1
#     return i
#
# def main():
#     t_1 = time.time()
#     for i in range(4):
#         process_test()
#     t_2 = time.time()
#     print(t_2 - t_1)
#
# if __name__ == '__main__':
#     main()
# 输出 16.809072256088257

# 多线程TEST
# import threading
# import time
#
# def thread_test():
#     for i in range(100000000):
#         i = i + 1
#     return i
#
# def main():
#     t1 = time.time()
#     t_1 = threading.Thread(target=thread_test)
#     t_2 = threading.Thread(target=thread_test)
#     t_3 = threading.Thread(target=thread_test)
#     t_4 = threading.Thread(target=thread_test)
#     t_1.start()
#     t_2.start()
#     t_3.start()
#     t_4.start()
#     t_1.join()
#     t_2.join()
#     t_3.join()
#     t_4.join()
#     t2 = time.time()
#     print(t2 - t1)
# if __name__ == '__main__':
#     main()
# 输出：16.85694432258606
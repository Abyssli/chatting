'''
    multiprocessing创建两个进程,同时复制一个文件的上下两半部分,
    各自复制到一个新的文件里(产生两个新文件)
    (文件:按字节数区分上下部分)
'''

from multiprocessing import Process
import os
file_name = input("输入文件名:")
# 父进程打开文件,子进程可以直接使用,因为自己进程会完全复制父进程的内存空间
'''
    python多进程机制 
        1.由父进程创建两个子进程,两个子进程分别open,两个子进程都连接同一个文件,
        此时该文件各有各的一套属性特征(也就是文件偏移量没有任何影响)
        
        2.在父进程中open,子进程从父进程中获取打开的文件,此时三个共用一个文件偏移量
        
        *一个子进程中的open不会影响其他进程的使用
        
'''
fd = open(file_name,"rb")
size = os.path.getsize(file_name) // 2


# 复制文件上半部分
def upper_part():
    p1 = open("upper.jpg","wb")
    up_part = fd.read(size)
    p1.write(up_part)
    p1.close()
    fd.close()

# 复制文件下半部分
def latter_part():
    p2 = open("latter.jpg","wb")
    fd.seek(size)
    late_part = fd.read()
    p2.write(late_part)
    p2.close()
    fd.close()

p2 = Process(target=latter_part)
p1 = Process(target=upper_part)
p1.start()
p2.start()
p1.join()
p2.join()



import os
import time
import shutil
import inspect
import numpy as npy


# 获取最大为n的质数判断表和质数表
def Primes(n):
    is_prime = [True] * (n + 1)
    prime_list = []
    for i in range(2, n + 1):
        if is_prime[i]:
            prime_list.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime, prime_list


# 找到库存放的位置
def FindModulePath():
    s = r'\\'.join(os.path.dirname(__file__).split('\\'))
    return s[0].capitalize()+s[1:]


# 用来处理文件的File工具
class File:
    @staticmethod  # 静态类
    # 获取当前文件路径
    def GetPath():
        s = os.path.abspath(os.path.dirname(inspect.stack()[1].filename))
        s = r'\\'.join(s.split('\\'))
        return s[0].capitalize()+s[1:]

    # 拷贝文件
    def Copy(from_path, to_path, name=None, prefix=None, suffix=None, contain=None):
        # 如果路径不存在，抛出错误
        if not os.path.exists(from_path) or not os.path.exists(to_path):
            raise FileNotFoundError('指定路径不存在')
        # 进行拷贝
        files_copied = []  # 已拷贝的文件
        for filename in os.listdir(from_path):
            source = os.path.join(from_path, filename)
            if os.path.isfile(source):
                if (name is None or filename == name) and \
                   (prefix is None or filename.startswith(prefix)) and \
                   (suffix is None or filename.endswith(suffix)) and \
                   (contain is None or contain in filename):
                    shutil.copy(source, to_path)
                    files_copied.append(filename)
        # 输出操作结果
        if len(files_copied) == 0:
            print('没有符合条件的文件')
        else:
            print('成功拷贝以下文件到目标路径：')
            for file in files_copied:
                print(os.path.join(to_path, file))

    # 移动文件
    def Move(from_path, to_path, name=None, prefix=None, suffix=None, contain=None):
        # 如果路径不存在，抛出错误
        if not os.path.exists(from_path) or not os.path.exists(to_path):
            raise FileNotFoundError("指定路径不存在")
        # 进行移动
        files_moved = []  # 已移动的文件
        for filename in os.listdir(from_path):
            source = os.path.join(from_path, filename)

            if os.path.isfile(source):
                if (name is None or filename == name) and \
                   (prefix is None or filename.startswith(prefix)) and \
                   (suffix is None or filename.endswith(suffix)) and \
                   (contain is None or contain in filename):
                    shutil.move(source, to_path)
                    files_moved.append(filename)
        # 输出操作结果
        if len(files_moved) == 0:
            print("没有符合条件的文件")
        else:
            print("成功移动以下文件到目标路径：")
            for file in files_moved:
                print(os.path.join(to_path, file))

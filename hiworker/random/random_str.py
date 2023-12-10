import random


def random_str(num):
    # 猜猜变量名为啥叫 H
    h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(h)

    return salt

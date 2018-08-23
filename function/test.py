def count():
    fs = []
    for i in range(1, 4):
        print(">>>>>")

        def f():
            print("<<<<")
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print("==============>: ", f1(), f2(), f3())

def concatenate(*args):
    return " ".join(map(str,args))

def iterate(*args):
    for x in args:
        print(x)

def iterate_dic(**kwrags):
    for key, value in kwrags:
        print(value)
        
result = concatenate("hello", "word")
result2 = iterate("hello", 230, "word" , "error", "404")
iterate_dic(name ="hello", name2 ="world")
print(result)
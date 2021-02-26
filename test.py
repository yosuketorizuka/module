from my_module import my_funcClass

if __name__ == '__main__':
    
    ins_1 = my_funcClass.my_funcClass(2,1)
    ins_2 = my_funcClass.my_funcClass(2,1)
    
    out1 = ins_1.my_sum(2,1)
    out2 = ins_2.my_dif(2,1)

    print(out1)
    print(out2)
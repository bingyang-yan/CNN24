from yby import *

root = Path(r'E:\Data\Paper_1\Data_v3\Y_mrst')
startup = r"D:\YAN\Research\MRST\mrst-2021b\startup.m"
temp_input = r"D:\YAN\Research\Paper\Paper_1\Code\Code_v3_master\temp_08_input.m"

root = Path(root)
the_input = Y_mrst(save=False, verbose=False).get_input(startup, temp_input)

if __name__=='__main__':
    res = Y_mat2data(root, the_input, the_glob='*.mat')
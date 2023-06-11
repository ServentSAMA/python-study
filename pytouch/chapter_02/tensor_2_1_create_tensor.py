import torch

'''
创建torch中的默认张量
'''
tensor = torch.arange(12)

print(tensor)

'''
改变形状 数据预处理 
'''

tensor = torch.reshape(tensor,(3,4))

print(tensor)



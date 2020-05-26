file1 = open(r'/root/mlopstask2/program.py',"r")
code = file1.read()

if 'keras' and 'Conv2D' in code:
     print('cnn')
else:
     print('not cnn')

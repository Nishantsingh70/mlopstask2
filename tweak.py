import random
def kernel_size():
    if (int(inputs[0])) < 10:
        if (int(inputs[0])) >= 8:
            inputs[0]=str(int(inputs[0])-3)
        elif (int(inputs[0])) <= 5:
            inputs[0]=str(int(inputs[0]))
def pool_size():
    if (int(inputs[1])) < 7:
        if (int(inputs[1])) >= 5:
            inputs[1]=str(int(inputs[1])-2)
        elif (int(inputs[1])) > 2 and (int(inputs[1])) < 5:
            inputs[1]=str(int(inputs[1])-1)
        elif (int(inputs[1])) == 2:
            inputs[1]=str(int(inputs[1]))
    
def epoch():
    inputs[2]=str(int(inputs[2])+5)
def learn_rate():
    if (float(inputs[3])) > 0.00000:
        inputs[3]=str(float(inputs[3])-0.003)
    else:
        inputs[3]=str(float(inputs[3])+0.004)
def Convlayer():
    if (int(inputs[4])) < 4:
        inputs[4]=str(int(inputs[4])+1)
    else:
        inputs[4]=str(int(inputs[4]))
def fc_input():
    if (int(inputs[5])) < 4:
        inputs[5]=str(int(inputs[5])+1)
    else:
        inputs[5]=str(int(inputs[5]))
def neuron_no():
    if(int(inputs[6])) > 0:
        if(int(inputs[6])) > 400 and (int(inputs[6])) < 600:
            inputs[6]=str(int(inputs[6])-200)
        elif (int(inputs[6])) > 200 and (int(inputs[6])) < 400:
            inputs[6]=str(int(inputs[6])-120)
        else:
            inputs[6]=str(int(inputs[6])-60)
    else:
        inputs[6]=str(int(inputs[6])+50)
def option(a):        
    print(a)
    if(a == 0):
        kernel_size()
    elif(a == 1):
        pool_size()
    elif(a == 2):
        epoch()
    elif(a == 3):
        learn_rate()
    elif(a == 4):
        Convlayer()
    elif(a == 5):
        fc_input()
    elif(a == 6):
        neuron_no()
accuracy_file_new = open('/root/mlopstask2/new_accuracy.txt',"r")
new_accuracy1 = accuracy_file_new.read()
new_accuracy1 = float(new_accuracy1)
accuracy_file_old = open('/root/mlopstask2/old_accuracy.txt',"r+")
old_accuracy1 = accuracy_file_old.read()
old_accuracy1 = float(old_accuracy1)
input_file = open('/root/mlopstask2/input_file.txt', "r+")
inputs = input_file.read()
inputs = inputs.split('\n')
if(float(new_accuracy1) < 0.90000000000000):
    if(float(new_accuracy1) > float(old_accuracy1)):
        old_accuracy1 = float(new_accuracy1)
        num = random.randint(0,6)
        print(num)
        option(num)        
input_file_data = '\n'.join(inputs)
input_file.seek(0)
input_file.write(input_file_data)
input_file.close()

old_accuracy1 = str(old_accuracy1)
accuracy_file_old.seek(0)
accuracy_file_old.write(old_accuracy1)
accuracy_file_old.close()

accuracy_file_new.close()





        



        


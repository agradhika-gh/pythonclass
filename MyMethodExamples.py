def methodNoInputsNoOutPut():
    print('This method has no input or output!')


def methodInputOnly(name):
    print(f'Hello {name}!!')


def methodOutputOnly():
    x = "Method with only Output"
    print('Method with only Output!')
    return x

def method2Inputs1Output(x,y):
    print(f'Addition is {x+y}')
    return x+y

methodNoInputsNoOutPut()
methodInputOnly('Radhika')
methodOutputOnly()
method2Inputs1Output(110,220)
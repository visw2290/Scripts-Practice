def shape(symbol, height, width):
    if len(symbol)>1:
        raise Exception('Symbol should be just 1 character')
    if (height == 1) or (width ==1):
        raise Exception('Height and width should be greater than 1')
    for i in range(height - 1):
        print(symbol)
    print(symbol * width)

shape('*',5,7)


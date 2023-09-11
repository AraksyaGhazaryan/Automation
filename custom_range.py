
def customRange(startPoint, endPoint, step=1):

    if startPoint < endPoint:
        while startPoint < endPoint:
            print(startPoint)  
            startPoint += step
   


number = customRange(10, 1, )
print(number)



def customRange(startPoint, endPoint, step=1):
    
    if startPoint < endPoint:
        while startPoint < endPoint:
            yield startPoint
            startPoint += step
   

for num in customRange(1, 5):
    print(num)



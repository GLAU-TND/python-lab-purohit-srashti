class MyException(Exception):
    pass

def Xyz(a,b):
        sum=a+b
        if sum<150:
          raise MyException('Custom Exception Occured')
        else:
          print("Sum is " + str(sum))


a = int(input())
b = int(input())
Xyz(a,b)

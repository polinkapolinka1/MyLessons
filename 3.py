import random, urllib.request
num=random.randint(1,1000)
destination= str(num)+'.png'
ur1='https://www.google.com/images/srpr/logo3w.png'
urllib.request.urlretrieve(ur1, destination)
print(destination)




from django.test import TestCase

# Create your tests here.
string = "cái bánh trưng và bánh trưng"
test = "bánh trưng"
re = "<mark>" +test +"<sup>"+ str(1) +"</sup>" +"</mark> Xin chào tôi là Vũ"
x =  "xoa1"
string = string.replace(test,re)
class Error():
    def __init__(self,stt=0,loi="",goiy=[]):
        self.stt = stt
        self.loi = loi
        self.goiy = goiy
loi = ["bánh chưng" , "quả tranh"]
goiy = [["bánh chưng","chưng hửng"],["quả chanh","chanh chanh"]]
arr = []
for i in range(len(loi)):
    node = Error(i+1,loi[i],goiy[i])
    arr.append(node)

print(arr[0].stt)
print(arr[0].loi)
print(arr[0].goiy)
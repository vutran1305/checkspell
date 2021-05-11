from django.shortcuts import render
# from .models import Erro,Goiy

# Create your views here.

def home(request):
    return render(request,"base.html")

class Error():
    def __init__(self,stt=0,loi="",goiy=[]):
        self.stt = stt
        self.loi = loi
        self.goiy = goiy
def error(request):

    if request.method == 'GET':
        loi = ["bánh chưng", "quả tranh"]
        goiy = [["bánh chưng", "chưng hửng"], ["quả chanh", "chanh chanh"]]
        arr = []
        for i in range(len(loi)):
            error = loi[i]
            node = Error(i + 1, error, goiy[i])
            arr.append(node)

        # searchtext = request.GET.get('search', None)
        # string = "tôi có 1 cái bánh trưng và bánh trưng"
        # error = "bánh trưng"
        # re = "<mark>" + error + "<sup>" + str(1) + "</sup>" + "</mark>"
        # goiy = ["bánh chưng" , "chưng cất" ,"bánh cưng"]
        # string = string.replace(error, re)
        context = { "arr":arr}
        return  render(request,"error.html",context)

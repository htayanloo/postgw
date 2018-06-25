import urllib.request

from hyperlink._url import unicode


class PostGateway:
    def __init__(self,username,password):
        self.username = username
        self.password = password


    def Run_url(self, url):


        try:
            url = str(url)
            temp = urllib.request.urlopen(url).read()

        except:
            return 'F-Connection'
        else:
            return temp

    def Getprice(self, Weight, Price, Shcode, State, City, Tip, Cod, Showtype):
        url = 'http://gateway.post.ir/Gateway/Price.asp?Username=&Password=&Weight='+str(Weight)+'&Price='+str(Price)+'&Shcode='+str(Shcode)+'&State='+str(State)+'&City='+str(City)+'&Tip='+str(Tip)+'&Cod='+str(Cod)+'&Showtype='+str(Showtype)+''

        temp = self.Run_url(url)

        return temp



    def Register(self, Shcode, Id, State, City, Pname, Weight, Cod, Price, Send, Name, Address, Email, Tel, Pcode):
        Pname = Pname.encode("utf8","ignore")
        Name = Name.encode("utf8","ignore")
        Address = Address.encode("utf8","ignore")
        url = 'http://gateway.post.ir/Gateway/?Username='+str(self.username)+'&Password='+str(self.password)+'&Shcode='+str(Shcode)+'&Id='+str(Id)+'&State='+str(State)+'&City='+str(City)+'&Pname='+str(Pname)+'&Weight='+str(Weight)+'&Cod='+str(Cod)+'&Price='+str(Price)+'&Send='+str(Send)+'&Name='+str(Name)+'&Address='+str(Address)+'&Email='+str(Email)+'&Tel='+str(Tel)+'&Pcode='+str(Pcode)+'&Ordertip=0&Showtype=0'
        unicode(url, encoding='utf-8')
        temp = self.Run_url(url=url)
        return  temp

    def Register_Bulk(self, data):
        url = "http://gateway.post.ir/Gateway/RegisterBulk.asp"

    def Change(self,Id,Status):
        url = "http://gateway.post.ir/Gateway/Change.asp?Username="+self.username+"&Password="+self.password+"&Id="+str(Id)+"&Status="+str(Status)+""

        temp = self.Run_url(url)
        return temp

    def Ping(self,o_id):
        url = "http://gateway.post.ir/Gateway/Ping.asp?Username="+self.username+"&Password="+self.password+"&Id="+str(o_id)+""
        temp = self.Run_url(url=url)
        return temp

    def Edit(self, Id, Pname, Weight, Cod, Price, Name, Address, Email, Tel, Pcode):
        Pname = Pname.encode("utf8","ignore")
        Name = Name.encode("utf8","ignore")
        Address = Address.encode("utf8","ignore")
        url = 'http://gateway.post.ir/Gateway/Edit.asp?Username='+str(self.username)+'&Password='+str(self.password)+'&Id='+str(Id)+'&Pname='+str(Pname)+'&Weight='+str(Weight)+'&Cod='+str(Cod)+'&Price='+str(Price)+'&Name='+str(Name)+'&Address='+str(Address)+'&Email='+str(Email)+'&Tel='+str(Tel)+'&Pcode='+str(Pcode)+'&Showtype=1'
        unicode(url, encoding='utf-8')
        temp = self.Run_url(url=url)
        return temp

    def Dayping(self,Changedate,Lid,Number):
        url = "http://gateway.post.ir/Gateway/Dayping.asp?Username="+self.username+"&Password="+self.password+"&Changedate="+str(Changedate)+"&Lid="+Lid+"&Number="+Number+""
        temp = self.Run_url(url=url)

        return temp
    def Billing(self,Min,Max):
        url = "http://gateway.post.ir/Gateway/Billing.asp?Username="+self.username+"&Password="+self.password+"&Min="+str(Min)+"&Max="+str(Max)+""
        temp = self.Run_url(url=url)

        return temp
    def Billing2(self,Id,Tip,page=1):
        url = "http://gateway.post.ir/Gateway/Billing2.asp?Username="+self.username+"&Password="+self.password+"&Id="+str(Id)+"&Tip="+str(Tip)+"&page="+str(page)+""
        temp = self.Run_url(url=url)
        return temp


import urllib.request









class PostGW(object):
    _username = None
    _password = None


    def __init__(self,username,password):
        self._username = username
        self._password = password

    def Resolve_Error(self,value):
        ErrorDic = {
            1:"اطلاعات درخواستی ناقص میباشد.",
            3:"امکان تغییر وضعیت این سفارش وجود ندارد.",
            101:"کد پستی وارد شده معتبر نمیباشد.",
            401:"خطا در اطلاعات شناسایی ) نام کاربري ، Api Password ( و یا Ip سرور",
            402:"خطا در شناسایی نام کاربري فروشنده",
            403:"فروشنده مورد نظر منقضی و یا مسدود شده است.",
            404:"درخواست / شناسه مورد نظر یافت نشد.",
            405:"امکان استفاده از این سرویس ارسال براي این فروشگاه امکان پذیر نمیباشد.",
            502:"خطا در شناسایی کد استان / شهرستان ارسال شده",
            503:"امکان ارسال مرسوله براي این مقصد میسر نمیباشد",
            505:"شناسه سفارش ارسال شده توسط شما تکراري میباشد",
            600:"این درخواست قبلا ثبت شده است.",
            601:"تغییر وضعیتی براي نمایش وجود ندارد",
            800:"String تولید شده براي ثبت سفارش معتبر نمیباشد.",
            801:"تعداد سفارش ارسالی بیشتر از حد مجاز میباشد. ) متد New Order (",
            802:"روش ارسال / سرویس درخواستی نامعتبر میباشد",
            803:"روش پرداخت درخواستی نامعتبر میباشد.",
            804:"پارامترهاي الزامی به سامانه ارسال نگردیده است.",
            805:"وزن ارسال شده نامعتبر میباشد.",
            806:"قیمت ارسال شده براي سفارش نامعتبر میباشد.",
            807:"مالیات بر ارزش افزوده ارسال شده نامعتبر میباشد.",
            808:"مالیات بر ارزش افزوده ارسال شده نامعتبر میباشد.",
            900:"تعداد سفارش ارسالی بیشتر از حد مجاز میباشد",
            999:"مقدار بازگشتی از پست معتبر نمیباشد"
            }
        try:
            value = int(value)
        except:
            return {"code":999,"message":ErrorDic[999]}

        if value in ErrorDic:
            return {"code":value,"message":ErrorDic[value]}
        else:
            return None

    def _get_url(self, url):


        try:
            url = str(url)
            temp = urllib.request.urlopen(url).read()

        except:
            return 'F-Connection'
        else:
            return temp


    def Getprice(self, Weight, Price, Shcode, State, City, Tip, Cod, Showtype):
        """
        Get Price with detail of Order
        :param Weight:
        :param Price:
        :param Shcode:
        :param State:
        :param City:
        :param Tip:
        :param Cod:
        :param Showtype:
        :return: 2 type   if ShowType is 0   result is send price else ShowType is 1  result is 3 section
        """
        url = 'http://gateway.post.ir/Gateway/Price.asp?Username=&Password=&Weight='+str(Weight)+'&Price='+str(Price)+'&Shcode='+str(Shcode)+'&State='+str(State)+'&City='+str(City)+'&Tip='+str(Tip)+'&Cod='+str(Cod)+'&Showtype='+str(Showtype)+''
        temp = self._get_url(url).decode('utf-8')

        temp = str(temp).split(';')
        temp_clear = self.Resolve_Error(temp[0])

        if temp_clear:
            return temp_clear
        else:
            if Showtype == 1:
                if len(temp) == 3:

                    return {'send_price':temp[0],'send_price_negative':temp[1],"tax":temp[2]}
                else:
                    return self.Resolve_Error(999)

            else:
                try:
                    result = int(temp)
                except:
                    return self.Resolve_Error(999)
                else:
                    return result



    def Register(self, Shcode, Id, State, City, Pname, Weight, Cod, Price, Send, Name, Address, Email, Tel, Pcode):
        Pname = Pname.encode("utf8","ignore")
        Name = Name.encode("utf8","ignore")
        Address = Address.encode("utf8","ignore")
        url = 'http://gateway.post.ir/Gateway/?Username='+str(self.username)+'&Password='+str(self.password)+'&Shcode='+str(Shcode)+'&Id='+str(Id)+'&State='+str(State)+'&City='+str(City)+'&Pname='+str(Pname)+'&Weight='+str(Weight)+'&Cod='+str(Cod)+'&Price='+str(Price)+'&Send='+str(Send)+'&Name='+str(Name)+'&Address='+str(Address)+'&Email='+str(Email)+'&Tel='+str(Tel)+'&Pcode='+str(Pcode)+'&Ordertip=0&Showtype=0'
        unicode(url, encoding='utf-8')
        temp = self.Run_url(url=url)
        return  temp
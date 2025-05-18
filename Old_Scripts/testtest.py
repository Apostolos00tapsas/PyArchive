#import urllib2, urllib
#mydata=[('email','admin'),('pass','admin2')]    #The first is the var name the second is the value
#mydata=urllib.urlencode(mydata)
#path='http://data.heartbit.gr/datadoclogin.php'    #the url you want to POST to
#req=urllib2.Request(path, mydata)
#req.add_header("Content-type", "application/x-www-form-urlencoded")
#page=urllib2.urlopen(req).read()
#a = page

#print a


def dis(val,num):
    if val==0:
        return num
    else:
        num=num+1
        print(num)
        return dis(val-1,num)


dis(10,2)

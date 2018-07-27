def myhentaicomic(num,c):
    try:
        ep,fmt = num.split(" ")
    except:
        ep = num
        fmt = "jpg"
        
    if int(ep) < 10:
        ep = "00"+ep
    elif int(ep) < 100:
        ep = "0"+ep
    if c == "3":
        url = "http://myhentaicomics.com/var/thumbs/Buu%27s%20Bodies%202/"+ep+"."+fmt
    elif c == "4":
        url = "http://myhentaicomics.com/var/thumbs/Milf%20Catchers/"+ep+"."+fmt
    elif c == "5":
        url = "http://myhentaicomics.com/index.php/Dexmom/"+ep+"."+fmt
    elif c == "6":
        url = "http://myhentaicomics.com/var/thumbs/Breaking%20The%20Rules%201/"+ep+"."+fmt
    elif c == "7":
        url = "http://myhentaicomics.com/var/thumbs/Breaking%20The%20Rules%202/"+ep+"."+fmt
    elif c == "8":
        url = "http://myhentaicomics.com/var/thumbs/Breaking%20The%20Rules%203/"+ep+"."+fmt
    elif c == "9":
        url = "http://myhentaicomics.com/var/thumbs/Breaking%20The%20Rules%204/"+ep+"."+fmt
    return url

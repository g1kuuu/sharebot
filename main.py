import ssl ,os ,requests ,time #:1
from threading import active_count ,Thread #:2
from pystyle import Colorate ,Colors ,Write #:3
from random import randint ,choice #:4
from urllib3 .exceptions import InsecureRequestWarning #:5
from http import cookiejar #:6
from Data .UserAgent import UserAgent #:7
from Data .Lists import DeviceTypes ,Platforms ,Channel ,ApiDomain #:8
import colorama #:9
class BlockCookies (cookiejar .CookiePolicy ):#:12
    return_ok =set_ok =domain_return_ok =path_return_ok =lambda OO0OO000OO00OO00O ,*OOOOOOO0OOO0O0OOO ,**OO0OO00O0OO000O0O :False #:13
    netscape =True #:14
    rfc2965 =hide_cookie2 =False #:15
requests .packages .urllib3 .disable_warnings (category =InsecureRequestWarning )#:18
ssl ._create_default_https_context =ssl ._create_unverified_context #:19
r =requests .Session ()#:20
ThreadCount =0 #:21
TotalSendedShare =0 #:22
TotalFailedReq =0 #:23
DebugMode =False #:24
r .cookies .set_policy (BlockCookies ())#:26
def Clear ():#:29
    if os .name =='posix':#:30
        os .system ('clear')#:31
    elif os .name in ('ce','nt','dos'):#:32
        os .system ('cls')#:33
    else :#:34
        pass #:35
def Title (OO000O0OO0O000OO0 ):#:38
    global DebugMode #:39
    if os .name in ('posix','ce','dos'):#:40
        pass #:41
    elif os .name =='nt':#:42
        os .system (f"title {OO000O0OO0O000OO0}")#:43
        return False #:44
    else :#:45
        pass #:46
def ReadFile (OOOO0OOOOO0000000 ,OOO00OOOOOO00O0OO ):#:49
    with open (OOOO0OOOOO0000000 ,OOO00OOOOOO00O0OO ,encoding ='utf8')as O0OO00000O0O00000 :#:50
        O00000O0OOOO00O0O =[OOOO0O00O00OOO0OO .strip ('\n')for OOOO0O00O00OOO0OO in O0OO00000O0O00000 ]#:51
        return O00000O0OOOO00O0O #:52
def SendView (OOOO0O0O00O0000OO ):#:55
    global TotalSendedShare ,TotalFailedReq ,DebugMode #:56
    O0O00O0O0000OO0O0 =choice (Platforms )#:57
    OO000O0OOO000O00O =randint (1 ,12 )#:58
    O0OO0000OO00OOO0O =choice (DeviceTypes )#:59
    O0OOO000O0O0OO0OO ={"content-type":"application/x-www-form-urlencoded; charset=UTF-8","user-agent":choice (UserAgent )}#:63
    O000O0000O00OO0OO =choice (["tiktok_web","musically_go"])#:64
    OO0O00OO0000O0OO0 =randint (1000000000000000000 ,9999999999999999999 )#:65
    O0O0OO0O000000OOO =choice (ApiDomain )#:66
    O000000OO000000OO =choice (Channel )#:67
    OO0O00O000000O0O0 =f"https://{O0O0OO0O000000OOO}/aweme/v1/aweme/stats/?channel={O000000OO000000OO}&device_type={O0OO0000OO00OOO0O}&device_id={OO0O00OO0000O0OO0}&os_version={OO000O0OOO000O00O}&version_code=220400&app_name={O000O0000O00OO0OO}&device_platform={O0O00O0O0000OO0O0}&aid=1988"#:68
    OOOOO0O000O00000O =f"item_id={OOOO0O0O00O0000OO}&share_delta=1"#:69
    try :#:71
        OOO0OO00OO0000000 =r .post (OO0O00O000000O0O0 ,headers =O0OOO000O0O0OO0OO ,data =OOOOO0O000O00000O ,stream =True ,verify =False )#:72
        try :#:73
            if (OOO0OO00OO0000000 .json ()["status_code"]==0 ):#:74
                O0OOO0O0000OO00O0 =OOO0OO00OO0000000 .json ()["log_pb"]["impr_id"]#:75
                TotalSendedShare +=1 #:76
                if DebugMode ==True :#:77
                    print (Colorate .Horizontal (Colors .blue_to_green ,f"Sent Share: {TotalSendedShare} ({O0OOO0O0000OO00O0})"))#:78
                else :#:79
                    print (Colorate .Horizontal (Colors .blue_to_green ,f"Sent Share: {TotalSendedShare} ({O0OOO0O0000OO00O0})"))#:80
                    Title (f"Thread :{str(active_count() - 1)} / Hit :{TotalSendedShare} / Fail :{TotalFailedReq}")#:81
            else :#:82
                pass #:83
        except :#:84
            TotalFailedReq +=1 #:85
            Title (f"Thread :{str(active_count() - 1)} / Hit :{TotalSendedShare} / Fail :{TotalFailedReq}")#:86
    except :#:87
        pass #:88
def ClearURI (O00OO0O0000O0000O ):#:91
    if ("vm.tiktok.com"in itemID or "vt.tiktok.com"in itemID ):#:92
        return r .head (itemID ,stream =True ,verify =False ,allow_redirects =True ,timeout =5 ).url .split ("/")[5 ].split ("?",1 )[0 ]#:94
    else :#:95
        return itemID .split ("/")[5 ].split ("?",1 )[0 ]#:96
if (__name__ =="__main__"):#:99
    Clear ()#:100
    print ("""
          


              

░██████╗░░░███╗░░██╗░░██╗██╗░░░██╗
██╔════╝░░████║░░██║░██╔╝██║░░░██║
██║░░██╗░██╔██║░░█████═╝░██║░░░██║
██║░░╚██╗╚═╝██║░░██╔═██╗░██║░░░██║
╚██████╔╝███████╗██║░╚██╗╚██████╔╝
░╚═════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░
  Share Bot V1 - g1ku#0955
           https://discord.gg/RUNesnhj3F
    """)#:118
    itemID =Write .Input (" « Video Link »  ",Colors .blue ,interval =0.0001 )#:120
    amount =Write .Input (" « Amount (0-inf) »  ",Colors .yellow ,interval =0.0001 )#:121
    NThread =500
    itemID =ClearURI (itemID )
    if (int (amount )==0 ):
        while True :
            Run =True
            while Run :
                if (active_count ()<=int (NThread )):
                    Thread (target =(SendView ),args =(itemID ,)).start ()
    else :
        for _ in range (int (amount )):
            if (active_count ()<=int (NThread )):
                Thread (target =(SendView ),args =(itemID ,)).start ()
  #hey, why are you looking down here?
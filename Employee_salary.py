bs=float(input("enter the basic salary:"))
if(bs<10000):
    ts=bs+(0.2)*bs+0.8*bs
    print(ts)
if(bs>10000 and bs<=20000):
    ts=bs+bs*0.25+bs*0.85
    print(ts)
if(bs>20000):
    ts=bs+bs*0.3+bs*0.95
    print(ts)

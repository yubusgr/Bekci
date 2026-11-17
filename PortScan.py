import socket





def oncescan(targeth, targetp):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        s.settimeout(1.0)
        a = s.connect((targeth, targetp))
        return "acik"
        
    except ConnectionRefusedError as e:
        return "kapali"
    
    except TimeoutError as t:
        return "zamanasimi"
    
    except Exception as e:
        print(e)
        return "hata"

    finally:
        s.close()

def servisbul(port):
    try:
        servisadi = socket.getservbyport(port)
        return servisadi 
    except OSError:
        return "Bilinmeyen Servis"


def portscanner(targethost, targetport): 
    sonuclar = {
        "acik": [],
        "kapali": [],
        "zamanasimi": []
    }
    for port in targetport: 
       i = oncescan(targethost, port)
       if i == "acik":
            servis = servisbul(port)
            sonuclar["acik"].append([port, servis])
       elif i == "kapali":
            sonuclar["kapali"].append(port)
       elif i == "zamanasimi":
           sonuclar["zamanasimi"].append(port)
    return sonuclar


scan = portscanner("192.168.1.102", (21,22,80,443,5050,6060,8080))

print(scan["acik"])
print(scan["kapali"])
print(scan["zamanasimi"])

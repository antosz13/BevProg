import urllib.request
import json

def main():
    response = urllib.request.urlopen('https://jsonip.com/')
    raw = response.read()
    txt = raw.decode("utf-8")
    d = json.loads(txt)
    print(d['ip'])
    
if __name__ == "__main__":
    main()
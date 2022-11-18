import json

def main():
    d = { 
            "name": "Antosz",
            "age": 19,
            "favcolour": "blue"
        }
    
    
    
    f = open("jsonki.json", "w")
    json.dump(d, f, indent=2)
    f.close()
    
    #f2 = 
    jsontxt = json.dumps(d)
    print(jsontxt, file=f2)
    f.close()
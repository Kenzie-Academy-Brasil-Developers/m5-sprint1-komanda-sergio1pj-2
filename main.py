from utils import json_handler
def main():
    print(json_handler.write_json("menu.json", {"name": "CHURROS DO M5", "price": 5}))
    print(json_handler.read_json("menu.json"))
if __name__ == "__main__":
    main()
    
    


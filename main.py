from datetime import datetime

def main():
    today = datetime.now()
     iso = today.isoformat()
      dt = iso[:-7] + '+00:00'
      print(dt)

if __name__ == "__main__":
    main()
    

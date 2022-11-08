from datetime import datetime

today = datetime.now()
iso = today.isoformat()
dt = iso[:-7] + '+00:00'
print(dt)

from datetime import date, datetime, timedelta

d = date.today()                    # 2025-01-24
dt = datetime.today()               # 2025-01-24 15:20:07.404041

# timedelta
delta = timedelta(days=5)
date_finale = d - delta             # 2025-01-19

# strftime
date_str = d.strftime("%d %b %Y")   # 24 Jan 2025
# il existe apparement strptime qui fait l'inverse
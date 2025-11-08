import time
from datetime import datetime

current_time = time.time()

formatted_time = f"{current_time:,.4f} or {current_time:.2e} \
in scientific notation"

current_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_time}")
print(f"{current_date}")

import requests
from datetime import datetime, timedelta

url_template = "https://simurg.space/gen_file?data=obs&date={date}"

day_offset = 1
while True:
  yesterday = datetime.now() - timedelta(days=day_offset)
  url = url_template.format(date=yesterday.strftime("%Y-%m-%d"))
  
  print(f'Working with URL: {url}')
  
  response = requests.get(url, stream=True)
  if response.status_code == 200:
    print(f"Data are available for {yesterday}")
    break
  else:
    print(f"Failed to get data for {yesterday}")
    day_offset = day_offset + 1

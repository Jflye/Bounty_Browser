import time
from selenium import webdriver

# --- Opens YwH ---
print("---Yes We Hack = Loaded!")
browser = webdriver.Chrome('PATH to where you installed chrome driver')
driver = webdriver.Chrome('PATH to chrome driver')
driver.get('https://yeswehack.com/programs')
time.sleep(10)

print('')
print('Moving on to HackerOne...')
print('')

# --- Opens HackerOne in new tab ---
print('')
print('---HackerOne = Loaded!')
driver.get('https://hackerone.com/directory/programs')
time.sleep(10)
print('')
print('Moving on to Bugcrowd...')
print('')

# --- Opens Bugcrowd in new tab ---
print('')
print('---Bugcrowd = Loaded!')
driver.get('https://bugcrowd.com/programs')
time.sleep(10)
print('')
print('Complete!')
driver.quit()

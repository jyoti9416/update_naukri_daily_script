# import selenium and time library  
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
 
#open firefox browser with naukri login url 
browser = webdriver.chrome()
try:
  browser.get('https://www.naukri.com/mnjuser/homepage')
  time.sleep(10) 
except error as e:
  print(e)
else:
  browser.get('https://www.naukri.com/nlogin/login') 
  time.sleep(10)
  #get username and password 
  emailElem = browser.find_element_by_id('usernameField') 
  emailElem.send_keys(<username>) 
  passwordElem = browser.find_element_by_id('passwordField') 
  passwordElem.send_keys(<password>) 
  passwordElem.submit() 
  time.sleep(5) 
 
#go to main profile page  
browser.get('https://www.naukri.com/mnjuser/profile?id=&orgn=homepage') 
time.sleep(5) 
 
# find the resume headline and edit it 
browser.find_element_by_css_selector('.resumeHeadline > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)').click() 
resume_headline_update = browser.find_element_by_id('resumeHeadlineTxt') 
resume_headline_update.clear() 
resume_headline_update.send_keys('Python and shell script developer looking for oppurtunities in Data Science and Machine Learning with 2.5 years of experience overall.') 
browser.find_element_by_css_selector('form.s12 > div:nth-child(3) > div:nth-child(1) > button:nth-child(2)').click() 

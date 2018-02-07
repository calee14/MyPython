from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# imitates a web browser
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

class MVCodeBot(object):
	def __init__(self):
		self.driver = webdriver.PhantomJS()
	def connect(self):
		driver = self.driver
		driver.get("https://www.mvcodeclub.com/users/sign_in")

		driver.implicitly_wait(1) # wait 1 seconds
		print("Successfully connected to the sign in page.")
	def login(self):
		driver = self.driver
		username = driver.find_element_by_id("user_login")
		password = driver.find_element_by_id("user_password")

		username.send_keys("cap1")
		password.send_keys("65X6a86G")
		
		driver.find_element_by_name("commit").click()
		print("Successfully logged in.")
	def logout(self):
		driver = self.driver
		signout = driver.find_element_by_class_name('intercom-shutdown')
		driver.execute_script("return arguments[0].scrollIntoView(true);", signout)
		signout.click()
		print("Successfully logged out.")
		self.connect()
	def incrementallogin(self):
		minute = 60
		hour = minute * 60
		time = 5
		while True:
			sleep(time) # sleep uses seconds
			print("Time is %s") % (time)
			self.login()
			self.logout()
			time *= 2
	def close(self):
		self.driver.close()
		print("Closed window.")
	def run(self):
		self.connect()
		self.incrementallogin()
		self.close()
bot = MVCodeBot()
bot.run()
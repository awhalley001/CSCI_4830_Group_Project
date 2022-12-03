# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestChangePages():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_changePages(self):
    self.driver.get("http://ec2-54-91-175-209.compute-1.amazonaws.com:8000/yard_capacity/home/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Home Page"
    self.driver.find_element(By.LINK_TEXT, "Yard").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Yard Table"
    self.driver.find_element(By.LINK_TEXT, "Create").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Car Table"
  
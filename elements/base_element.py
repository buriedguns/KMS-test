from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement:
	def __init__(self, session, locator):
		self.session: Chrome = session
		self.locator = locator

	def web_element(self):
		WebDriverWait(self.session, 15).until(ec.presence_of_element_located(self.locator))
		return self.session.find_element(*self.locator)

	def get_link(self):
		return self.web_element().get_attribute('href')

	def get_text(self):
		text = self.web_element().text
		if not text:
			text = self.web_element().get_attribute("innerText")
		if not text:
			text = self.web_element().get_attribute("textContent")
		if not text:
			text = self.web_element().get_attribute("value")
		if text:
			return text.strip()
		return None

from .base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Button(BaseElement):

	def __init__(self, session, locator):
		super().__init__(session=session, locator=locator)

	def click(self):
		WebDriverWait(self.session, 15).until(ec.element_to_be_clickable(self.locator))
		self.web_element().click()

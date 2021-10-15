from .base_element import BaseElement


class Input(BaseElement):
	def __init__(self, session, locator):
		super().__init__(session=session, locator=locator)

	def clear(self):
		self.web_element().clear()

	def clear_and_send_keys(self, text):
		if text:
			self.clear()
			self.web_element().send_keys(text)

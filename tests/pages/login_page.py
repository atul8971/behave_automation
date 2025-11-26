class LoginPage:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.email_text_box = "#username"
        self.password_text_box = "#password"
        self.sign_in_button = "//input[@value='Sign In']"

    def login(self, username, password):
        """Login to the application using provided credentials"""
        try:
            self.logger.info("Attempting to fill username field")
            self.page.locator(self.email_text_box).click()
            self.page.locator(self.email_text_box).fill(username)
            self.logger.debug(f"Username field filled with: {username}")

            self.logger.info("Attempting to fill password field")
            self.page.locator(self.password_text_box).click()
            self.page.locator(self.password_text_box).fill(password)
            self.logger.debug("Password field filled")

            self.logger.info("Clicking sign in button")
            self.page.locator(self.sign_in_button).click()
            self.logger.info("Sign in button clicked successfully")
        except Exception as e:
            self.logger.error(f"Error during login page interaction: {str(e)}")
            raise

    def register(self, username, password):
        """Login to the application using provided credentials"""
        try:
            self.logger.info("Attempting to fill username field")
            self.page.locator(self.email_text_box).click()
            self.page.locator(self.email_text_box).fill(username)
            self.logger.debug(f"Username field filled with: {username}")

            self.logger.info("Attempting to fill password field")
            self.page.locator(self.password_text_box).click()
            self.page.locator(self.password_text_box).fill(password)
            self.logger.debug("Password field filled")

            self.logger.info("Clicking sign in button")
            self.page.locator(self.sign_in_button).click()
            self.logger.info("Sign in button clicked successfully")
        except Exception as e:
            self.logger.error(f"Error during login page interaction: {str(e)}")
            raise
from tests.pages.login_page import LoginPage
class LoginActions:
    def __init__(self, context):
        self.context = context
        self.login_page = LoginPage(page=self.context.page, logger=self.context.logger)
    
    def perform_login(self, username, password):
        """
        Performs login operation with given credentials
        Args:
            username: User's email/username
            password: User's password
        """
        self.context.logger.info(f"Starting login process for user: {username}")
        self.context.logger.debug("Initializing login operation with LoginPage")
        try:
            self.login_page.login(username, password)
            self.context.logger.info("Login operation completed successfully")
            self.context.logger.debug("Login workflow completed, page should be ready")
        except Exception as e:
            self.context.logger.error(f"Login failed: {str(e)}")
            raise
    

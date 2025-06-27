from playwright.sync_api import sync_playwright
from tests.utils.logger_utils import setup_logger


def before_all(context):
    """Initialize logger before all tests"""
    context.logger = setup_logger()

def before_scenario(context, scenario):
    context.logger.info(f"Starting scenario: {scenario.name}")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(args=['--start-maximized'], headless=False)
    context.pw_context = context.browser.new_context()
    context.page = context.pw_context.new_page()
    context.page.goto(context.config.userdata.get("url"))


def after_scenario(context, scenario):
    context.logger.info(f"Completed scenario: {scenario.name}")
    if hasattr(context, 'page'):
        context.page.close()
    if hasattr(context, 'pw_context'):
        context.pw_context.close()
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()
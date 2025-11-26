from behave import *
from tests.actions.login_actions import LoginActions

@then(u'Loign to application using "{username}" and "{password}"')
def login_to_application(context, username, password):
    LoginActions(context=context).perform_login(username=username,
                                                  password=password)

@then(u'Loign to application using "{username}" and "{password}"')
def register_to_application(context, username, password):
    LoginActions(context=context).perform_login(username=username,
                                                  password=password)
    
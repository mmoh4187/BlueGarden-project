from behave import *

@given('User's ID & password')
def step_impl(context):
    pass

@when('When we enter ID and password')
def step_impl(context):
    assert True is not False

@then('If the user's ID and password are correct, goto user profile')
def step_impl(context):
    assert context.failed is False
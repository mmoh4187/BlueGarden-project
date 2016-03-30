from lettuce import *
import mechanize
import os.path

@step('my name is "(.*)"')
def set_my_name(step, name):
    # save our name for subsequent steps
    world.reg_name = name

@step('I am on the registration page')
def on_reg_page(step):
    world.br = mechanize.Browser()
    # open login.html in the parent dir
    world.br.open('file://%s' % os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'signup.html')))
    # world.br is now primed for subsequent steps

@given('User name, email and password.')
def fill_out_form(step):
    # save our name for subsequent steps to use
    world.reg_name = 'Rutherford'

    # interact with the form and submit
    world.br.select_form(nr=0)
    world.br.form['username'] = world.reg_name
    world.br.form['password'] = 'hello'
    world.br.submit()

@when('the user name, email and password are valid.')
def should_be_on_profile(step):
    # depends on world.br being seeded
    assert 'UserHome.html' in world.br.geturl()

@then('The system successfully registers the user.')
def should_see_my_name(step):
    # depends on world.reg_name and world.br being seeded
    assert world.reg_name in world.br.response().read()
    world.br.response().seek(0)
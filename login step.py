from behave import given, when, then


@given('User name and password.')
def step(context):
    from django.conf import settings
    settings.configure()
	from django.contrib.auth.models import User
    u = User(username='foo', email='foo@example.com')
    u.set_password('bar')
    u.save()


@when('The user name and password are correct.')
def step(context):
    br = context.browser
    br.open(context.browser_url('/account/login/'))
    br.select_form(nr=0)
    br.form['username'] = 'foo'
    br.form['password'] = 'bar'
    br.submit()


@then('The user successfully logs into the system.')
def step(context):
    br = context.browser
    response = br.response()
    assert response.code == 200
    assert br.geturl().endswith('/account/'), br.geturl()


@then('The system shows a welcome message.')
def step(context):
    # Remember, context.parse_soup() parses the current response in
    # the mechanize browser.
    soup = context.parse_soup()
    msg = str(soup.findAll('h2', attrs={'class': 'welcome'})[0])
    assert "Welcome, foo!" in msg
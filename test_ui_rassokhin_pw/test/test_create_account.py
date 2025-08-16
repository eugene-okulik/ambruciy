def test_create_new_account(create_account):
    data = {
        "first name": 'Джонни',
        "last name": 'Депп',
        "password": 'Qwerty123',
        "confirm_password": 'Qwerty123',

    }
    email = create_account.create_fake_email()
    create_account.open_page()
    create_account.accept_cookie()
    create_account.user_registration(
        data["first name"],
        data["last name"],
        email,
        data["password"],
        data["confirm_password"]
    )
    create_account.check_registration(
        'Thank you for registering with Main Website Store.')
    create_account.check_account_information(create_name=f'{data["first name"]} {data["last name"]}',
                                             create_email=email)


def test_create_new_account_with_registered_email(create_account):
    data = {
        "first name": 'Test',
        "last name": 'Test',
        "email": "Test@mail.ru",
        "password": 'Qwerty123',
        "confirm_password": 'Qwerty123',

    }
    create_account.open_page()
    create_account.accept_cookie()
    create_account.user_registration(
        data["first name"],
        data["last name"],
        data["email"],
        data["password"],
        data["confirm_password"]
    )
    create_account.check_registration(
        'There is already an account with this email address. '
        'If you are sure that it is your email address, '
        'click here to get your password and access your account.')


def test_create_new_account_with_different_password(create_account):
    data = {
        "first name": 'Бред',
        "last name": 'Питт',
        "password": 'Qwerty123',
        "confirm_password": 'Qwerty456',

    }
    email = create_account.create_fake_email()
    create_account.open_page()
    create_account.accept_cookie()
    create_account.user_registration(
        data["first name"],
        data["last name"],
        email,
        data["password"],
        data["confirm_password"]
    )
    create_account.check_error_with_different_passwords('Please enter the same value again.')

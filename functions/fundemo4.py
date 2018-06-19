def details(**params):
    print(params.get('name', 'No name'))
    print(params.get('email', 'No email'))
    print(params.get('mobile', 'No mobile'))


details(name='Abc', email='abc@gmail.com')

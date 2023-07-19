def strength(password):
    result = {}
    length = len(password) >= 8
    upper = False
    digit = False

    for i in password:
        if i.isupper():
            upper = True

    for i in password:
        if i.isdigit():
            digit = True

    result['length'] = length
    result['upper'] = upper
    result['digit'] = digit

    if all(result.values()):
        return 'Strong Password'
    else:
        return 'Weak Password'

print(strength('aaaaaaaaaaa'))

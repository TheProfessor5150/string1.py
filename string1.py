def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    else:
        return f'Number of donuts: {count}'

# Examples
print(donuts(5))   # Output: Number of donuts: 5
print(donuts(23))  # Output: Number of donuts: many

def both_ends(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]

# Examples
print(both_ends('spring'))  # Output: spng
print(both_ends('a'))       # Output: (empty string)
print(both_ends('hello'))   # Output: helo

def fix_start(s):
    if len(s) == 0:
        return s
    first_char = s[0]
    modified_string = first_char + s[1:].replace(first_char, '*')
    return modified_string

# Examples
print(fix_start('babble'))  # Output: ba**le
print(fix_start('aardvark'))  # Output: a*rdv*rk
print(fix_start('google'))  # Output: goo*le

def mix_up(a, b):
    if len(a) < 2 or len(b) < 2:
        return ''
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return f'{new_a} {new_b}'

# Examples
print(mix_up('mix', 'pod'))    # Output: pox mid
print(mix_up('dog', 'dinner')) # Output: dig donner
print(mix_up('gnome', 'house')) # Output: honme gouse
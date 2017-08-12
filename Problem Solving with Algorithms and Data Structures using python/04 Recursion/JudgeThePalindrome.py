# coding:utf-8


# Judge the Palindrome
def palindrome(n_string):
    if len(n_string) == 1:
        return True
    elif n_string[0].lower() == n_string[-1].lower():
        palindrome(n_string[1:-2])
        return True
    else:
        return False


b = 'kayak'
c = 'aibohphobia'
d = 'Live not on evil'
e = 'Reviled did I live, said I, as evil I did deliv'
f = 'Go hang a salami; I’m a lasagna hog.'
g = 'Able was I ere I saw Elba'
h = 'Kanakanak – a town in Alaska'
l = 'Wassamassaw – a town in South Dakota'
print palindrome(b)
print palindrome(c)
print palindrome(d)
print palindrome(e)
print palindrome(f)
print palindrome(g)
print palindrome(h)
print palindrome(l)



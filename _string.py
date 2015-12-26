# note: you should not contain a string.py in the same directory
import string
def main():
    print ("ascii_letters: %s" % string.ascii_letters)
    print ("ascii_lowercase: %s" % string.ascii_lowercase)
    print ("ascii_lowercase: %s" % string.ascii_uppercase)
    print ("digits: %s" % string.digits)
    print ("hexdigits: %s" % string.hexdigits)
    print ("octdigits: %s" % string.octdigits)
    print ("punctuation: %s" % string.punctuation)
    print ("printable: %s" % string.printable)
    print ("whitespace: %s" % string.whitespace)
    # non-destructive
    s = "abcDEF!@#123 ."
    print ("origin: %s" % s)
    print ("lower: %s" % s.lower())
    print ("upper: %s" % s.upper())

    # destructive
    print ("origin: %s" % s)
    # s[1] = 'x'    # immutable
if __name__ == '__main__':
    main()
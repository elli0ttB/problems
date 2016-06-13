def test(expected, string):
    if all_unique_chars(string) != expected:
        print "FAILURE"
        print string
        print expected
    print "SUCCESS"

def main():
    test(True, "python")
    test(False, "dogfood")
    test(True, "")
    test(True, "1")
    test(False, "12 1")

def all_unique_chars(string):
    # if ascii we could do if len(string) > 128 return False
    for i, s in enumerate(string):
        if string.find(s,i+1) != -1:
            return False
    return True

main()

def all_unique_chars(string):
    return (len(set(string)) == len(string))

main()


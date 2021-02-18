
def lessThan():
    # We are given a multiset A of n natural numbers, and a natural number i.
    # Find how many numbers in the multiset A are smaller than that number.
    A = []
    I = []
    n = int(input("Insert n number (< 10^6) : "))
    if n < pow(10, 6):
        A = []
        while len(A) < n:
            A.append(int(input()))
        print(A)

    k = int(input("Insert k number (< 10^6) : "))
    if k < pow(10, 6):
        I = []
        while len(I) < k:
            I.append(int(input()))
        print(I)

    for elem in I:
        print(sum(i < elem for i in A))


def lastNonZeroFactorialDigit():
    # For a given number n, write the last non - zero digit of the number n!
    tests = []
    test_number = int(input("Insert test number (< 1000) : "))
    if test_number < 1000:
        tests = []
        while len(tests) < test_number:
            tests.append(int(input()))
        print(tests)

    for elem in tests:
        factorial = 1
        for i in range(elem):
            factorial *= i+1
        factorial = str(factorial).replace('0', '')
        print(factorial[len(factorial)-1])


def stringMerge():
    # A function to concatenate two strings taking one character at a time
    tests_amount = int(input("Specify the number of tests : "))
    for i in range(tests_amount):
        test = (input("Specify two strings separated by a space : "))
        test = test.split(" ")
        merged_string = ""
        for j in range(min(len(test[0]), len(test[1]))):
            merged_string += test[0][j] + test[1][j]
        print(merged_string)


def uppercaseHtmlTags():
    # Program that converts all html tags (letters between '<' '>' characters) from a file to uppercase
    ''' html_example.txt
    <html>
    <head>
    <TITLE>This is title</Title>
    </head>
    <body>
    <b>Some thing</b>
    </body>
    </html>
    '''
    file = open("html_example.txt", "r")
    text = file.read()
    inside_tag = False
    for i in range(len(text)):
        if text[i] == '<':
            inside_tag = True
        elif text[i] == '>':
            inside_tag = False
        else:
            if inside_tag is True:
                text = text[:i] + text[i].upper() + text[i+1:]
            else:
                pass
    print(text)


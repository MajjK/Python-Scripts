
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


def mysteriousOrdering(S, unorderedA):
    # Let A be an ordered sequence of numbers, eg. A = {1, 0, 20, 3}
    # For a sequence A we can define another ordered sequence S_A; where for each A[i], each value S[i] equals the
    # count of values that are to the left or A[i] and are smaller or equal to A[i]. In our example S = {0, 0, 2, 2}.
    #
    # Your task is to order the input sequence according to S. Write the function mysterious_ordering, its input is
    # sequence S and unordered sequence A, its output is A reordered according to S.
    # e.g. mysterious_ordering(S = {0, 0, 2, 2}, unordered_A = {0, 3, 20, 1}) -> {1, 0, 20, 3}
    n = len(unorderedA)
    unorderedA.sort()
    A = []

    for i in range(n):
        smallerValues = S[n - 1 - i]
        A = [unorderedA[smallerValues]] + A
        unorderedA.remove(unorderedA[smallerValues])
    return A


def proteinChains(s1, s2):
    # The protein chain can be written as a word consisting of capital letters A to T,
    # for example "BDDFPQPPRRAGGHPOPDKJKPEQAAER"
    # Given a protein chain, geneticists can swap any two amino acids in it with places, e.g. the chain "AABBCC"
    # can be swapped with "ACBBCA"
    # Your task is to write a function that will check whether it is possible to obtain protein chain s2 from protein
    # chain s1. The actual protein chains consist of about 10^8 amino acids, care must be taken to ensure good
    # performance of the algorithm.
    # Algorithm Complexity = O(n)
    uniqueLetters = set(s2)

    for elem in uniqueLetters:
        if s2.count(elem) != s1.count(elem):
            return False
    return True

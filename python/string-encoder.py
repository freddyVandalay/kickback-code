def StringEncoder(rawString):
    """
    Write a function that encodes a string as below
    E.g.
        'AABBCCCCD' --> '2A2B4CD'
        'ABBBDD' --> 'A3B2D'
    Makes assumption
    """

    # Version 1
    LastLookedAtCh = ''
    counter = 1
    encodedString = ''
    # print(f'RawString: {rawString}')
    for ch in rawString:
        if ch is LastLookedAtCh:
            counter += 1
        else:
            if counter == 1:
                encodedString = encodedString + LastLookedAtCh
            else:
                encodedString = encodedString + str(counter) + LastLookedAtCh
                counter = 1

        LastLookedAtCh = ch
    if counter > 1:
        encodedString += str(counter) + ch
    else:
        encodedString += ch
    # print(f'EncodedString: {encodedString}')

    # Verion 2 TODO
    # i = 0
    #
    # def count(ch):
    #
    # return ','.join(str(i))


def main():
    testSamples = [
        ('AABBCCCCD', '2A2B4CD'),
        ('ABBBDD', 'A3B2D')
    ]
    # StringEncoder('AABBCCCCD')
    for sample in testSamples:
        print(f"Test sample: {sample}")
        assert StringEncoder(sample[0]) == sample[1]
main()

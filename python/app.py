seen_strings = {}


def stringinate():
    """Takes input from user and performs different tasks."""

    longestString = ''
    longestPalindrome = ''
    while True:
        inputResult = input('Enter an input string (\'stats\' to see statistics, \'quit\' to exit): ')
        if (inputResult.lower() == "quit"):
            print('Exiting...\n')
            break
        elif (inputResult.lower() == "stats"):
            if len(seen_strings.keys()):
                print('\nStats:\n %s\n' % seen_strings)
                print('\n Most Popular : \n', maxOccuringItem(seen_strings)[0])
                print('\n Longest input received : \n', longestString)
                if (len(longestPalindrome.strip())):
                    print('\n Longest Palindrome string : \n', longestPalindrome)
            else:
                print('\nPlease enter input strings for statistics')

        else:
            if len(inputResult.strip()):
                print('\nInput = %s' % inputResult)
                print('Length = %s \n' % len(inputResult))
                (maxOccuringChar, frequency) = calculateMaxFrequency(inputResult)
                print('Maximum Occuring character in input string is "', maxOccuringChar, '" and it occurs', frequency,
                      ' times')
                seen_strings[inputResult] = seen_strings.get(inputResult, 0)
                seen_strings[inputResult] += 1
                if len(inputResult) > len(longestString):
                    longestString = inputResult
                if isPalindrome(inputResult) and len(inputResult) > len(longestPalindrome):
                    longestPalindrome = inputResult

            else:
                print('\n Enter valid input')


def calculateMaxFrequency(inputString):
    """Calculates the maximum frequency.
       Args:
            Inputstring:String
       Returns:
            Keyofmaxvalue,maxvalue
    """
    frequencyDict = {}
    punctuationString = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
    for char in inputString:
        if char not in punctuationString:
            frequencyDict[char] = frequencyDict.get(char, 0) + 1
    return maxOccuringItem(frequencyDict)


def maxOccuringItem(inputDict):
    """Calculates the maximum occuring item.
       Args:
            inputDict:Dictionary
       Returns:
            Keyofmaxvalue,maxvalue
    """
    maxValue = 0
    keyOfMaxValue = ''
    for (key, value) in inputDict.items():
        if value > maxValue:
            maxValue = value
            keyOfMaxValue = key

    return (keyOfMaxValue, maxValue)


def isPalindrome(inputString):
    """Checks if string is Palindrome or not.
       Args:
            inputString:String
       Returns:
            True or False
    """
    for i in range(0, len(inputString) // 2):
        if inputString[i] != inputString[len(inputString) - i - 1]:
            return False
    return True


if __name__ == '__main__':
    stringinate()
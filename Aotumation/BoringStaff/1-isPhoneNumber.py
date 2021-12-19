import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#print('Is 415-555-4242 a phone number?')
#print(isPhoneNumber('415-555-4242'))
#print('Is Moshi moshi a phone number?')
#print(isPhoneNumber('Moshi moshi'))

#message = 'Call me at 415-555-1011 tomorrow, 415-555-9999 is my office.'
#for i in range(len(message)):
#    chunk = message[i:i+12]
#    if isPhoneNumber(chunk):
#        print('Phone number found: ' + chunk)
#print('Done')

#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo = phoneNumRegex.search('My number is 415-555-4242.')
#print('Phone number found: ' + mo.group())

#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search('My number is 415-555-4242.')
#print(mo.group(1))
#print(mo.group(2))
#print(mo.group(0))
#print(mo.group())
#print(mo.groups())
#
#areaCode, mainNumber = mo.groups()
#print(areaCode)
#print(mainNumber)

#heroRegex = re.compile(r'Batman|Tina Fey')
#mo1 = heroRegex.search('Tina Fey Batman and')
#print(mo1.group())

#batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#mo = batRegex.search('Batman Batmobile lost a wheel')
#print(mo.group())
#print(mo.group(0))
#print(mo.group(1))

#batRegex = re.compile(r'Bat(wo)?man')
#mo1 = batRegex.search('The Batwoman Adventures of Batman')
#print(mo1.group())
#
#mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group())

#phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
#mo1 = phoneRegex.search('My number is 415-555-4242')
#print(mo1.group())
#
#mo2 = phoneRegex.search('My number is 555-4242')
#print(mo2.group())

#batRegex = re.compile(r'Bat(wo)*man')
#mo1 = batRegex.search('The Advantures of Batman')
#print(mo1.group())
#
#mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group())
#
#mo3 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo3.group())

#batRegex = re.compile(r'Bat(wo)+man')
#mo1 = batRegex.search('The Adventure of Batwoman')
#print(mo1.group())
#
#mo2 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo2.group())
#
#mo3 = batRegex.search('The adventures of Batman')
#if ( mo3 == None):
#    print('Yeah it is None')

## (Ha){3} will match 'HaHaHa', but it will not match 'Ha'
## (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', 'HaHaHaHaHa'
## (Ha){3,}  will match three or more instances
## (Ha){,5}  will match zero to five instances
## --------------------------------------------------------
#haRegex = re.compile(r'(Ha){3}')
#mo1 = haRegex.search('HaHaHa')
#print(mo1.group())
#
#mo2 = haRegex.search('Ha')
#if (mo2 == None):
#    print('Yeah it is None')

## greedy (default): match longest string possible
## Non-greedy      : match shortest string possible
## ? : Declare a non-greedy match
## ? : flaggin an optional group
#greedyHaRegex = re.compile(r'(Ha){3,5}')
#mo1 = greedyHaRegex.search('HaHaHaHaHa')
#print(mo1.group())
#
#nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
#mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
#print(mo2.group())

## search():  will return first match
## findall(): will return every match (list of strings)
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
#print(mo.group())
#
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#print(mo1)
#
## findall() return a list of tuple, if there are groups
#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
#mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#print(mo2)

## Character Classes
## \d: 0-9
## \D: char but not 0-9
## \w: Letter, 0-9, underscore
## \W: Any char but not letter, 0-9, underscore
## \s: space(space, tab, newline)
## \S: Any char but not Space(space, tab, newline)
## ------------------------------------------------
#xmasRegex = re.compile(r'\d+\s\w+')
#mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swanas, 6 geese, 5 rings, 4 brids, 3 hens, 2 doves, 1 partridge')
#print(mo)

## will match any vowel
#vowelRegex = re.compile(r'[aeiouAEIOU]')
#mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
#print(mo)

## Making your own Character classes
## caret^ just after the character class's opening bracket,  make a negative character class.
#vowelRegex = re.compile(r'[^aeiouAEIOU]')
#mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
#print(mo)
#
## caret^ at the start of a regex, match occur at the beginning of the searched text.
#beginWithHello = re.compile(r'^Hello')
#mo1 = beginWithHello.search('Hello, World!')
#print(mo1)
#
## doller$ at the end of regex, string must end with this regex
#mo2 = beginWithHello.search('He said Hello.')
#if( mo2 == None):
#    print('Yeah it is None')

#endsWithNumber = re.compile(r'\d$')
#mo = endsWithNumber.search('Your number is 42')
#print(mo)
#
#mo1 = endsWithNumber.search('Your number is forty two.')
#if(mo1 == None):
#    print('Yeah it is None')

#wholeStringIsNum = re.compile(r'^\d+$')
#mo = wholeStringIsNum.search('1234567890')
#print(mo)
#
#mo1 = wholeStringIsNum.search('1234zxdcv567890')
#if (mo1 == None):
#    print('mo1 is None')
#
#mo2 = wholeStringIsNum.search('12345  67890')
#if (mo2 == None):
#    print('mo2 is None')

## The Wildcard Character
## . dot | wildcard match any character except for a newline. just one character
#atRegex = re.compile(r'.at')
#mo = atRegex.findall('The cat in the adhat sat on the flat mat.')
#print(mo)

## Matching Everything with Dot-Start
## . dot: any single char except newline
## * star: Zero or more of the preceding char
## .* anything
## Greedy mode: match as much text as possible.
## ------------------------------------------
#nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
#mo = nameRegex.search('First Name: Al is here. Last Name: Sweigart')
#print(mo.group())
#print(mo.group(1))
#print(mo.group(2))

## .*? : Non-greedy: match shorter text.
#nongreedyRegex = re.compile(r'<.*?>')
#mo = nongreedyRegex.search('<To serve man> for dinner.>')
#print(mo.group())
#
#greedyRegex = re.compile(r'<.*>')
#mo1 = greedyRegex.search('<To serve man> for dinner.>')
#print(mo1.group())

## Matching Newlines with the Dot Character


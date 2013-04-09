
# Level 0 is no messages
# Level 1 is ERROR messages
# Level 2 is WARNING messages
# Level 3 is INFO messages
DEBUG_LEVEL = 2

char_to_morse = {
'!':"-.-.--",
'"':".-..-.",
'$':"...-..-",
'&':".-...",
"'":".----.",
'(':"-.--.",
')':"-.--.-",
'+':".-.-.",
',':"--..--",
'-':"-....-",
'.':".-.-.-",
'/':"-..-.",
'0':"-----",
'1':".----",
'2':"..---",
'3':"...--",
'4':"....-",
'5':".....",
'6':"-....",
'7':"--...",
'8':"---..",
'9':"----.",
':':"---...",
';':"-.-.-.",
'=':"-...-",
'?':"..--..",
'@':".--.-.",
'_':"..--.-",
'A':".-",
'B':"-...",
'C':"-.-.",
'D':"-..",
'E':".",
'F':"..-.",
'G':"--.",
'H':"....",
'I':"..",
'J':".---",
'K':"-.-",
'L':".-..",
'M':"--",
'N':"-.",
'O':"---",
'P':".--.",
'Q':"--.-",
'R':".-.",
'S':"...",
'T':"-",
'U':"..-",
'V':"...-",
'W':".--",
'X':"-..-",
'Y':"-.--",
'Z':"--.."
}
morse_to_char = {v:k for k,v in char_to_morse.items()}

char_delimit = " "
word_delimit = "  "
# Between chars is 2 spaces
def charToMorse(c):
    if char_to_morse.has_key(c):
        return char_to_morse[c]
    elif c == ' ':
        return char_delimit
    else:
        if DEBUG_LEVEL >= 3:
            print "Unknown symbol '%c', skipping..." % c 
        return ""

# Between words is 3 spaces
def writeMorse(msg):
    out = []
    for word in msg.upper().split(" "):
        out.append(char_delimit.join( filter(bool, map(charToMorse, word)) ))
    return word_delimit.join(out)

def morseToChar(m):
    if morse_to_char.has_key(m):
        return morse_to_char[m]
    else:
        if DEBUG_LEVEL >= 3:
            print "Unknown sequence '%s', skipping..." % m
        return ""

def readMorse(morse):
    out = []
    for word in morse.split(word_delimit):
        out.append( "".join( filter(bool, map(morseToChar, word.split(char_delimit))) ) )
    return " ".join(out)


def doTest(test_message):
    print "--------------------------------------------------------------"
    print "Original: %s" % test_message.upper()
    a = writeMorse(test_message)
    print "   Morse: %s" % a
    b = readMorse(a)
    print "and Back: %s" % readMorse(a)
    print "Valid? %s" % ("Yes" if test_message.upper() == b else "No")
    print "--------------------------------------------------------------"

test1 = "This is number 1 test."
test2 = "What is the meaning of life, the universe, and everything?"
test3 = "Wierd chars # is !@#$%^&*()<> bloop "
with open("quotes.txt",'r') as f:
    test4 = f.read()

doTest(test1)
doTest(test2)
doTest(test3)
doTest(test4)
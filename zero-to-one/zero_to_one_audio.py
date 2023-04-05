import pyttsx3 as ts

# Object creation 
engine = ts.init()

"""RATE"""
# getting deatails of the current speaking rate
rate = engine.getProperty('rate')

# Printing the current rate
print(rate)

# Setting up new voice rate
engine.setProperty('rate', 135)

"""VOLUME"""
# Getting to know current volume level (min=0 and max=1)
volume = engine.getProperty('volume')

# Printing current volume level(min=0 and max=1)
print(volume)

# Setting up volume level between 0 and 1 
engine.setProperty('volume', 1.0)

"""VOICE"""
# Getting details of current voice
voices = engine.getProperty('voices')

# For male speaker
#engine.setProperty('voice', voices[0].id)

# For female speaker
engine.setProperty('voice', voices[1].id)

#Do some testing
engine.say("""Hello World!
           I will start reading shortly!
           Kindly need your attention beautiful!""")

# Print a message 
print('Are you ready? Let\'s start...')

# Read the text file from your computer(any source)
# or you can import the file path
word = open('FILENAME.txt', 'r', encoding='utf-8')

for line in word:
    engine.say(line)
    engine.runAndWait()
    
print('Done with reading the file 😎')

engine.say('Thank you so much for listening, I hope you have fun')


# In case you want to display the rate
# engine.say('My current speaking rate is' + str(rate))

engine.runAndWait()
engine.stop()

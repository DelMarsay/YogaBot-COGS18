import string
import random
from IPython.display import Image, display
import pandas as pd

from classes import YogaClass


def is_question(input_string):
    
    """ Takes an input message and 
    returns True if it's a question """
    
    if '?' in input_string:
        output = True
    
    else:
        output = False
        
    return output


def remove_punctuation(input_string):
    
    """ It returns input string with 
    punctuation removed """ 
    
    out_string = ''                      
    
    for char in input_string:             
        if char not in string.punctuation:
            out_string = out_string + char 
            
    return out_string


def prepare_text(input_string):
    
    """ It returns input string with 
    lowercase letters and without punctuation 
    and makes a list """
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list


def selector(input_list, check_list, return_list):
    
    """Returns an item from return_list if 
    an item in input_list is in check_list."""
    
    output = None 
    
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break 
            
    return output


def string_concatenator(string1, string2, separator):
    
    """Concatenates two strings with separator between them"""
    
    output = string1 + separator + string2
    
    return output


def list_to_string(input_list, separator):
    
    """Makes a string from input_list 
    with separator between items"""
    
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
        
    return output


def should_end_chat(input_list):
    """Ends the chat if the user inputs 'quit'."""
    
    if is_in_list(['quit', 'bye', 'goodbye', 'night'], input_list):
        return True 
    else:
        return False


def is_in_list(list_one, list_two):
    
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    
    """Find and return an element from list_one 
    that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


def get_image(pose, df):
    
    """Returns an image of pose from df"""
    
    filtered_df = df[df['english_name'].str.lower() == pose.lower()]
    if not filtered_df.empty:
        for index, row in filtered_df.iterrows():
            output = Image(url=row['img_url'], width = 300)
            return output
    else:
        return f"Sorry. I don't have a {pose} demo yet."


def yoga_buddy(yoga_classes):
    
    day = random.choice(list(yoga_classes.keys()))
    
    if yoga_classes[day].students:
        buddy = random.choice(yoga_classes[day].students).capitalize()

        return f'Your yoga buddy is {buddy} on {day} at {yoga_classes[day].time}' 
            
    return 'Sorry, no yoga buddy found!'

YOGA_IN = ['chest', 'shoulders', 'arms', 'back', 'abs', 'hips', 'glutes', 'legs']
YOGA_OUT = ['Got it! I recommend', 'Ok. You can try', 'I see. A good pose is']
YOGA_POSES = {'chest': ['Camel', 'Wild thing', 'Crescent moon'], 
              'shoulders': ['Forward bend with shoulder opener', 'Shoulder stand', 'Eagle'], 
              'arms': ['downward-facing dog', 'Plow', 'Upward-facing dog'], 
              'back': ['cat', 'cow', 'Child\'s Pose'], 
              'abs': ['Boat', 'Plank', 'Side plank'], 
              'hips': ['Half lord of the fishes', 'Pigeon', 'Butterfly'], 
              'glutes': ['Chair', 'Sphinx', 'Warrior Three'], 
              'legs': ['Tree', 'Warrior One', 'Warrior Three']}

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

GREETINGS_IN = ['hello', 'hey', 'sup', 'hola', 'hi', 'howdy', 'good morning', 'good afternoon', 'good evening']
GREETINGS_OUT = ['Hi there. How are you feeling today?', 
                 'Glad you\'re here. How are you?', 
                 'Welcome to my chat room. How are you?']

BAD_IN = ['bad', 'tired', 'down', 'stressed', 'anxious', 'overwhelmed', 'lazy', 
          'sick', 'depressed', 'sleepy', 'mad', 'angry', 'sad', 'upset' ]
BAD_OUT = ['I recommend a yoga class. What day works for you?',
            'Sorry to hear that. If you\'d like a yoga buddy for support, type "buddy"']

GOOD_IN = ['good', 'excited', 'happy', 'energized', 'awesome', 'fine', 'blessed',
           'super', 'ok', 'great', 'ecstatic', 'wonderful', 'well', 'amazing' ]
GOOD_OUT = ['Great to hear that! Pick a day of the week for yoga.', 
            'Cool! What day can you attend my yoga class?', 
            'That sounds nice! What day are you free for yoga?']

LAUGHTER_IN = ['ha', 'haha', 'hahaha', 'lol', 'lmao', 'funny']
LAUGHTER_OUT = ['Laughter is medicine and so is yoga!']

JOKE_IN = ['joke', 'no', 'ok']
JOKE_OUT = ['Why did the bagel struggle in yoga class? It couldn\'t find its center', 
           'What do you call a bagel that has mastered yoga class. A pretzel',
           'Why does everyone love yoga teachers? They bend over backwards for you', 
           'I didn\'t think yoga would fix my posture. But I stand corrected', 
           'What\'s stretchy and has wheels? My yoga pants. I lied about the wheels']

NONO_IN = ['you', 'name', 'old', 'wearing', 'live']
NONO_OUT = ['What body part would you like to work on?', 
           'What day of the week could you come to my yoga class?']

           
UNKNOWN = ['Type "buddy" if you would like to be matched with another yogi', 
           'type the name of a body part to match with a pose', 
           'type a day of the week to attend a class',
           'type "joke" if you\'d like to simply hear a joke']

QUESTION = ['This is about you, not me', 'I\'ll get back to you on that', 
            'No one\'s ever asked that before',  
           'Here\'s a question for you: what day can you join me for yoga?']

yoga_classes = {'Sunday': YogaClass('Sunday', '9am'),
               'Monday': YogaClass('Monday', '10am'),
               'Tuesday': YogaClass('Tuesday','6pm'),
               'Wednesday': YogaClass('Wednesday','10am'),
               'Thursday': YogaClass('Thursday', '6pm'),
               'Friday': YogaClass('Friday', '10am'),
               'Saturday': YogaClass('Saturday', '11am')}

studio_members = ['Anna', 'Brad', 'Carla', 'David', 'Erica', 'Francisco', 'Gina', 'Hector', 'Ingrid', 'James']

for day in yoga_classes:
    yclass = yoga_classes[day]
    number = random.choice(range(6,9))
    while number:
        if yclass.available:
            yclass.students = yclass.students + [random.choice(studio_members)]
            if len(yclass.students) == yclass.capacity:
                yclass.available = False
        number = number - 1

df = pd.read_json('https://raw.githubusercontent.com/rebeccaestes/yoga_api/master/yoga_api.json')

def have_a_chat():
    
    #this function is from assignment 3 and I modified it for my own chatbot
    #it includes original code by me
    
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('Yoga student :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if should_end_chat(msg):
            out_msg = 'Namaste!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            
            outs.append(selector(msg, BAD_IN, BAD_OUT))
                
            outs.append(selector(msg, GOOD_IN, GOOD_OUT))
            
            outs.append(selector(msg, LAUGHTER_IN, LAUGHTER_OUT))

            # Check if the input has no or joke and output a joke
            outs.append(selector(msg, JOKE_IN, JOKE_OUT))
            
            outs.append(selector(msg, ['thanks', 'thank'], ['You\'re welcome']))

            # Check if the input mentions a body part that is specified, add a pose and image output if so
            if is_in_list(msg, YOGA_IN):
                body_part = find_in_list(msg, YOGA_IN)
                pose = random.choice(YOGA_POSES[body_part])
                
                output = get_image(pose, df)
                string = f"Sorry. I don't have a {pose} demo yet."
                
                if output is not string:
                    display(output)
                    outs.append(list_to_string([selector(msg, YOGA_IN, YOGA_OUT), pose, 'pose for your',
                                            body_part], ' '))
                else:
                    outs.append(output)

            if is_in_list(msg, DAYS):
                day = find_in_list(msg, DAYS)
                outs.append(yoga_classes[day.capitalize()].add_student())
                
            if is_in_list(msg, ['buddy']):
                outs.append(yoga_buddy(yoga_classes))
            
            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(selector(msg, NONO_IN, NONO_OUT))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = random.choice(QUESTION)

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('Yoga teacher:', out_msg)






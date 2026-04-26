import nltk
from nltk.chat.util import Chat, reflections

# 1. Custom Reflections
my_reflections = reflections.copy()
my_reflections['my pr'] = 'your Personal Record'
my_reflections['i weigh'] = 'you weigh'

# 2. The Rule Base
pairs = [
    [
        r"hi|hello|hey|sup", 
        ["Hello! I am your Rule-Based Fitness Assistant. Ask me about your diet, cardio, or workouts!"]
    ],
    [
        r"my goal is to (.*)", 
        ["That's a fantastic goal! Accomplishing %1 will require consistency in both your lifting and your nutrition.", 
         "I love that goal. Let's make %1 happen!"]
    ],
    [
        r"(.*)(protein|diet|macros)(.*)", 
        # Fixed the % bug by spelling out "percent"
        ["Nutrition is 80 percent of the work! For high protein, prioritize foods like chicken breast, eggs, and paneer.", 
         "Make sure you are hitting your protein macros to rebuild muscle after lifting."]
    ],
    [
        r"(.*)(steps|walking|cardio)(.*)", 
        ["A daily goal of 10,000 steps is fantastic for active recovery and cardiovascular health without burning you out.",
         "Walking is the most underrated cardio. 10,000 steps a day keeps your metabolism active!"]
    ],
    [
        r"(.*)(coffee|caffeine|pre-workout)(.*)", 
        ["Black coffee is an excellent, low-Kcal pre-workout. A high-quality instant coffee will give you the same performance boost as brewed without the hassle."]
    ],
    [
        r"i weigh (.*)", 
        ["Noted. Since you weigh %1, make sure your water intake and protein match your body mass!"]
    ],
    [
        r"my weight is (.*)", 
        ["Noted. At %1, make sure your water intake and protein match your body mass!"]
    ],
    # Fallback Rule
    [
        r"(.*)", 
        ["I am strictly a fitness bot. Could you rephrase that to be about workouts, steps, or nutrition?", 
         "My rules don't cover that. Ask me about your diet or gym routine instead!"]
    ]
]

def run_fitness_bot():
    print("=== NLP Fitness Assistant ===")
    print("Type 'quit', 'exit', or 'bye' to end the program.")
    print("-" * 50)
    
    # Initialize the bot
    bot = Chat(pairs, my_reflections)
    
    # Custom interaction loop
    while True:
        # Adds the "You: " prefix to your input
        user_input = input("You: ")
        
        # Check if the user wants to exit (converted to lowercase to catch "Bye", "EXIT", etc.)
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Keep grinding at the gym! See you later.")
            break  # This physically breaks the loop and ends the program
            
        # Generate and print the bot's response with the "Bot: " prefix
        response = bot.respond(user_input)
        if response:
            print(f"Bot: {response}\n")
        else:
            print("Bot: I didn't quite catch that.\n")

if __name__ == "__main__":
    run_fitness_bot()
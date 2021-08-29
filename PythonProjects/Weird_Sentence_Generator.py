
import random


# creating the word list or database

person = ["I",
          "You",
          "They",
          "He",
          "She",
          "We"
          ]

secondword = ["am",
          "are",
          "is"
          ]

action = ["going",
          "running",
          "dodging",
          "watching",
          "driving",
          "stopping",
          "flexing",
          "playing",
          "cooking",
          "never",
          "using"
        ]

objects = ["Netflix",
          "Spotify",
          "Call of Duty",
          "Facebook",
          "Google",
          "book",
          "skateboard",
          "football",
          "basketball",
          "lecture",
          "computer",
          "dinner",
          "breakfast",
          "lunch",
          "meatballs",
          "fish",
          "bicycle",
          "typo",
        ]

location = ["in Istanbul",
            "in London",
            "at my home",
            "outside",
            "in my dream"
        ]

timezone = ["today",
          "tomorrow",
          "yesterday",
          "right now",
          "an hour ago",
          "this month",
        ]

random_per = random.choice(person)
random_2nd = random.choice(secondword)
random_act = random.choice(action)
random_obj = random.choice(objects)
random_loc = random.choice(location)
random_tim = random.choice(timezone)

print(f"{random_per} {random_2nd} {random_act} {random_obj} {random_loc} {random_tim}.")



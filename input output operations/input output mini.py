# -----------------------------------------------------------------------------------
# Stream: Python
# Tech Module: 10 Operations
# Project: 1
#
# Problem:
# Your friend has sent a text file with lines containing a secret message.
# You're supposed to find the meeting time and place using the following hints:
#
# 1. The number of lines in the file tells you the meeting time.
#    - If the number of lines < 12, it's that many AM.
#    - If it's between 12 and 24, convert to 12-hour format and display AM/PM.
#
# 2. The word that appears most frequently gives the meeting place.
#    - Example: if "Park" appears most → Meeting place is "Park Street"
#
# Sample Output:
# Meeting time: 3 PM
# Meeting place: Apollo Street
# -----------------------------------------------------------------------------------

from collections import Counter
import re

def get_meeting_details(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            line_count = len(lines)

            
            full_text = ' '.join(lines)

         
            words = re.findall(r'\b\w+\b', full_text)

            word_counts = Counter(words)

           
            most_common_word, freq = word_counts.most_common(1)[0]

            
            if line_count == 0:
                meeting_time = "No content in file"
            elif line_count <= 12:
                meeting_time = f"{line_count} AM"
            elif line_count < 24:
                meeting_time = f"{line_count - 12} PM"
            else:
                meeting_time = f"{line_count % 12 or 12} PM"

          
            meeting_place = most_common_word.capitalize() + " Street"

          
            print("Meeting time:", meeting_time)
            print("Meeting place:", meeting_place)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print("An error occurred:", e)


# -------------------------------

get_meeting_details("sample.txt")

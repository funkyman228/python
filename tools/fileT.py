import googletrans
import os
import locale
import re
num = 0

# most of the charectors used in japanese
japanese_characters_pattern = '[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]'

# illigal charecters
illegal_characters = ['\\', '/', '?', ':', '*', '"', '<', '>', '|']
pattern = '[{}]'.format(''.join(illegal_characters))

print("Enter dir")
folder_path = input()  # Replace this with the actual path to your folder
folder_path = folder_path.replace(os.sep, '/')
file_names = os.listdir(folder_path)
total = len(file_names)


# ask fast or slow
print("fast: f, or slow: s")
speed = input()

for file_name in file_names:
    num = num + 1

    # print current file num
    print("\n", num, "of", total)

    old_name = os.path.join(folder_path, file_name)

    # Split the file name into two parts
    name_parts = file_name.split("_")

    # print old name
    print(name_parts[1])

    if re.search(japanese_characters_pattern, file_name):
        
        # Translate the file name using googletrans
        translator = googletrans.Translator()
        translated_name_part = translator.translate(name_parts[1], src='ja', dest='en').text
        translated_name_part = translated_name_part.replace("\"", '')

        # limit to 100 char
        translated_name_part = translated_name_part[:100]

        # delete illigal chareters
        translated_name_part = re.sub(pattern, '', translated_name_part)

        # Join the two parts back together to get the final translated file name
        translated_name = name_parts[0] + "_" + translated_name_part

        # print new file name
        print(translated_name_part)


        # Rename the file
        if speed == "s":
            if input() != "n":
                new_name = os.path.join(folder_path, translated_name)
                os.rename(old_name, new_name)
        else:
            new_name = os.path.join(folder_path, translated_name)
            os.rename(old_name, new_name)

print("\ndone")
input()
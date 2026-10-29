import pandas as pd
import time
from googletrans import Translator

input_file = '/Users/seanwatanabe/Documents/basic-words.xlsx'
output_file = '/Users/seanwatanabe/Documents/basic-words-translated.xlsx'

df = pd.read_excel(input_file,  engine="openpyxl")

# print(df)

df.columns = ['word', 'part_of_speech']

df['word'] = df['word'].str.strip()
df['part_of_speech'] = df['part_of_speech'].str.strip()


words= df['word']

translator = Translator()

japanese_words = []

# Originally, built this program to translate 3000+ Eng words, so I assumed relieving memory usage using "iter()"
# would be a good way to handle the work loads. NOT SURE tho.

for index, word in  enumerate(iter(words)):
    if index < 300:
        time.sleep(0.1)
        try:
            translated_word = translator.translate(word, src="en", dest='ja').text
            print(index, translated_word)
        except Exception as e:
            print(f"Error {e}")
    else:
        break

    # try:
    #     translated_word = translator.translate(word, src="en", dest='ja').text
    #     print(translated_word)
    # except Exception as e:
    #     print(f"Error {e}")



#     try:
# translated_word = translator.translate(word, src='en', dest='ja').text
#     print(translated_word)
# except:Exception as e:
# print(f"Error: {e}")
    







# def translate_with_pos(word, speech):
#     try:
#         context = f"{word} ({speech})"
#         return translator.translate(context, src='en', dest='ja').text
#     except Exception as e:
#         return f"[Error: {e}]"

# df['japanese'] = df.apply(lambda row: translate_with_pos(row['word'], row['part_of_speech']), axis=1)

# df.to_excel(output_file, index=False, engine='openpyxl')
# print(f"✅ Translations complete. File saved as: {output_file}")
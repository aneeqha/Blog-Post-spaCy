

import re, os, shutil, sys
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
#rom textblob import TextBlob

def main():
    num = 0
    Input_String = sys.argv[1]
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe('spacytextblob')

    # For Splitting Paragraphs into List of Sentences
    products = Input_String.split(".")
    postive = 0
    negative = 0
    print("Polarity ranges from (-1 -> 1)")
    for product in products:
        product = product.strip()
        if (product != ""):
            blob = nlp(product)
            Polarity = float(blob._.polarity)
            print("\"" + product + "\" -> ", Polarity)
            if (Polarity > 0):
                 if (Polarity < 0.25):
                    print("Emotion: Mildly Positive")
                 if (Polarity < 0.5):
                    print("Emotion: Positive")
                 else:
                    print("Emotion: Strongly Positive")

            elif (Polarity < 0):
                Polarity = (-1)*Polarity
                if (Polarity < 0.25):
                    print("Emotion: Mildly Negative")
                elif (Polarity < 0.5):
                    print("Emotion:  Negative")
                else:
                    print("Emotion: Strongly Negative")

            else:
                print("Emotion: Impassive")
            num += 1

            # if (Polarity > 0):
            #     if (Polarity < 0.5):
            #         print("Emotion: Mildly Positive")
            #     else:
            #         print("Emotion: Strongly Positive")

            # elif (Polarity < 0):
            #     Polarity = (-1)*Polarity
            #     if (Polarity < 0.5):
            #         print("Emotion: Mildly Negative")
            #     else:
            #         print("Emotion: Strongly Negative")

            # else:
            #     print("Emotion: Impassive")
            # num += 1


if __name__ == '__main__':
    main()

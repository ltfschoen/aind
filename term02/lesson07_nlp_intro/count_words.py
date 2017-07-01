

"""Count words."""

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    
    # DONE: Convert to lowercase
    text = text.lower()

    # TODO: Split text into tokens (words), leaving out punctuation
    # (Hint: Use regex to split on non-alphanumeric characters)
    import re

    # replace dash with empty space
    text = re.sub(r'[^a-zA-Z!\-]', ' ', text)

    # replace the following with empty space
    text = text.replace(".", "") \
               .replace(",", "") \
               .replace("-", "") \
               .replace("?", " ") \
               .replace("!", " ") \
               .replace(";", " ") \
               .replace(":", " ") \
               .replace("\'", " ") \
               .replace("\"", " ") \
               .replace('  ',' ')
    print("text: ", text)
    tokens = list(set(text.split()))
    print("unique tokens: ", tokens)
    print ("corpus has " +  str(len(text)) + " total number of words")
    print ("corpus has " +  str(len(tokens)) + " unique words")
    
    # TODO: Aggregate word counts using a dictionary
    for i, w in enumerate(tokens):
        counts[w] = text.count(w)
    print("word counts: ", counts)
    
    return counts


def test_run():
    # Replace with input.txt, input2.txt, and input3.txt
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()

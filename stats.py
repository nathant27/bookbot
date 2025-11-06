def count_words(text):
    return len(text.split())

def get_letter_counter(text):
    counter = {}

    for c in text:
        c = c.lower()
        
        """
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
        """

        counter[c] = counter.get(c, 0) + 1

    return counter

    
    
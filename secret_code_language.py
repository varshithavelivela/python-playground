menu=["a.encode","b.decode"]
print(menu)
user=input("Enter your choice: ")
if user.lower() == "a":
  
    sentence = input("Enter the sentence: ")
    words=sentence.split()
    encoded_word=[]
    for word in words:
        if len(word) >=3:
            new_word=word[1:]+word[0]
            lan1="klh"+new_word+"mno"
            encoded_word.append(lan1)
        else:
            reversed_word=word[::-1]
            encoded_word.append(reversed_word)

    final_sentence=" ".join(encoded_word)
    print(final_sentence)
        
else:
    sentence=input("Enter your sentence:")
    words=sentence.split()
    decoded_word=[]
    for word in words:
        if len(word)>=3:
            old_word=word[3:-3]
            lan2=old_word[-1]+old_word[:-1]
            decoded_word.append(lan2)
        else:
           correct_word=word[::-1]
           decoded_word.append(correct_word)
    final_sentence=" ".join(decoded_word)
    print(final_sentence)



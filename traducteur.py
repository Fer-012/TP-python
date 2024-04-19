def translate(phrase, dic):
    translated_phrase = []
    for i in phrase.split():
        if i in dic:
            translated_phrase.append(dic[i])
        else:
            translated_phrase.append(i) 
    return ' '.join(translated_phrase)

dic = {"langage": "language", "un": "a", "est": "is", "formidable": "wonderful"}
phrase_fr = "Python est formidable"
print("French:", phrase_fr)
print("English:", translate(phrase_fr, dic))

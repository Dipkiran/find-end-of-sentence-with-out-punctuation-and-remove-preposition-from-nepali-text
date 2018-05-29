import nltk

def base():
    raw = 'आमा and मामा को i am 4 मा fail माथि '
    nepaliprep =['करिब', 'माथि', 'पारि', 'पछि', 'विरूद्घ', 'माझ', 'वरिपरि', 'जस्तो कि', 'मा', 'पहिला', 'पछाडि', 'तल','मन्तिर', 'छेउमा','बिचमा','त्यसभन्दा पर',
    'तर','ले','त्यसो हुँदा हुँदै पनि','ताका','बाहेक','लागि','बाट','भित्र', 'नजिक', 'अर्को','को','प्रति', 'देखि', 'तिर', 'सँग','लाई']
    nouns = ['आमा','मामा']
    output=[]
    string = ''
    for word in raw.split():
        if word not in nouns:
            try:
                for words in nepaliprep:
                    newword = word.replace(words,'')
                    word = newword
            except:
                pass
        output.append(word)
    string = ' '.join(output)
    print(string)
base()

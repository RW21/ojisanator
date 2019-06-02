import MeCab
import emojis
import jaconv

chasen = MeCab.Tagger("-Ochasen")


def parse(sentence):
    word_list = [word.split('\t') for word in chasen.parse(sentence).split('\n')]
    del word_list[len(word_list) - 2:]
    return word_list


def add_nouns(parsed: list):
    word_list = []
    for word in parsed:

        if '人名' in word[3]:
            word_list.append(word[0])
            word_list.append('チャン')

        elif '助詞' in word[3]:
            word_list.append(word[0])
            word_list.append('、')

        elif '助動詞' in word[3]:
            word_list.append(jaconv.hira2kata(word[0]))

        else:
            word_list.append(word[0])

    return ''.join(word_list)

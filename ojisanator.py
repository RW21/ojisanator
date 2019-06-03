import random

import MeCab
import jaconv

chasen = MeCab.Tagger("-Ochasen")


def parse(sentence):
    word_list = [word.split('\t') for word in chasen.parse(sentence).split('\n')]
    del word_list[len(word_list) - 2:]
    return word_list


def random_emote():
    if random.randint(0, 2) == 0:
        return '😚'
    else:
        return '（笑）'


def add_ojisan(parsed: list):
    word_list = []
    for i, word in enumerate(parsed):

        if '人名' and '固有名詞' in word[3]:
            word_list.append(word[0])
            word_list.append('チャン')

            if random.randint(0, 2) == 0:
                word_list.append(random_emote())

        elif '係助詞' in word[3]:
            word_list.append(word[0])
            word_list.append(random_emote())
            word_list.append('、')

        elif '助動詞' in word[3] and '特殊' not in word[4]:
            # catches ない to not kanakanalise it.
            word_list.append(jaconv.hira2kata(word[0]))
            word_list.append(random_emote())

        elif '終助詞' in word[3]:
            word_list.append(jaconv.hira2kata(word[0]))
            word_list.append(random_emote())

        elif '接尾' and '人名' in word[3]:
            pass

        elif '接続助詞' in word[3]:
            word_list.append(word[0])
            word_list.append(random_emote())

        elif word[0] == ('?' or '？'):
            word_list.append('❓')

        elif word[0] == ('!' or '！'):
            word_list.append('❗')

        else:
            word_list.append(word[0])

    return ''.join(word_list)


def ojisanator(sentence):
    return add_ojisan(parse(sentence))

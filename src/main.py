#!/usr/bin/python
# coding: utf-8


def read_file(file_path=u'../res/gre词汇txt版.txt'):
    with open(file_path, 'r') as f:
        raw = f.readlines()

    raw = list(map(lambda i: i.strip(), raw))
    assert len(raw) > 1, 'word file empty!'
    word_dic = dict()
    for index, line in enumerate(raw):
        if index % 2 == 0:
            word_dic[line] = raw[index + 1]

    return word_dic


def get_notified_word(word_dictionary):
    # May change to other ways in the future
    from random import choice
    word = choice(list(word_dictionary.keys()))
    return word, word_dictionary[word]


def push_notification(msg):
    word, chinese = msg
    cmd = """/usr/bin/osascript -e 'display notification \"{chi}\" with title \"{eng}\"' """.format(eng=word,
                                                                                                    chi=chinese)
    import os
    os.system(cmd)


if __name__ == '__main__':
    all_words = read_file()
    word_pair = get_notified_word(all_words)
    push_notification(word_pair)

#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/18
"""
"""


def test_phkit():
    import phkit

    text = '漢字拼音啊！！！Hi:TTS for han4 -~_@25只=小鱼儿。'
    target_hans = '汉字拼音啊!!!hi:TTS for han四 -~_@二十五只=小鱼儿。'

    target_pins = ['han4', 'zi4', 'pin1', 'yin1', 'a5', ('!',), ('!',), ('!',), ('h',), ('i',), (':',), ('T',), ('T',),
                   ('S',), (' ',), ('f',), ('o',), ('r',), (' ',), ('h',), ('a',), ('n',), 'si4', (' ',), ('-',),
                   ('~',), ('_',), ('@',), 'er4', 'shi2', 'wu3', 'zhi3', ('=',), 'xiao3', 'yu2', 'er2', ('。',)]
    target_phs = ['h', 'an', '4', '-', 'z', 'iy', '4', '-', 'p', 'in', '1', '-', 'ii', 'in', '1', '-', 'aa', 'a', '5',
                  '-', '!', '-', '!', '-', '!', '-', 'H', '-', 'I', '-', ':', '-', 'Tt', '-', 'Tt', '-', 'Ss', '-', '#',
                  '-', 'F', '-', 'O', '-', 'R', '-', '#', '-', 'H', '-', 'A', '-', 'N', '-', 's', 'iy', '4', '-', '#',
                  '-', '-', '-', '-', '-', 'ee', 'er', '4', '-', 'sh', 'ix', '2', '-', 'uu', 'u', '2', '-', 'zh', 'ix',
                  '3', '-', '-', 'x', 'iao', '3', '-', 'vv', 'v', '2', '-', 'ee', 'er', '2', '-', '.', '-', '~', '_']
    target_seq = [11, 32, 74, 2, 28, 51, 74, 2, 19, 46, 71, 2, 12, 46, 71, 2, 3, 30, 75, 2, 128, 2, 128, 2, 128, 2, 109,
                  2, 110, 2, 133, 2, 95, 2, 95, 2, 94, 2, 135, 2, 107, 2, 116, 2, 119, 2, 135, 2, 109, 2, 102, 2, 115,
                  2, 22, 51, 74, 2, 135, 2, 2, 2, 2, 2, 8, 39, 74, 2, 23, 50, 72, 2, 25, 56, 72, 2, 29, 50, 73, 2, 2,
                  27, 44, 73, 2, 26, 65, 72, 2, 8, 39, 72, 2, 130, 2, 1, 0]

    assert target_phs.count('-') == len(target_hans) == 37

    hans = phkit.chinese.sequence.normalize_chinese(text)
    hans = phkit.chinese.sequence.normalize_english(hans)
    print('target_hans = ', f"'{hans}'")

    pins = phkit.text2pinyin(hans, errors=lambda x: [(w,) for w in x])
    print('target_pins = ', pins)

    phs = phkit.pinyin2phoneme(pins)
    phs = phkit.pinyinkit.change_diao(phs)
    print('target_phs = ', phs)

    seq = phkit.phoneme2sequence(phs)
    print('target_seq = ', seq)

    phs2 = phkit.text2phoneme(text)
    assert phs2 == target_phs

    pin_text = ' '.join([w if isinstance(w, str) else w[0].replace(' ', '#') for w in target_pins])
    seq3 = phkit.chinese_text_to_sequence(pin_text, cleaner_names='pinyin')
    pins3 = phkit.chinese_sequence_to_text(seq3).split()
    assert len(pins3) == len(target_pins)

    phs3 = phkit.chinese.sequence.sequence2phoneme(seq3)
    phs3 = phkit.chinese.pinyin.change_diao(phs3)
    assert phs3 == target_phs

    assert len(phkit.symbol_chinese) == 145

    text = "岂有此理"
    target = ['q', 'i', '2', '-', 'ii', 'iu', '3', '-', 'c', 'iy', '2', '-', 'l', 'i', '3', '-', '~', '_']
    result = phkit.text2phoneme(text)
    assert result == target

    text = "我的儿子玩会儿"
    target = ['uu', 'uo', '3', '-', 'd', 'e', '5', '-', 'ee', 'er', '2', '-', 'z', 'iy', '5', '-', 'uu', 'uan', '2',
              '-', 'h', 'ui', '4', '-', 'ee', 'er', '5', '-', '~', '_']
    result = phkit.text2phoneme(text)
    assert result == target


if __name__ == "__main__":
    print(__file__)
    test_phkit()

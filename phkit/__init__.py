#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/17
"""
![phkit](phkit.png "phkit")

## phkit
phoneme toolkit: 拼音相关的文本处理工具箱，中文和英文的语音合成前端文本解决方案。

#### 安装

```
pip install -U phkit
```
"""
__version__ = "0.2.11"

version_doc = """
#### 版本
v{}
""".format(__version__)

history_doc = """
### 历史版本
#### v0.2.10
- ttskit适配的音素工具。
"""

from phkit.chinese import __doc__ as doc_chinese
from phkit.chinese.symbol import __doc__ as doc_symbol
from phkit.chinese.sequence import __doc__ as doc_sequence
from phkit.chinese.pinyin import __doc__ as doc_pinyin
from phkit.chinese.phoneme import __doc__ as doc_phoneme
from phkit.chinese.number import __doc__ as doc_number
from phkit.chinese.convert import __doc__ as doc_convert
from phkit.chinese.style import __doc__ as doc_style
from .english import __doc__ as doc_english
from .pinyinkit import __doc__ as doc_pinyinkit

readme_docs = [__doc__, version_doc,
               doc_pinyinkit,
               doc_chinese, doc_symbol, doc_sequence, doc_pinyin, doc_phoneme, doc_number, doc_convert, doc_style,
               doc_english,
               history_doc]

from .chinese import text_to_sequence as chinese_text_to_sequence, sequence_to_text as chinese_sequence_to_text
from .english import text_to_sequence as english_text_to_sequence, sequence_to_text as english_sequence_to_text
from .pinyinkit import lazy_pinyin, pinyin, slug, initialize

# 兼容0.1.0之前的版本，python3.7以上版本支持。
from .chinese import convert, number, phoneme, sequence, symbol, style
from .chinese.style import guobiao2shengyundiao, shengyundiao2guobiao
from .chinese.convert import fan2jian, jian2fan, quan2ban, ban2quan
from .chinese.number import say_digit, say_decimal, say_number
from .chinese.pinyin import text2pinyin, split_pinyin
from .chinese.sequence import text2sequence, text2phoneme, pinyin2phoneme, phoneme2sequence, sequence2phoneme
from .chinese.sequence import symbol_chinese, ph2id_dict, id2ph_dict

if __name__ == "__main__":
    print(__file__)

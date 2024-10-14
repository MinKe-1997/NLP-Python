# -*- coding = utf-8 -*-
# @Time: 2024/10/14 上午9:14
# @Author: 风我风格
# @File: nltk库的使用.py
# @Email: 1090461393@qq.com
# @Software: PyCharm


"""
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
网站下载不下来只能自己手动下载nltk的语料库
nltk的预料库对中文不友好，中文不使用它.命名体识别和词性标注找不到预料库无法进行使用
"""
# 导入库
from nltk.tokenize import WordPunctTokenizer
from nltk.text import Text
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.chunk import RegexpParser


# 1.分词
# 输入字符串，即待处理的文本
input_str = "Today’s weather is good, very windy and sunny, we have no classes in the afternoon, We have to play basketball tomorrow."

# 搭建分词器对象
tokenizer = WordPunctTokenizer()  # WordPunctTokenizer 将字符串拆分为单词和标点符号，按空格和标点进行分割

# 使用分词器对输入字符串进行分词
tokens = tokenizer.tokenize(input_str)  # tokenize 方法返回一个分割后的单词列表，每个单词和标点符号为一个独立元素

# 将所有单词转换为小写字母，以确保单词的一致性（忽略大小写差异）
tokens = [word.lower() for word in tokens]  # 通过列表推导式将分词后的每个单词转化为小写

# 打印前五个分词后的单词，检查分词结果
print(tokens[:5])  # 输出列表中的前五个单词，方便快速查看分词后的前几个元素

# 2.创建文本对象对词进行分析
t = Text(tokens)
# 统计good这个词的出现次数
t.count("good")
t.index("good")
t.plot(8)
plt.show()

# 3.停用词
# 去掉换行符
stopwords.readme().replace("\n", " ")
# 可导入中文停用词
chinese_stopwords = stopwords.words('chinese')
# print(chinese_stopwords)
# 导入英文停用词并去掉换行符号
stopwords.raw('english').replace('\n', ' ')
# 所有单词小写
test_words = [word.lower() for word in tokens]
# 将分词后的单词列表转化为集合，以去除重复的单词（集合中的元素是唯一的）
test_words_set = set(test_words)
# 取目标文本与停用词文本的交集
common_stopwords = test_words_set.intersection(set(stopwords.words('english')))
for word in common_stopwords:
    print(word)
# 4.过滤停用词
filtered = [w for w in test_words_set if (w not in stopwords.words('english'))]
print(filtered)
# 5.分块
sentence = [('the', 'DT'), ('little', 'JJ'), ('yellow', 'JJ'), ('dog', 'NN'), ('died', 'VBD')]
grammer = "MY_NP: {<DT>?<JJ>*<NN>}"
cp = RegexpParser(grammer)
result = cp.parse(sentence)  # 进行分块
print(result)
result.draw()

# 6.词性标注和命名实体识别无法使用,没有找到语料库
"""
from nltk import ne_chunk
from nltk import pos_tag
tags = pos_tag(tokens)
sentence = "Edison went to Tsinghua University today"
print(ne_chunk(pos_tag(tokenizer.tokenize(sentence))))
"""

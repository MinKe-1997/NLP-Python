# -*- coding = utf-8 -*-
# @Time:  下午2:46
# @Author: 闵柯
# @File: 数据清洗实例.py
# @Software: PyCharm

import re
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer

class DataCleansing:
    def __init__(self):
        """简单的类不需要初始化函数,我一般保留这个结构"""
        pass
    def get_data(self, file_path):
        """获取原始数据"""
        # 读取原始数据
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        #  返回数据
        return data

    def get_stop_words(self):
        """获取停用词"""
        # 返回停用词文本
        return stopwords.words('english')

    def txt_clean(self, file_name_path):
        """
        清洗数据
        :param file_name_path: 源数据路径
        :return: 清洗后的文本数据
        """
        data = self.get_data(file_name_path)
        # 去掉HTML标签(e.g. & amp)
        text_no_special_entities = re.sub(r'\&\w*; |#\w*|@\w*', ' ', data)
        # 去掉一些价值符号
        text_no_tickers = re.sub(r'\$\w*','',text_no_special_entities)
        # 去掉超链接
        text_no_hyperlinks = re.sub(r'http?:\/\/.*\/\w*', '', text_no_tickers)
        # 去掉一些专有名词缩写
        text_no_small_words = re.sub(r'\b\w{1,2}\b', '', text_no_hyperlinks)
        # 去掉多余空格
        text_no_whitespaces = re.sub(r'\s+', ' ', text_no_small_words)
        text_no_whitespaces = text_no_whitespaces.lstrip()
        # 分词
        tokenizer = WordPunctTokenizer()
        tokens = tokenizer.tokenize(text_no_whitespaces)
        # 去停用词
        cache_english_stopwords = self.get_stop_words()
        list_no_stopwords = [i for i in tokens if i not in cache_english_stopwords]
        # 过滤后结果
        text_filtered = ' '.join(list_no_stopwords)
        # 返回过滤后的结果
        return text_filtered


if __name__ == '__main__':
    """主程序"""
    # 实例化对象
    data_clean = DataCleansing()
    # 原始数据
    data = data_clean.get_data(r"E:\Project\Pycharm\NLP_Project\CH1\data\text.txt")
    # 数据预处理
    text_filtered = data_clean.txt_clean(r"E:\Project\Pycharm\NLP_Project\CH1\data\text.txt")
    print(f"原始数据为:  {data}", "\n\n", f"过滤后的数据为:  {text_filtered}")








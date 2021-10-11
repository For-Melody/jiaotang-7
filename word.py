# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 21:16
# @Author :
# @File : word.py
# @Software : PyCharm
from pyecharts import options as opts
from pyecharts.charts import WordCloud


words = [
    ("知乎", "46"),
    ("B站", "94"),
    ("CSDN", "78"),
    ("博客园", "12"),
    ("百度", "150"),
    ("GitHub", "53"),
    ("菜鸟", "13"),
    ("中国大学MOOC", "22"),
    ("焦糖", "27"),
    ("模板之家", "16"),
    ("豆瓣", "33"),
    ("天猫", "5"),
    ("微博", "7"),
]

c = (
    WordCloud()
    .add(
        "",
        words,
        word_size_range=[20, 100],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-My_Web"))
    .render("wordcloud2.html")
)
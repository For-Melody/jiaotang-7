# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 20:38
# @Author :
# @File : jizuobiao.py
# @Software : PyCharm
from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker

c = (
    Polar()
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=Faker.web, type_="category"))
    .add("Count", [46, 94, 78, 12, 150,53,13,22,27,16,33,5,7], type_="bar", stack="stack0")
    .set_global_opts(title_opts=opts.TitleOpts(title="常用网站大全"))
    .render("jizuobiao.html")
)

# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 20:12
# @Author :
# @File : loudou.py
# @Software : PyCharm
import pyecharts.options as opts
from pyecharts.charts import Funnel


x_data = ["知乎", "B站", "CSDN", "博客园", "百度","GitHub","菜鸟","中国大学MOOC","焦糖","模板之家","豆瓣","天猫","微博"]
y_data = [46, 94, 78, 12, 150,53,13,22,27,16,33,5,7]

data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

(
    Funnel(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图", subtitle="我的常用网站真没20个"))
    .render("funnel_chart2.html")
)


# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 20:55
# @Author :
# @File : xiang.py
# @Software : PyCharm
from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType

location = ["知乎", "B站", "CSDN", "博客园", "百度","GitHub","菜鸟","中国大学MOOC","焦糖","模板之家","豆瓣","天猫","微博"]
values = [46, 94, 78, 12, 150,53,13,22,27,16,33,5,7]

c = (
    PictorialBar()
    .add_xaxis(location)
    .add_yaxis(
        "",
        values,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="我7天内最常浏览的网站"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("pictorialbar_base.html")
)


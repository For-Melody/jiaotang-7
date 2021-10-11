## 焦糖#7

* 链接：[Github](https://github.com/chynb/jiaotang-7)  

***

### 1.任务一

> 任务一我没找出数据但了解了缓存方式并找到了缓存地址和文件，不过不知道怎么转化为可读性文件

​		浏览器数据储存有前段缓存和后端缓存，基本的网络请求分为三步：请求，处理，相应（这当然不可能是我总结出来的）。在查找资料的过程中，我对前段缓存的印象最深，所以我就只谈谈我知道的吧，如果有错误恳请斧正。

* 1. 按储存位置分

     分别有Service Worker，Memory Cache，Disk Cache和网络请求

     * Service Worker

       如果浏览器有Service Worker那么开始就会优先从其中找缓存文件，这是一个强大的工具（其他程序猿说的），可以将网络资源存储在电脑本地中，从而在某些情况下（比如刷新操作）能节省时间以及节约成本（我的理解是请求数不变但返回文件大小变小）

     * Memory Cache

       在内存中缓存会使得计算机访问速度加快但同时也极不稳定，如果不小心关闭了网页那么缓存的内容也就会消失，跟内存上的内容在电脑关机后会清空一样  

     * Disk Cache

       磁盘中缓存肯定是最慢的，但好处是他的稳定性强，可以永久储存，并且因为磁盘的造价低廉（至少比内存，寄存器和高速缓存便宜的多）所以能够储存的大小也更大     

     * 网络请求

       就是网络发啥你收啥，前提是在以上三个地方都没找到缓存

* 2.按失效策略分

  ​	有强制缓存，协商缓存

  * 强制缓存

    如果有请求就看缓存库，有就直接返回，没有再请求服务器。这个方法能直接减少请求数。

    Expire和Cache-control是可以造成强缓存的字段，其中Expire是使用的绝对时间，如果用户更改本地时间会造成许多不可控的影响，所以一般应该不会使用，而另一个Cache-control则用的相对时间

  * 协商缓存

    强制缓存失效后才使用协商缓存，又服务器决定缓存内容是否失效。

    这种方法节省了响应体体积，因如果是304只会返回一个状态码。  

    ***

  > ​       这些是我了解到的缓存方式，我没有使用Chrome或者Fire Fox，而是用的QQ浏览器，所以我只找到了本地的缓存数据，也就是Disk Cache，在其中又找到了Service Worker，但文件基本无后缀使用各种方式打开也只是乱码，腾讯对这些数据进行隐藏加密我也见怪不怪了，实在是没找到怎么转化，虽然传输是使用二进制，但是在本地应该都会转化成可读性文件，像cookies应该是.txt，因为二进制文件基本上都是非可读性文件，都不可读了转化成文档也没什么意义  

***

### 2.任务二

> 这个任务我以放飞自我，因为时间太短我也就没怎么自己写代码，直接用了Echarts 来做数据可视化。
>
> 同时因为任务一的数据没有提取出来，我就直接用了历史记录来获取数据，代码只是一个计数器所以我就没必要放上来了  

对于Echarts这个工具，我一开始使用的版本是v0.5.x，使用的时候报了许多bug，最多的就是缺少某一个库，通过pip install 指令下载后也无法运行，后来查找资料才得知那个版本已经停止更新，所以又升级了版本，但依然报错，在网上查找资料后才发现类等已经被封装好了，我再次编写才导致类名相同而报错

* 1.漏斗图

  ```python
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
  ```

Echarts的封装很好所以基本不用自己写什么代码，只需要使用提供的库就能画出图，所以代码我就不标注注释了

**这是效果图：**

![avatar](https://wx3.sinaimg.cn/mw690/006w6fGHly1gvbr81i7a4j61hc0pk0xu02.jpg))

> 我将图片传在我的微博上所以有水印  

* 2.极坐标图

  ```python
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
  ```

**效果图：**

![avatar](https://wx1.sinaimg.cn/mw690/006w6fGHly1gvbr8113npj60u20knaco02.jpg)

* 3.象形图

  ```python
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
  ```

**效果图：**

![avatar](https://wx1.sinaimg.cn/mw690/006w6fGHly1gvbr8203d7j60x40g3gpo02.jpg)

* 4.词云图

  ```python
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
  ```

**效果图:**

![avatar](https://wx2.sinaimg.cn/mw690/006w6fGHly1gvbr828f48j60th0h2ad402.jpg)

> ps：每次刷新会变换位置

因为时间比较紧所以后面写的就不是那么详细了（简直是不详细了 (ノへ￣、)）

***

附加Pcharm和Ananconda（混个加分 (๑•̀ㅂ•́)و✧）

![avatar](https://wx2.sinaimg.cn/mw690/006w6fGHly1gvbrr9qtcrj60xz0hqmzz02.jpg)



![avatar](https://wx1.sinaimg.cn/mw690/006w6fGHly1gvbrra1xhtj60r40kgjy602.jpg)
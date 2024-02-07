# CampusCanteenAnalytics-tk

# 项目简介
这个食堂数据分析应用程序通过Tkinter GUI提供了直观的界面，让用户能够浏览、比较和分析不同食堂的关键数据。用户可以查看各食堂的人均消费排名，了解特定食堂的菜品受欢迎程度，并根据不同标准（如周人流量、周营业额、投诉情况等）进行排名。此外，应用程序还展示了投诉情况的分布。通过提供交互式操作，用户能够选择关注的食堂和排名标准。
# 效果展示
![\[图片\]](https://img-blog.csdnimg.cn/direct/6e2042add22f4982b70d523e37c05b30.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/85ceb5157d3e4d2782f1a43033fe5126.png)

# 数据纵览
总.xlsx
![\[图片\]](https://img-blog.csdnimg.cn/direct/053de2aabb214a59bb7e7ac5f1ce12fc.png)

田园菜单.xlsx、百业菜单.xlsx、龙山菜单.xlsx的数据格式都大致如下。
![\[图片\]](https://img-blog.csdnimg.cn/direct/5b9237186825485da5f8f1dfca476679.png)

# 项目思路
1. 加载数据：
  - 从Excel文件加载总体数据到名为zong的数据框。
  - 从Excel文件加载田园菜单数据到名为TainYuan的数据框。
  - 从Excel文件加载百业菜单数据到名为BaiYe的数据框。
  - 从Excel文件加载龙山菜单数据到名为LongShan的数据框。
2. 创建Tkinter窗口：
  - 创建一个Tkinter窗口并设置标题为“食堂数据分析”。
3. 定义显示排名的函数：
  - display_ranking函数用于显示基于人均消费的食堂排名。
  - display_menu_ranking函数用于显示特定食堂菜品排名。
  - display_ranking_criteria函数用于显示指定标准的排名。
  - display_complaint_distribution函数用于显示投诉情况的饼图。
4. 定义按钮点击事件函数：
  - button_click函数处理按钮点击事件，根据所选食堂调用相应的显示函数。
5. 创建菜单栏：
  - 创建菜单栏包括排名标准和食堂选项的子菜单。
6. 设置排名标准的菜单项选择：
  - 为排名标准创建子菜单，并定义选择该项时的回调函数。
7. 设置食堂选项的菜单：
  - 为食堂选项创建子菜单，并定义选择该项时的回调函数。
8. 显示初始排名：
  - 使用display_ranking_criteria函数显示初始的人均消费排名。
9. 处理投诉情况分布：
  - 使用display_complaint_distribution函数显示投诉情况分布。
10. 运行Tkinter事件循环：
  - 启动Tkinter的事件循环，使窗口可以响应用户操作。

# 具体讲解链接
CSDN：https://blog.csdn.net/m0_46573428/article/details/136068944
# 后记
如果觉得有帮助的话，求 关注、收藏、点赞、星星 哦！

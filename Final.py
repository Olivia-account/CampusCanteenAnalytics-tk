import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# 设置背景颜色
bg_color = (240, 240, 240)
# 将背景颜色转换为十六进制格式
bg_color_hex = "#{:02x}{:02x}{:02x}".format(*bg_color)

# 设置图表字体配置
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
# 确保图表中负号的正确显示
plt.rcParams['axes.unicode_minus'] = False

# 加载每个食堂的数据
# 从Excel文件加载总体数据到名为zong的数据框
zong = pd.read_excel('总.xlsx')

# 从Excel文件加载田园菜单数据到名为TainYuan的数据框
TainYuan = pd.read_excel('田园菜单.xlsx')

# 从Excel文件加载百业菜单数据到名为BaiYe的数据框
BaiYe = pd.read_excel('百业菜单.xlsx')

# 从Excel文件加载龙山菜单数据到名为LongShan的数据框
LongShan = pd.read_excel('龙山菜单.xlsx')

# 计算'zong'数据框中的人均消费
zong['人均消费'] = zong['周营业额'] / zong['周人流量']

# 创建Tkinter窗口
window = tk.Tk()
# 设置Tkinter窗口标题
window.title("食堂数据分析")

# 函数：显示基于人均消费的食堂排名
def display_ranking(df, title):
    # 清除先前的图表
    plt.clf()
    # 创建具有指定大小和背景颜色的新图表
    plt.figure(figsize=(9, 3.5), facecolor=bg_color_hex)

    # 绘制水平条形图，显示人均消费
    plt.barh(df['餐厅名称'], df['人均消费'], color='#3498db', \
             edgecolor='black', linewidth=0.5)

    # 用值注释数据点
    for index, value in enumerate(df['人均消费']):
        plt.text(value, index, f'{value:.2f} 元', ha='left', \
                 va='center', fontsize=10)

    # 设置图表的标题、标签和网格
    plt.title(title + '人均消费排名', fontsize=14, fontweight='bold')
    plt.ylabel('餐厅名称', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.6)

    # 在Tkinter窗口中显示图表
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()

    # 销毁先前的画布，以避免重叠
    if hasattr(display_ranking, 'tk_canvas'):
        display_ranking.tk_canvas.get_tk_widget().destroy()
    canvas.get_tk_widget().pack()

    # 保存新画布以供将来参考
    display_ranking.tk_canvas = canvas

# 函数：显示特定食堂菜品排名
def display_menu_ranking(df, title):
    # 获取基于'评分'列的前3行
    top3 = df.nlargest(3, '评分')

    # 创建具有指定大小和背景颜色的新图表
    plt.figure(figsize=(9, 5), facecolor=bg_color_hex)

    # 绘制水平条形图，显示菜品排名
    plt.barh(df[title+'菜品'], df['评分'], color='#2ecc71', \
             edgecolor='black', linewidth=0.5)
    
    # 使用散点图突出前3个菜品，用红色星星表示
    plt.scatter(top3['评分'], top3[title+'菜品'], color='red', \
                marker='*', s=100, label='Top 3')
    
    # 用值注释数据点
    for index, value in enumerate(df['评分']):
        plt.text(value, index, f'{value:.2f} ', ha='left', \
                 va='center', fontsize=10)
    
    # 设置图表的标题、标签、图例和网格
    plt.title(title + '菜品评分排名', fontsize=14, fontweight='bold')
    plt.ylabel('菜品', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.6)

    # 在Tkinter窗口中显示图表
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()

    # 销毁先前的画布，以避免重叠
    if hasattr(display_menu_ranking, 'tk_canvas'):
        display_menu_ranking.tk_canvas.get_tk_widget().destroy()
    canvas.get_tk_widget().pack()

    # 保存新画布以供将来参考
    display_menu_ranking.tk_canvas = canvas

# 函数：处理按钮点击事件
def button_click(cafeteria):
    # 根据所选食堂调用display_menu_ranking函数
    if cafeteria == '田园菜单':
        display_menu_ranking(TainYuan, '田园食堂')
    elif cafeteria == '百业菜单':
        display_menu_ranking(BaiYe, '百业广场')
    elif cafeteria == '龙山菜单':
        display_menu_ranking(LongShan, '龙山食堂')

# 函数：显示指定标准的排名
def display_ranking_criteria(df, column, title):
    # 获取基于指定列的前3行
    top3 = df.nlargest(3, column)

    # 创建具有指定大小和背景颜色的新图表
    plt.figure(figsize=(9, 4), facecolor=bg_color_hex)

    # 绘制所有食堂的水平条形图
    plt.barh(df['餐厅名称'], df[column], color='#3498db', \
             edgecolor='black', linewidth=0.5)
    
    # 使用散点图突出前3个食堂，用红色星星表示
    plt.scatter(top3[column], top3['餐厅名称'], \
                color='red', marker='*', s=100, label='Top 3')
    
    # 用值注释数据点
    for index, value in enumerate(df[column]):
        annotation = f'{value:.2f}'
        plt.text(value, index, annotation, ha='left', \
                 va='center', fontsize=10)
    
    # 设置图表的标题、标签和网格
    plt.title(title + f'{column}排名', fontsize=14, fontweight='bold')
    plt.ylabel('餐厅名称', fontsize=12)
    # plt.grid(axis='x', linestyle='--', alpha=0.6)

    # 在Tkinter窗口中显示图表
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()

    # 销毁先前的画布，以避免重叠
    if hasattr(display_ranking_criteria, 'tk_canvas'):
        display_ranking_criteria.tk_canvas.get_tk_widget().destroy()
    canvas.get_tk_widget().pack()

    # 保存新画布以供将来参考
    display_ranking_criteria.tk_canvas = canvas


def display_complaint_distribution(df, title):
    # 获取分布
    complaints_distribution = Counter(df['情况'])
    
    # 创建具有指定大小和背景颜色的新图表
    plt.figure(figsize=(8, 8), facecolor=bg_color_hex)
    
    # 绘制分布
    plt.pie(complaints_distribution.values(), \
            labels=complaints_distribution.keys(), \
                autopct='%1.1f%%', startangle=140)
    
    # 设置图表的标题
    plt.title(title + '情况分布', fontsize=14, fontweight='bold')

    # 在Tkinter窗口中显示图表
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()

    # 销毁先前的画布，以避免重叠
    if hasattr(display_complaint_distribution, 'tk_canvas'):
        display_complaint_distribution.tk_canvas.get_tk_widget().destroy()
    canvas.get_tk_widget().pack()

    # 保存新画布以供将来参考
    display_complaint_distribution.tk_canvas = canvas


# 函数：处理排名标准的菜单项选择
def menu_select_criteria(column):
    display_ranking_criteria(zong, column, '食堂')

# 创建菜单栏
menu_bar = tk.Menu(window)

# 创建排名标准的菜单
ranking_menu = tk.Menu(menu_bar, tearoff=0)

# 将排名标准选项添加到菜单中
# 将“周人流量排名”添加到排名标准菜单，并定义选择该项时的回调函数
ranking_menu.add_command(label="周人流量排名", \
                         command=lambda: menu_select_criteria('周人流量'))

# 将“周营业额排名”添加到排名标准菜单，并定义选择该项时的回调函数
ranking_menu.add_command(label="周营业额排名", \
                         command=lambda: menu_select_criteria('周营业额'))

# 将“投诉情况排名”添加到排名标准菜单，并定义选择该项时的回调函数
ranking_menu.add_command(label="投诉情况排名", \
                         command=lambda: menu_select_criteria('投诉情况'))

# 将“环境打分排名”添加到排名标准菜单，并定义选择该项时的回调函数
ranking_menu.add_command(label="环境打分排名", \
                         command=lambda: menu_select_criteria('环境打分'))

# 将“饮食习惯排名”添加到排名标准菜单，并定义选择该项时的回调函数
ranking_menu.add_command(label="饮食习惯排名", \
                         command=lambda: menu_select_criteria('饮食习惯'))

# 将“食物安全排名”添加到排名标准菜单，并定义选择该项时的回调函数
ranking_menu.add_command(label="食物安全排名", \
                         command=lambda: menu_select_criteria('食物安全'))

# 将“营养均衡排名”添加到排名标准菜单，并定义选择该项时的回调函数
ranking_menu.add_command(label="营养均衡排名", \
                         command=lambda: menu_select_criteria('营养均衡'))

# 将排名标准菜单添加到菜单栏
menu_bar.add_cascade(label="排名", menu=ranking_menu)

# 创建食堂选项的菜单
cafeteria_menu = tk.Menu(menu_bar, tearoff=0)

# 将食堂选项添加到菜单中
# 向食堂选项菜单中添加“田园菜单”命令，并定义选择该项时的回调函数
cafeteria_menu.add_command(label="田园菜单", \
                           command=lambda: button_click('田园菜单'))

# 向食堂选项菜单中添加“百业菜单”命令，并定义选择该项时的回调函数
cafeteria_menu.add_command(label="百业菜单", \
                           command=lambda: button_click('百业菜单'))

# 向食堂选项菜单中添加“龙山菜单”命令，并定义选择该项时的回调函数
cafeteria_menu.add_command(label="龙山菜单", \
                           command=lambda: button_click('龙山菜单'))

# 将食堂菜单添加到菜单栏
menu_bar.add_cascade(label="食堂菜单", menu=cafeteria_menu)

# 为窗口设置菜单栏
window.config(menu=menu_bar)

# 显示初始的人均消费排名
display_ranking_criteria(zong, '人均消费', '食堂')

# 导入用于计算投诉分布的所需模块
from collections import Counter

# 函数：显示投诉分布的饼图
def display_complaint_distribution(df, title):
    # 获取投诉分布
    complaints_distribution = Counter(df['投诉情况'])
    
    # 创建具有指定大小和背景颜色的新图表
    plt.figure(figsize=(8, 8), facecolor=bg_color_hex)
    
    # 绘制投诉分布的饼图
    plt.pie(complaints_distribution.values(), \
            labels=complaints_distribution.keys(), \
            autopct='%1.1f%%', startangle=140)
    
    # 为图表设置标题
    plt.title(title + '投诉情况分布', fontsize=14, fontweight='bold')

    # 在Tkinter窗口中显示图表
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()

    # 销毁先前的画布，以避免重叠
    if hasattr(display_complaint_distribution, 'tk_canvas'):
        display_complaint_distribution.tk_canvas.get_tk_widget().destroy()
    canvas.get_tk_widget().pack()

    # 保存新画布以供将来参考
    display_complaint_distribution.tk_canvas = canvas

# 运行Tkinter事件循环
window.mainloop()

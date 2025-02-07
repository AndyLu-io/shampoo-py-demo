import seaborn as sns
import matplotlib.pyplot as plt

# 绘制箱线图
sns.boxplot(x='category', y='value', data=df)
plt.show()

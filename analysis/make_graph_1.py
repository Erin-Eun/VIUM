# %%
from unique_labels import * 

#=======================================
# Graph 1
#=======================================

# 값(value) 기준으로 오름차순 정렬
label_set = sorted(label_set.items(), 
                   reverse=True,
                   key=lambda x:x[1])
label_set = dict(label_set)
# print(label_set)

x = list(label_set.keys())
y = list(label_set.values())

plt.figure(figsize=(10, 10))
sns.barplot(y, x, palette='deep')
plt.title('Number of Labels', fontsize=20)

for i, v in enumerate(y):
    plt.text(v+0.6, i+0.1, v)

plt.show()
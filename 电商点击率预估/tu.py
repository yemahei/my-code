import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5, 6]
y1 = [1050, 2300,3800,5060,7360,9999]

x2 = [1, 2, 3, 4, 5, 6]
y2 = [1000,1800, 2400, 3600, 5700, 7600]

x3 = [1, 2, 3, 4, 5, 6]
y3 = [950, 1670,2250,3300,4790,6490]

x4 = [1, 2, 3, 4, 5, 6]
y4 = [1000,1800, 2400, 3600, 5700, 7600]
group_labels = ['378', '624', '988', '1306', '1690', '2036']
plt.title('S-apriori vs D-apriori')
plt.xlabel('data size')
plt.ylabel('time(ms)')

# plt.plot(x1, y1,'r', label='broadcast')
# plt.plot(x2, y2,'b',label='join')
# plt.xticks(x1, group_labels, rotation=0)

plt.plot(x3, y3, 'c', label='D-apriori')
plt.plot(x4, y4, 'r', label='S-apriori')
plt.xticks(x3, group_labels, rotation=0)

plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()
#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''

# s1 = 72
# s2 = 85
# r = s1 + s2
# print('%.1f'%r)

#input
# price=input('price=')
# p=int(price)
# if p>1000:
#     print('no')
# else:
#     print('yes')

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖
'''
# height = float(input('height='))
# weight = float(input('weight='))
# BMI = weight/height**2
#
# if BMI<=18.5:
#     print('过轻')
# elif BMI>18.5 and BMI<=25:
#     print('正常')
# else:
#     print('过重')

#请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Me','He','She']
for name in L:
    print(name)

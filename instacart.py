import sqlite3
import numpy as np
#from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt 
import pandas as pd
from collections import Counter

pd.set_option('display.max_rows',200)

sqlite_file = '/Users/john/Documents/CDL/instacart.db'
table_orders = 'orders'
table_orders_products = 'orders_products'
table_products = 'products'
table_aisles = 'aisles'
table_departments = 'departments'
id_column = 'order_id'
user_id = 'user_id'

#connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
d = conn.cursor()

#c.execute('SELECT orders.order_id, order_products.product_id AS productID, products.product_name AS product FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id INNER JOIN products on products.product_id = order_products.product_id WHERE orders.order_id = 2168274;')
#c.execute('SELECT products.product_name AS product, COUNT (products.product_name) AS cnt FROM products INNER JOIN order_products on order_products.product_id = products.product_id INNER JOIN orders ON orders.order_id = order_products.order_id GROUP BY product ORDER BY cnt DESC LIMIT 100;')


########## Most ordered items###########
#mypd = pd.read_sql_query('SELECT products.product_name AS product, COUNT (products.product_name) AS cnt FROM products INNER JOIN order_products on order_products.product_id = products.product_id INNER JOIN orders ON orders.order_id = order_products.order_id GROUP BY product ORDER BY cnt DESC LIMIT 10;',conn)
# c.execute('SELECT products.product_name AS product, COUNT (products.product_name) AS cnt FROM products INNER JOIN order_products on order_products.product_id = products.product_id INNER JOIN orders ON orders.order_id = order_products.order_id GROUP BY product ORDER BY cnt DESC LIMIT 10;')
# product = []
# count = []
# for row in c.fetchall():
#     product.append(row[0])
#     count.append(row[1])

# plt.bar(product, count)
# plt.xticks(rotation='vertical')
# plt.subplots_adjust(bottom=0.45)
# plt.ylabel('Count')
# plt.show()
#########################################


############### number of orders per person
# c.execute('SELECT  orders.user_id, orders.order_number AS cnt FROM orders ORDER BY orders.order_number DESC;')
# mylist = []
# mydict = {}
# for num in range(1,101):
#     mydict[num] = []
#     #print(num)
# for row in c.fetchall():
#     if row[0] in mylist:
#         continue
#     mylist.append(row[0])
#     mydict[row[1]].append(row[0])
# finaldict ={}
# for key in mydict:
#     finaldict[key]=len(mydict[key])
# #print(mysql)
# #results = c.fetchall()
# #print(results)
# c.close()
# conn.close()

# plt.bar(finaldict.keys(), finaldict.values(), color='g')
# plt.xlabel('Number or Orders Per User')
# plt.ylabel('Frequency')
# plt.show()
###########################################################

######### One time users##################################
# c.execute('SELECT  orders.user_id, orders.order_number AS cnt, orders.order_id FROM orders ORDER BY orders.order_number DESC;')
# d.execute('SELECT  orders.user_id, orders.order_number AS cnt, orders.order_id FROM orders ORDER BY orders.order_number DESC;')

# mylist = []
# mydict = {}
# for num in range(1,101):
#     mydict[num] = []
#     #print(num)
# for row in c.fetchall():
#     if row[0] in mylist:
#         continue
#     mylist.append(row[0])
#     mydict[row[1]].append(row[0])
# low_order = []

# #for key in mydict:
# #    #print(type(key))
# #    print(key, mydict[key])
# #print(mydict[1])
# for row in d.fetchall():
#     #print(row[0])
#     #print(mydict[1])
#     for num in range(90,101):
#         if row[0] in mydict[num]:
#             low_order.append(row[2])
# mypd = pd.read_sql_query('SELECT products.product_name AS product, COUNT (products.product_name) AS cnt FROM products INNER JOIN order_products on order_products.product_id = products.product_id INNER JOIN orders ON orders.order_id = order_products.order_id WHERE orders.order_id IN %s GROUP BY product ORDER BY cnt DESC LIMIT 10;' % str(tuple(low_order)),conn)
# #print(type(mypd.product), type(mypd.cnt))
# e1 = mypd.product()
# print(mypd.cnt)
# plt.bar(product, count)
# plt.xticks(rotation='vertical')
# plt.subplots_adjust(bottom=0.45)
# plt.ylabel('Count')
# plt.show()
# ##################################################################

########DOW######################
# c.execute('SELECT  orders.order_dow AS dow FROM orders;')

# dummy_list = []
# for row in c.fetchall():
#     dummy_list.append(row[0])

# bins=[0,1,2,3,4,5,6]
# plt.hist(dummy_list, color='g',bins=np.arange(0,8,1),rwidth=0.8,align='left')
# plt.xlabel('Day of Week')
# plt.ylabel('Count')
# plt.show()

# c.close()
# conn.close()
######################################


################Order time#################
# c.execute('SELECT  orders.Order_hour_of_day AS hour FROM orders;')

# dummy_list = []
# for row in c.fetchall():
#     dummy_list.append(row[0])

# bins=[0,1,2,3,4,5,6]
# plt.hist(dummy_list, color='g',bins=np.arange(0,26,1),rwidth=0.8,align='left')
# plt.xlabel('Hour of Order')
# plt.ylabel('Count')
# plt.show()

# c.close()
# conn.close()
##############################################

################Days since last order###########
# c.execute('SELECT  orders.Days_Since_Prior_Order AS hour FROM orders;')


# dummy_list = []
# for row in c.fetchall():
#     if type(row[0]) == float:
#         dummy_list.append(row[0])

# bins=[0,1,2,3,4,5,6]
# plt.hist(dummy_list, color='g',bins=np.arange(0,32,1),rwidth=0.8,align='left')
# plt.xlabel('Days Since Last Order')
# plt.ylabel('Count')
# plt.show()

# c.close()
# conn.close()
##################################################

##############Number of items per order#############
# c.execute('SELECT order_products.order_id, order_products.product_id FROM order_products;')

# dummy_list=[]
# for row in c.fetchall():
#     dummy_list.append(row[0])
# mydict=Counter(dummy_list)


# plt.hist(mydict.values(), color='g',bins=np.arange(0,61,1),rwidth=0.8,align='left')
# plt.xlabel('Number of Items per Order')
# plt.ylabel('Count')
# plt.show()

# c.close()
# conn.close()

############################################


######## number of items vs days since last order#############




#############################################

########## Reordered?
# c.execute('SELECT orders.order_id, order_products.product_id, order_products.reordered FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id;')

# dummy_list = []
# for row in c.fetchall():
#     dummy_list.append(row[2])

# print(sum(dummy_list),len(dummy_list))
# c.close()
# conn.close()

# plt.bar((0,1), (len(dummy_list)-sum(dummy_list),sum(dummy_list)), color='g')
# ax = plt.axes()
# ax.xaxis.set_major_locator(plt.MaxNLocator(2))
# ax.xaxis.set_ticklabels(('','No','Yes'))
# ax.set_xlabel('Repurchased')
# ax.set_ylabel('Count')
# plt.show()
#####################


################ Reordered vs Day since last order
# c.execute('SELECT orders.order_id, orders.Days_Since_Prior_Order, order_products.product_id, order_products.reordered FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id;')

# reordered_list = []
# day_list = []
# mydict = {}

# for num in range(0,31):
#     mydict[num] = []
# for row in c.fetchall():
#     if type(row[1])==float:
#         mydict[row[1]].append(row[3])
# finaldict ={}
# for key in mydict:
#     perc = sum(mydict[key])/len(mydict[key])
#     finaldict[key] = perc

# plt.bar(finaldict.keys(), finaldict.values(), color='g')
# plt.xlabel('Day Since Last Order')
# plt.ylabel('Percentage of Reordered Items')
# plt.show()

#####################################################


################# Days since vs number of items per order
# c.execute('SELECT  orders.order_id, orders.Days_Since_Prior_Order, order_products.product_id FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id;')


# days_dict ={}
# order_dict = {}
# for num in range(0,9999999):
#     days_dict[num] = []
# for row in c.fetchall():
#     if type(row[1]) == float:
#         days_dict[row[0]].append(row[1])
# xlist=[]
# ylist=[]
# for key in days_dict:  
#     if len(days_dict[key]) > 0:
#         xlist.append(days_dict[key][0])
#         ylist.append(len(days_dict[key]))
# mydict={}
# for day in xlist:
#     mydict[day] = []
# for (day,item) in zip(xlist,ylist):
#     #print(day, item)
#     mydict[day].append(item)
# finalx = []
# finaly = []
# for key in mydict:
#     finalx.append(key)
#     finaly.append(sum(mydict[key])/len(mydict[key]))
    
# plt.scatter(finalx,finaly)
# plt.xlabel('Days Since Prior Order')
# plt.ylabel('Average Number of Items In Order')
# plt.show()

###################################################################

######### time of day vs day of week

# c.execute('SELECT  orders.Order_hour_of_day AS hour, orders.order_dow FROM orders;')

# mydict = {}
# for num in range(0,7):
#     mydict[num] = []
# for row in c.fetchall():
#     mydict[row[1]].append(row[0])
# xlist=[]
# ylist=[]
# xhist = []
# yhist = []
# for key in mydict:
#     #print(key)
#     xlist.append(key)
#     ylist.append(sum(mydict[key])/len(mydict[key]))
#     for val in range(len(mydict[key])):
#         xhist.append(key)
#         yhist.append(mydict[key][val])
# # for (x1,y1) in zip(xhist,yhist):
# #     print(x1,y1)

# # print(x)
# # print('here')
# # print(y)
# bins=[0,1,2,3,4,5,6]
# #plt.scatter(xlist,ylist)
# plt.hist2d(xhist,yhist,bins = (np.arange(0,8,1),np.arange(0,25,1)))
# plt.xlabel('DOW')
# plt.ylabel('Hour')
# plt.show()

# c.close()
# conn.close()

########################### Demographic

#c.execute('SELECT orders.order_id, orders.user_id, order_products.product_id, products.product_name FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id INNER JOIN products ON products.product_id = order_products.product_id LIMIT 1;')
# c.execute('SELECT orders.order_id, orders.user_id FROM orders;')

# userdict = {}
# orderdict = {}
# for var in range(0,500000):
#     userdict[var] = []

# percdict={}

# # for row in c.fetchall():
# #     userdict[row[1]][row[0]].append(row[3])

# # for user in userdict:
# #     for order in userdict[user]:
# #         print(order)
# orderid = 0
# for row in c.fetchall():
#     # print(row)
#     userdict[row[1]].append(row[0])
# c.close()
# perc = []
# for user1 in userdict:
#     if len(userdict[user1]) == 0:
#         continue
#     total_orders = len(userdict[user1])
#     feminine_orders = 0
#     for order1 in userdict[user1]:
#         # print(order1)
#         #if len(order1) == 0:
#         #    continue
#         #if len(order1)>1:
#         #    mypd = pd.read_sql_query('SELECT orders.order_id, orders.user_id, order_products.product_id, products.product_name FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id INNER JOIN products ON products.product_id = order_products.product_id WHERE orders.order_id IN %s'% str(tuple(order1)),conn)
#         #else:
#         mypd = pd.read_sql_query('SELECT orders.order_id, orders.user_id, order_products.product_id, products.product_name FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id INNER JOIN products ON products.product_id = order_products.product_id WHERE orders.order_id = %s'% str((order1 )),conn)
#         # print(user1)
#         # print(mypd.order_id)
#         # print(mypd.product_name)
#         for val in mypd.product_name:
#             if val.find('Tampon') > 0 or val.find('Women') > 0 or val.find('Women') > 0:
#                 feminine_orders =+ 1
#         del(mypd)
#     perc.append(feminine_orders/total_orders)
#     print(feminine_orders/total_orders)
# plt.hist(perc,color='g',bins=np.arange(0,0.5,.001),align='left')
# plt.show()
        
        
    
        

#conn.close()



#################  number of items per order vs reorder %
# c.execute('SELECT  orders.order_id, order_products.reordered, order_products.product_id FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id;')


# reorder_dict ={}
# order_dict = {}
# for num in range(0,9999999):
#     order_dict[num] = []
# for row in c.fetchall():
#     # if type(row[1]) == float:
#     order_dict[row[0]].append(row[1])

# perc_list = []
# tot_list = []

# mydict= {}
# for num in range(1,1000):
#     mydict[num] = []
# for key in order_dict:  
#     if len(order_dict[key]) > 0:
#         perc = sum(order_dict[key])/len(order_dict[key])
#         total = len(order_dict[key])
#         #print(perc, total)
#         mydict[total].append(perc)
#         perc_list.append(perc)
#         tot_list.append(total)



# # mydict={}
# # for day in xlist:
# #     mydict[day] = []
# # for (day,item) in zip(xlist,ylist):
# #     #print(day, item)
# #     mydict[day].append(item)
# finalx = []
# finaly = []
# for key in mydict:
#     print(key,mydict[key])
#     if len(mydict[key]) < 1:
#         continue
#     finalx.append(key)
    
#     finaly.append(sum(mydict[key])/len(mydict[key]))
    
# plt.scatter(finalx,finaly)#,bins = (np.arange(0,60,5),np.arange(0,1,0.1)))
# plt.xlabel('Number of Items in Order')
# plt.ylabel('Average Percent of Reorders')
# plt.show()

################### Number of items from department

c.execute('SELECT orders.order_id, order_products.product_id, products.department_id, departments.Department FROM orders INNER JOIN order_products ON order_products.order_id = orders.order_id INNER JOIN products ON products.product_id = order_products.product_id INNER JOIN departments ON departments.Department_Id = products.department_id;')

mydict={}
deps = ['alcohol','babies','bakery','beverages','breakfast','bulk','canned goods','dairy eggs','deli','dry goods pasta','frozen','household','international','meat seafood','missing','other','pantry','personal care','pets','produce','snacks']
for num in deps:
    mydict[num] = 0
for row in c.fetchall():
    mydict[row[3]] += 1

plt.bar(mydict.keys(),mydict.values())
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.45)
plt.ylabel('Count')
plt.show()
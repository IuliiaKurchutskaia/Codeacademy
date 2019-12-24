#Cool T-Shirts Inc. has asked you to analyze data on visits to their website. 
#Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.

#In this case, our funnel is going to describe the following process:

#A user visits CoolTShirts.com
#A user adds a t-shirt to their cart
#A user clicks “checkout”
#A user actually purchases a t-shirt4

import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head()) 
print(cart.head()) 
print(checkout.head()) 
print(purchase.head()) 

#How many of the timestamps are null for the column cart_time?
visits_cart=pd.merge(visits, cart, how='left')
len_visits_cart=len(visits_cart)
print(len_visits_cart)
cart_time_null=len(visits_cart[visits_cart.cart_time.isnull()])
print(cart_time_null)

percent_visited=float(cart_time_null)/len_visits_cart
print(percent_visited)

#Repeat the left merge for cart and checkout and count null values. 
#What percentage of users put items in their cart, but did not proceed to checkout?

checkout_cart=pd.merge(cart, checkout, how='left')
len_checkout_cart=len(checkout_cart)
print(len_checkout_cart)
checkout_cart_null=len(checkout_cart[checkout_cart.checkout_time.isnull()])
percent_visited=float(checkout_cart_null)/len_checkout_cart
print(percent_visited)

#Merge all four steps of the funnel, in order, using a series of left merges. 
#What percentage of users proceeded to checkout, but did not purchase a t-shirt?
all_data=visits.merge(cart, how='left')\
   .merge(checkout, how='left')\
   .merge(purchase, how='left')
print(all_data)
len_all_data=len(all_data)
all_data_null=len(all_data[all_data.purchase_time.isnull()])
print(all_data_null)
percent_purchase=float(all_data_null)/len_all_data
print(percent_purchase)

#Average Time to Purchase
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())

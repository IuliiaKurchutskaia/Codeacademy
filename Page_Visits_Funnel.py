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

visits_cart=pd.merge(visits, cart, how='left')
len_visits_cart=len(visits_cart)
print(len_visits_cart)
cart_time_null=len(visits_cart[visits_cart.cart_time.isnull()])
print(cart_time_null)

percent_visited=float(cart_time_null)/len_visits_cart
print(percent_visited)
#Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?

checkout_cart=pd.merge(cart, checkout, how='left')
len_checkout_cart=len(checkout_cart)
print(len_checkout_cart)
checkout_cart_null=len(checkout_cart[checkout_cart.checkout_time.isnull()])
print(checkout_cart_null)

percent_visited=float(checkout_cart_null)/len_checkout_cart
print(percent_visited)
all_data=visits.merge(cart, how='left')\
   .merge(checkout, how='left')\
   .merge(purchase, how='left')
print(all_data)
len_all_data=len(all_data)
print(len_all_data)
all_data_null=len(all_data[all_data.purchase_time.isnull()])
print(all_data_null)

percent_purchase=float(all_data_null)/len_all_data
print(percent_purchase)


all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())

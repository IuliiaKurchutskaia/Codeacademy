#A/B Testing for ShoeFly.com
#Our favorite online shoe store, ShoeFly.com is performing an A/B Test. 
#They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google.
#They want to know how the two ads are performing on each of the different platforms on each day of the week. 
#Help them analyze the data using aggregate measures.



import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())   #.Examine the first few rows of ad_clicks.
#How many views (i.e., rows of the table) came from each utm_source
ad_clicks.groupby('utm_source')\
    .user_id.count()\
    .reset_index()

ad_clicks['is_click'] = ~ad_clicks\   #Create a new column called is_click, 
   .ad_click_timestamp.isnull()  #which is True if ad_click_timestamp is not null and False otherwise.
 
    #We want to know the percent of people who clicked on ads from each utm_source
clicks_by_source=ad_clicks.groupby(['utm_source', 'is_click']).user_id.count()\
.reset_index()
clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])

#Now let’s pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.
ad_clicks.groupby('experimental_group')\
    .user_id.count()\
    .reset_index()
#Create a new column in clicks_pivot called percent_clicked which is equal to the percent
# of users who clicked on the ad from each utm_source.
print(ad_clicks.groupby(['experimental_group', 'is_click'])\
    .user_id.count()\
    .reset_index()\
    .pivot(
      index='experimental_group',
      columns='is_click',
      values='user_id')\
    .reset_index()
 )

a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']
b_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'B']

#he column experimental_group tells us whether the user was shown Ad A or Ad B.
#The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.
a_clicks_pivot=a_clicks\
    .groupby(['is_click','day']).user_id\
    .count()\
    .reset_index()\
    .pivot(
      index='day',
      columns='is_click',
      values='user_id')\
    .reset_index()
a_clicks_pivot[' percent of users']=             a_clicks_pivot[True]/(a_clicks_pivot[True] + a_clicks_pivot[False])
b_clicks_pivot=b_clicks\
    .groupby(['is_click','day']).user_id\
    .count()\
    .reset_index()\
    .pivot(
      index='day',
      columns='is_click',
      values='user_id')\
    .reset_index()
b_clicks_pivot[' percent of users']=             b_clicks_pivot[True]/(b_clicks_pivot[True] + b_clicks_pivot[False])

print(a_clicks_pivot,b_clicks_pivot,ad_clicks )

import requests
from bs4 import BeautifulSoup
import sys
import os

# Fucntion of counting live YOUTUBE channel views
def youtube():

 usr_name=input('Enter Username of Youtube Channel : ')
 url='https://www.youtube.com/user/'+usr_name

 while True:
  r=requests.get(url)
  soup=BeautifulSoup(r.text,'lxml')
  span_tags=soup.find_all('span')
  string=str(span_tags)
  lis=string.split('><')
  fin_data=''
  lis2=[]
  for i in lis:
   if 't-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip' in i:
    fin_data+=str(i)
    lis2=fin_data.split(' ')
    break
  fin_data=''
  fin_data=str(lis2[1])
  print(f'Current Subscribers Count : {fin_data[12:]}')

# Fucntion for the counting number of posts on the entered hashtag
def insta_hashtag():
 hashtag = input('Enter Hashtag to search : ')
 temp_count = 0
 while True:
  r = requests.get('https://www.instagram.com/explore/tags/' + hashtag)
  soup = BeautifulSoup(r.text, 'lxml')
  main_tag = soup.find_all('script')[3]
  lis = str(main_tag).split(',')  # list type data count=''
  try:
   count = lis[12]
  except(ValueError, IndexError):
   print(f'Sorry Hashtag {hashtag} doesn\'t exist')
   continue
  count = count.replace('"edge_hashtag_to_media":{"count":', '')
  count = int(count)
  if (count - temp_count) > 0:
   print(f'#{hashtag} Posts : {count} (+{count - temp_count})')
  elif (count - temp_count) < 0:
   print(f'#{hashtag} Posts : {count} ({count - temp_count})')
  elif (count - temp_count) == 0:
   print(f'#{hashtag} Posts : {count}: (0)')
  temp_count = count

#Function for the checking some "hidden" details of the instagram profiles
def instagram_profile():
 username = input('Enter The Instagram Username : ')
 url = 'https://www.instagram.com/' + username
 html = requests.get(url)
 soup = BeautifulSoup(html.text, "lxml")
 temp = ''
 lis = []
 main_tag = soup.find_all('script')[4]  # all importatnt tags are saved in this main_tag variable
 data = str(main_tag)
 '''file1=open('script.txt','r+')
 file1.write(main_tag.text)#writing only main tag in the other file which will be used later to rip information
 file1.seek(0)'''
 data = str(main_tag)
 for ch in ['\n', '{', '}', '"']:
  data = data.replace(ch, '')
 data = data.replace('true', 'Yes').replace('false', 'No').replace('external_url', 'Extra URLs in Bio').replace(
  'graphql:user:biography', 'Bio').replace('is_business_account', 'Business Account').replace('edge_followed_by:count',
                                                                                              'Followers').replace(
  'edge_follow:count', 'Following:').replace('full_name', 'Full Name').replace('has_channel', 'Channel').replace('id',
                                                                                                                 'Instagram Token ID').replace(
  'is_business_account', 'Business Account').replace('is_joined_recently', 'Joined Recently').replace(
  'business_category_name', 'Business Category').replace('is_private', 'Private Account').replace('is_verified',
                                                                                                  'Verified')
 lis = data.split(',')
 lis = lis[8:32]  # adding starting 30 elements i.e. most of required info
 lis.insert(0, 'Username:' + username)
 for i in lis:
  print(i)

#########This section is the driver code#########
print('############ Social Media Inspector###############')
print('1. Youtube Channel Subscriber Counter\n2. Instagram Hashtag Posts Counter\n3. Instagram Profile Check\nEnter Your Choice : ',end='')
choice=int(input())
if choice == 1:
 youtube()
elif choice==2:
 insta_hashtag()
elif choice==3:
 instagram_profile()

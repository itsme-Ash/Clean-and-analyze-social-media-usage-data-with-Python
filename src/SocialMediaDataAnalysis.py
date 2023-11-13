#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media
# Introduction

Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
The objective of this project is to analyze social media data and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# # Importing required libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


# # Generating random data for the social media data

# In[2]:


n = 500  
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']
data = {
    'User Id': range(1, n + 1),
    'Category': [random.choice(categories) for _ in range(n)],
    'Post Type': [random.choice(['Text', 'Image', 'Video']) for _ in range(n)],
    'Date': pd.date_range('2021-01-01', periods=n),
    'Age': np.random.randint(13, 72, size=n),
    'Gender': np.random.randint(0, 2, size=n),  # 0 for male, 1 for female 
    'Likes': np.random.randint(0, 10000, size=n),
    'Comments': np.random.randint(0, 1000, size=n),
    'Shares': np.random.randint(0, 1000, size=n),
    'Views': np.random.randint(0, 100000, size=n),
    'Engagement': np.random.randint(1, 100, size=n),  # Simulated engagement metric
    'Followers Count': np.random.randint(100, 10000, size=n)  # Simulated followers count
}

These random variables were generated to mimic a social media dataset, facilitating analysis and exploration of user behaviors and engagement patterns across various content categories and post types.

# Variables Documentation:

My Random Variables:
1.	User ID: Unique identification number assigned to each user.
2.	Category: Represents the type of content posted, selected randomly from options like Food, Travel, Fashion, etc.
3.	Post Type: Indicates the format of the post (Text, Image, Video).
4.	Date: Timestamp indicating when the post was made, ranging from '2021-01-01' to a period of 'n'.
5.	Age: Randomly generated age of the users, ranging from 13 to 72 years old.
6.	Gender: Binary representation (0 for male, 1 for female) denoting the user's gender.
7.	Likes: Random count of likes received for the post, ranging from 0 to 10,000.
8.	Comments: Random count of comments received on the post, ranging from 0 to 1,000.
9.	Shares: Random count of shares received for the post, ranging from 0 to 1,000.
10.	Views: Random count of views on the post, ranging from 0 to 100,000.
11.	Engagement: Simulated metric representing the level of interaction with the post, ranging from 1 to 100.
12.	Followers Count: Simulated count of followers a user has, ranging from 100 to 10,000.
# In[32]:


SM.to_csv('social_media_data.csv', index=False)


# # Loading and Exploring Data

# In[3]:


SM = pd.DataFrame(data)
SM.head(3)


# In[4]:


SM.tail(3)


# In[5]:


SM.info()


# In[6]:


SM.describe()


# In[7]:


print(SM['Category'].value_counts())


# In[8]:


print(SM['Post Type'].value_counts())


# In[9]:


#I have no null values but the process of cleaning would be as the following:
SM.dropna(inplace=True)


# # Visualize and Analyze the data

# In[10]:


# Visualize 'Likes' with a histogram using Matplotlib
plt.hist(SM['Likes'], bins=12, edgecolor ="black")
plt.xlabel('Likes')
plt.ylabel('Frequency')
plt.title('Distribution of Likes')
plt.show()

This visualization helps in understanding the spread and concentration of the 'Likes' values within the specified bins.
# In[11]:


# Calculate and print the mean of 'Likes'
print(f"Mean Likes: {SM['Likes'].mean()}")


# In[12]:


# Visualize 'Likes' per catergories and post types

sns.catplot(data=SM, x="Likes", y="Category", hue="Post Type", kind="swarm")

The 'swarm' plot kind represents individual data points in a categorical arrangement, where each point's position on the category axis reflects the 'Likes' value, segregated by both 'Category' and 'Post Type'. This visualization aids in understanding how 'Likes' are distributed within various categories and post types, allowing for a comparative analysis of their distribution patterns.
# In[13]:


sns.catplot(data=SM, x="Category", y="Likes", hue="Post Type", kind="bar")


# In[ ]:


As the previous catplot visualisation, This visualization also enables a comparative analysis of 'Likes' across various categories and post types, providing insight into their relative magnitudes within each category.


# In[14]:


sns.catplot(data=SM, x="Gender", y="Likes", hue="Post Type", kind="bar")
plt.title("Likes by Gender and Post Type")


# In[15]:


# Group by 'Post Type' and calculate the mean of 'Likes'and 
mean_likes_type= SM.groupby('Post Type')['Likes'].mean()
print("Mean Likes per Post Type:")
print(mean_likes_type)


# In[16]:


# Create a boxplot for 'Category' vs 'Likes'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Likes', data=SM)
plt.show()


# In[17]:


# Group by 'Category' and calculate the mean of 'Likes'
mean_likes_category = SM.groupby('Category')['Likes'].mean()
print("Mean Likes per Category:")
print(mean_likes_category)


# In[30]:


mean_G_category = SM.groupby('Category')['Gender'].mean()
print("Gender per Category:")
print(mean_G_category)


# In[18]:


# Visualize 'Engagement' & Post Types
sns.catplot(data=SM, x="Post Type", y="Engagement", kind="swarm")


# In[19]:


#Analyzing the difference of likes for genders by categories
sns.catplot(data=SM, x="Category", y="Likes", hue="Gender", kind="box")


# In[20]:


# Create a boxplot for 'Post Type' vs 'Comments'
plt.figure(figsize=(8, 5))
sns.boxplot(x='Post Type', y='Comments', data=SM)
plt.title('Comments by Post Type')
plt.show()


# In[21]:


# Visualize 'Age' with a histogram using Matplotlib
plt.hist(SM['Age'], bins=20, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()


# In[22]:


# Create a boxplot for 'Gender' vs 'Likes'
plt.figure(figsize=(6, 4))
sns.boxplot(x='Gender', y='Likes', data=SM)
plt.title('Likes by Gender')
plt.show()


# In[23]:


# Group by 'Gendr' and calculate the mean of 'Likes'
mean_likes_category = SM.groupby('Gender')['Likes'].mean()
print("Mean Likes per Category:")
print(mean_likes_category)


# In[24]:


sns.catplot(data=SM, x="Category", y="Engagement", kind="bar")
print("Engagements per Category:")


# In[28]:


sns.catplot(data=SM, x="Category", y="Engagement", hue="Post Type", kind="bar")
print("Engagements per Post Types in each Category:")


# In[29]:


sns.catplot(data=SM, x="Category", y="Engagement", hue="Gender", kind="bar")


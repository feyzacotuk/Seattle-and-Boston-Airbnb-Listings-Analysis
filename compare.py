#!/usr/bin/env python
# coding: utf-8

# In[156]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[157]:


file_path = 'listings_seatle.csv'
df_seatle = pd.read_csv(file_path)


# In[158]:


df_seatle=df_seatle[["id","name","host_location","host_response_time","host_response_rate","host_acceptance_rate","host_is_superhost","host_has_profile_pic","host_identity_verified","price","review_scores_rating"]]


# In[159]:


df_seatle.isna().sum()


# In[160]:


#I have to drop the ones that are not true because even one missing answer would affect my comparison.#
df_seatle=df_seatle.dropna()


# In[161]:


df_seatle.info()


# In[162]:


# Yüzdelik sütunları dönüştürme
df_seatle['host_response_rate'] = df_seatle['host_response_rate'].str.rstrip('%').astype('float') / 100.0
df_seatle['host_acceptance_rate'] = df_seatle['host_acceptance_rate'].str.rstrip('%').astype('float') / 100.0

# "t" ve "f" stringlerini boolean değerlerine dönüştürme
df_seatle['host_is_superhost'] = df_seatle['host_is_superhost'].replace({'t': True, 'f': False}).astype('bool')
df_seatle['host_has_profile_pic'] = df_seatle['host_has_profile_pic'].replace({'t': True, 'f': False}).astype('bool')
df_seatle['host_identity_verified'] = df_seatle['host_identity_verified'].replace({'t': True, 'f': False}).astype('bool')


# In[163]:


# İlgili sütunları seçme
selected_columns = ['host_response_rate', 'host_acceptance_rate', 'host_is_superhost', 'host_has_profile_pic', 'host_identity_verified', 'review_scores_rating']

# Seçilen sütunlar ile yeni bir DataFrame oluşturma
df_selected = df_seatle[selected_columns]

# Korelasyon matrisini hesaplama
correlation_matrix = df_selected.corr()

# review_scores_rating ile korelasyonları görüntüleme
print(correlation_matrix['review_scores_rating'])


# In[164]:


# Isı haritası oluşturma
plt.figure(figsize=(6, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[165]:


#These correlation coefficients are useful for understanding the impact of certain host behaviors and attributes on review scores. The strongest relationship is observed between host_is_superhost and review_scores_rating, indicating that superhosts tend to receive higher review scores. Among the other variables, there are weak positive or negative relationships, or almost no relationship at all.#


# In[166]:


df_seatle['price'] = df_seatle['price'].str.replace('$', '').str.replace(',', '').astype('float')


# In[237]:


# İlgili sütunları seçme
selected_columns = ['host_response_rate', 'host_acceptance_rate', 'host_is_superhost', 'host_has_profile_pic', 'host_identity_verified', 'review_scores_rating',"price"]

# Seçilen sütunlar ile yeni bir DataFrame oluşturma
df_selected = df_seatle[selected_columns]


# Korelasyon matrisini hesaplama
correlation_matrix = df_selected.corr()
correlation_matrix


# In[205]:


file_path = 'listings.csv'
df_boston = pd.read_csv(file_path)


# In[206]:


df_boston=df_boston[["id","name","host_location","host_response_time","host_response_rate","host_acceptance_rate","host_is_superhost","host_has_profile_pic","host_identity_verified","price","review_scores_rating"]]


# In[207]:


df_boston.isna().sum()


# In[208]:


#I have to drop the ones that are not true because even one missing answer would affect my comparison.#
df_boston=df_boston.dropna()


# In[209]:


df_boston.info()


# In[210]:


# Yüzdelik sütunları dönüştürme
df_boston['host_response_rate'] = df_boston['host_response_rate'].str.rstrip('%').astype('float') / 100.0
df_boston['host_acceptance_rate'] = df_boston['host_acceptance_rate'].str.rstrip('%').astype('float') / 100.0

# "t" ve "f" stringlerini boolean değerlerine dönüştürme
df_boston['host_is_superhost'] = df_boston['host_is_superhost'].replace({'t': True, 'f': False}).astype('bool')
df_boston['host_has_profile_pic'] = df_boston['host_has_profile_pic'].replace({'t': True, 'f': False}).astype('bool')
df_boston['host_identity_verified'] = df_boston['host_identity_verified'].replace({'t': True, 'f': False}).astype('bool')


# In[211]:


# İlgili sütunları seçme
selected_columns = ['host_response_rate', 'host_acceptance_rate', 'host_is_superhost', 'host_has_profile_pic', 'host_identity_verified', 'review_scores_rating']

# Seçilen sütunlar ile yeni bir DataFrame oluşturma
df_selected = df_boston[selected_columns]

# Korelasyon matrisini hesaplama
correlation_matrix = df_selected.corr()

# review_scores_rating ile korelasyonları görüntüleme
print(correlation_matrix['review_scores_rating'])


# In[212]:


# Isı haritası oluşturma
plt.figure(figsize=(6, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[225]:


# Tüm hücreleri stringe dönüştürme
df_boston['price'] = df_boston['price'].astype(str)

# Dolar işaretini ve virgülleri kaldırma ve float'a dönüştürme
df_boston['price'] = df_boston['price'].str.replace('$', '').str.replace(',', '').astype('float')


# In[235]:


# İlgili sütunları seçme
selected_columns = ['host_response_rate', 'host_acceptance_rate', 'host_is_superhost', 'host_has_profile_pic', 'host_identity_verified', 'review_scores_rating']

# Seçilen sütunlar ile yeni bir DataFrame oluşturma
df_selected = df_boston[selected_columns]


# Korelasyon matrisini hesaplama
correlation_matrix = df_selected.corr()
correlation_matrix


# In[ ]:






# imports
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from array import *


rating = pd.read_csv('rating.csv')

anime0 = pd.read_csv('anime.csv')
anime_npk = anime0.set_index('anime_id')

#2
anime = anime0.drop(columns=['name', 'members', 'rating'])
# spand genre in columns, one for each genre
def func(x):
    if x['genre'] is np.nan:
        return x
    else:
        genres = list(map(lambda y: y.strip(), x['genre'].split(',')))
        for g in genres:
            x[g] = 1
        return x
anime2 = anime.apply(func, axis=1)

#3
# expand type in columns, one for each type
one_hot = pd.get_dummies(anime2['type'])
one_hot[one_hot == 0] = np.nan
anime3 = (anime2
          .drop(columns=['type', 'episodes', 'genre'])
          .join(one_hot, rsuffix='-type'))

rating_anime = rating.join(anime3.set_index('anime_id'), on='anime_id')

rating_anime.loc[rating_anime['rating'] == -1, 'rating'] = 5

# anime3 is a dataframe that was joined before.
attr = anime3.columns.tolist()
anime_class = anime3

attr.remove('anime_id')

rating_anime[attr] = rating_anime[attr].mul(rating_anime['rating'], axis=0)

users = (rating_anime
         .drop(columns=['anime_id', 'rating'])
         .groupby(by='user_id')
         .mean())

users = users.fillna(value=0)

#3.5

pca = PCA()
pca.fit(users)
acc_var = np.cumsum(pca.explained_variance_ratio_)

#4
number_of_components = 30
pca.set_params(n_components=number_of_components)
pca.fit(users)
users_pca = pca.transform(users)
users_pos_pca = pd.DataFrame(users_pca)
users_pos_pca['user_id'] = users.index
users_pos_pca = users_pos_pca.set_index('user_id')

#5
users_with_label = pd.DataFrame(PCA(n_components=3).fit_transform(users))
users_with_label['user_id'] = users.index
users_with_label = users_with_label.set_index('user_id')

kmeans = KMeans(n_clusters=8, n_init=30)
users_with_label['label'] = kmeans.fit_predict(users_pos_pca)

#6
rating_user = rating.join(users_with_label[['label']], on='user_id')
rating_user.loc[rating_user['rating'] == -1, 'rating'] = np.nan
CD = kmeans.cluster_centers_
## CD[i][j] -> cluster i, j-th dimension(измерение)
#7
groups = (rating_user[['anime_id', 'rating', 'label']]
          .groupby(by=['label', 'anime_id'])
          .rating.agg(['mean', 'count']))

groups['obj'] = groups['mean']*groups['count']
groups_obj = groups[['obj']].dropna()

cats = groups_obj.index.get_level_values(0).unique().tolist()
rec = []
for cat in cats:
    rec.append(
        groups_obj
        .loc[cat]
        .sort_values(by='obj', ascending=False)
        .reset_index()
        .join(
            anime0[['name', 'anime_id']].set_index('anime_id'),
            on='anime_id')
        ['name']
        .rename(cat)
    )
rec = pd.concat(rec, axis=1)



#it returns i - Anime name
index_by_name = anime0.set_index(['name'])


def get_the_best(index):
    x_pd_pca = users_pos_pca.loc[index]
    mn = 1e18
    last = -1
    for tim in range(1, 8, 1):
        nw = 0
        for i in range(1, 30, 1):
            nw += (CD[tim][i] - x_pd_pca[i]) * (CD[tim][i] - x_pd_pca[i])
        if nw < mn:
            mn = nw
            last = tim
    label = last

    for i in rec[label]:
        ANIME_ID = index_by_name.loc[i]['anime_id']

        if rating.loc[rating['anime_id']==ANIME_ID].loc[
            rating['user_id']==index].empty:
            return i

print(rec.head(10))
print(CD)
# For recommendations use
# 1) PCA for decrease num of dimensions
# 2) CD for find label (cluster where this person is)
# 3) rec for anime, which person hasn't seen and recommend the best one

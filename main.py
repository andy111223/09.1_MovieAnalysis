import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

pd.set_option('display.float_format','{:.2f}'.format)

genres = pd.read_csv('tmdb_genres.csv')
genres.info()
genres.columns
genres.dtypes
print(genres.head())

movies = pd.read_csv('tmdb_movies.csv')
movies.info()
movies.columns
movies.dtypes
print(movies.head())

# 1
third_quartile = movies['vote_count'].quantile(0.75)
top_movies = movies[movies['vote_count'] > third_quartile].sort_values(by='vote_average',ascending=False).head(10)
print(top_movies)

# 2
movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')
movies = movies.dropna(subset=['release_date'])
movies['year'] = movies['release_date'].dt.year.astype(int)

filtered_movies = movies[(movies['year'] >= 2010) & (movies['year'] <= 2016)]
avg_stats_movies = filtered_movies.groupby('year').agg(
    avg_revenue = ('revenue','mean'),
    avg_budget = ('budget','mean')
).reset_index()

print(avg_stats_movies)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(avg_stats_movies['year'], avg_stats_movies['avg_revenue'], color='lightblue', label='Average Revenue')
ax.plot(avg_stats_movies['year'], avg_stats_movies['avg_budget'], color='orange', label='Average Budget')

ax.set_xlabel('Year')
ax.set_ylabel('Amount in mln USD')
ax.set_title('Average revenue and budget of movies released in years 2010-2016')

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.1f}'))

ax.set_xticks(avg_stats_movies['year'])
ax.set_xticklabels(avg_stats_movies['year'], rotation=45)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()

plt.show()

# 3
genres.rename(columns={'Unnamed: 0' : 'genre_id'}, inplace=True)
genres.dropna(subset=['genre_id'], inplace=True)
genres['genre_id'] = genres['genre_id'].astype(int)

merged_movies = movies.merge(genres, left_on='genre_id', right_on='genre_id', how='left')
print(merged_movies)

# 4
top_genre = merged_movies.value_counts('genres')
print(top_genre)
print(f"The most common genre is '{top_genre.index[0]}' with {top_genre.iloc[0]} movies.")

# 5
runtimes = merged_movies.groupby('genres').agg(
    avg_runtime = ('runtime','mean')
)

top_runtimes = runtimes.sort_values(by='avg_runtime',ascending=False).head(3)
print('Genres with the longest average runtime:\n', top_runtimes)

# 6
history_movies = merged_movies[merged_movies['genres'] == 'History']
print(history_movies)

plt.figure(figsize=(10, 6))
plt.hist(history_movies['runtime'].dropna(), bins=10, color='pink', edgecolor='black', alpha=0.7)
plt.xlabel('Runtime (minutes)')
plt.ylabel('Number of Movies')
plt.title('Histogram of Runtime for History Genre')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
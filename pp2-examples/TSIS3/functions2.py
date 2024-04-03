# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Task 1
def score_above_5_5(movie):
    return movie['imdb'] > 5.5

# Call the function
print(score_above_5_5(movies[0]))

#Task 2
def movies_above_5_5(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

# Call the function
print(movies_above_5_5(movies))

#Task 3
def movies_in_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

# Call the function
print(movies_in_category(movies, 'Romance'))

#Task 4
def average_score(movies):
    return sum(movie['imdb'] for movie in movies) / len(movies)

# Call the function
print(average_score(movies))

#Task 5
def category_average_score(movies, category):
    return sum(movie['imdb'] for movie in movies_in_category(movies, category)) / len(movies_in_category(movies, category))

# Call the function
print(category_average_score(movies, 'Romance'))
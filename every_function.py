# 3-10. Every Function: Think of something you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, 
# cities, languages, or anything else you’d like. Write a program that 
# creates a list containing these items and then uses each function 
# introduced in this chapter at least once.
movies = ['the avengers', 'logan', 'guardians of the galaxy', 
          'iron man', 'avengers endgame']

print(movies[0])

print(movies[0].title())

print(movies)
movies[1] = 'x-men first class'
print(movies)

movies.append('x-men days of future past')
print(movies)

movies.insert(0, 'deadpool')
print(movies)

del movies[6]
print(movies)

popped_movie = movies.pop(0)
print(movies)
print(popped_movie)
print(popped_movie.title() + " is not an MCU movie")

movies.remove('x-men first class')
print(movies)

print(sorted(movies))

print(sorted(movies, reverse=True))

movies.reverse()
print(movies)

movies.sort()
print(movies)

movies.sort(reverse=True)
print(movies)

print(len(movies))
#Get input of list of movies that was released in 2025.Also get input of movies watched by the user (any year)Display the following:1.	Movies of 2025 that are watched by the user 2.	Movies of 2025 that are yet to be watched by the user 3.Total list of movies watched by the user combined with movies of 2025

movie_list_2025=['tere ish main','Dhurindar','Avatar','Puspa','Jaari2']
movie_set_2025=set(movie_list_2025)

watched_movie=input("Enter the watched movies:").title()
movie_user = watched_movie.split(',')
movie_user_set=set(movie_user)

# 1.	Movies of 2025 that are watched by the user

movieset_1=movie_set_2025.intersection(movie_user_set)
print(movieset_1)

# 2.	Movies of 2025 that are yet to be watched by the user

movieset_2=movie_set_2025.difference(movie_user_set)
print(movieset_2)

# 3.	Total list of movies watched by the user combined with movies of 2025

movieset_3=movie_set_2025.union(movie_user_set)
print(movieset_3)

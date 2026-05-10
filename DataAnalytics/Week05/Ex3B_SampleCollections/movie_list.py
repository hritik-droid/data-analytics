movies = ["Inception", "Avengers", "Interstellar", "Joker"]

print("The list movies includes my top " + str(len(movies)) + " favorite movies")
print(movies)

# sorted() does NOT change original list
print(sorted(movies))
print(movies)

# sort() DOES change original list
movies.sort()
print(movies)

# Add another movie
movies.append("Batman")
print(movies)
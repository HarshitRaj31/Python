movies=[]
n=int(input("Enter Number Of Movies: "))

for i in range(n):
    name=input("Enter Movie Name: ")
    rating=input("Enter rating: ")
    genre=input("Enter genre: ")

    movies.append((name,rating,genre))

    print("Movies",movies)

for  name,rating,genre in movies:
    if rating > 8.0:
        print(name)

highest=max(movies, key=lambda x:x[0])
print("Highest Movies",highest)

average=sum(rating for name, genre,rating in movies)/n
print("Average Rating",average)

g = input("\nEnter genre: ")

print("Movies of", g, ":")
for name, rating, genre in movies:
    if genre.lower() == g.lower():
        print(name)
        movies.sort(key=lambda x: x[1], reverse=True)

print("\nMovies sorted by rating:")
for name, rating, genre in movies:
    print(name, rating)
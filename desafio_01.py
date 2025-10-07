favorite_movie = ["bastardos inglórios", "Corra!"]

dates = ["06/10/2025", "07/10/2025"]

movie = [{"filme": favorite_movie[n],"data":dates[n]} for n in range(len(favorite_movie))]

for i in range(len(movie)):
    print(f"\nfilme: {movie[i]['filme']}\ndata:{movie[i]['data']}")
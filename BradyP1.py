AllMovies = []
Movie = []
MovieName = input('Input Movie Name ')
MovieLength = input('Input Movie Length ')
MovieYear = int(input('Input Movie Year '))
MovieDirector = input('Input Movie Director ')
MovieCompany = input('Input Movie Company ')
MovieDescription = input('InputMovie Description')
MovieProduction = MovieYear -2 
Movie.append(MovieName)
Movie.append(MovieLength)
Movie.append(MovieYear)
Movie.append(MovieDirector)
Movie.append(MovieCompany)
Movie.append(MovieDescription)
Movie.append(MovieProduction)
AllMovies.append(Movie)
print(AllMovies)

command = input('enter command ')
if command == 'Movie':
    print(f'{MovieName}')
elif command == 'Length':
    print(f'{MovieLength}')
elif command == 'Year':
    print(f'{MovieYear}')
elif command == 'Director': 
    print(f'{MovieDirector}')
elif command == 'Company':
    print(f'{MovieCompany}')
elif command == 'Description':
    print(f'{MovieDescription}')
elif command == "Production":
    print(f'{MovieProduction}')
else:
    print('Invalid Command')

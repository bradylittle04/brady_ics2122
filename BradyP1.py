AllSongs = []
Song = []
SongName = input('Input Song Name ')
SongLength = input('Input Song Length ')
SongYear = int(input('Input Song Year '))
SongWriter = input('Input Song Writer ')
SongProducer = input('Input Song Producer ')
SongMeaning = input('Input Song Meaning ')
SongProduction = SongYear -2 
Song.append(SongName)
Song.append(SongLength)
Song.append(SongYear)
Song.append(SongWriter)
Song.append(SongProducer)
Song.append(SongMeaning)
Song.append(SongProduction)
AllSongs.append(Song)
print(AllSongs)

command = input('enter command ')
if command == 'Song':
    print(f'{SongName}')
elif command == 'Length':
    print(f'{SongLength}')
elif command == 'Year':
    print(f'{SongYear}')
elif command == 'Writer': 
    print(f'{SongWriter}')
elif command == 'Producer':
    print(f'{SongProducer}')
elif command == 'Meaning':
    print(f'{SongMeaning}')
elif command == "Production":
    print(f'{SongProduction}')
else:
    print('Invalid Command')

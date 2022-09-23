def main():
    title =  "Howl's Moving Castle"
    genre = 'Japanese animation'
    author = 'Miyazaki Hayao'
    year = 2004
    imdb = 8.2
    mainC = 'Sophie'
    mins = 119
    originalLang = 'Japanese'
    job = 'hatmaker'
    
    
    text =" {title} is a {genre} film, written by {author},. The film was produced in {year}. It's IMDB rating is {imdb}. The main character's name is {name}, who is a {job}. The film is {mins} mins long. The original language is {lang}."
    print(text.format(title = title, genre = genre, author = author, year = year, imdb = imdb, name = mainC, mins = mins, lang = originalLang, job = job))
    
    
    
    
if __name__ == "__main__":
    main()
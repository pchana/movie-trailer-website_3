import media
import fresh_tomatoes

" " " Create data for my favorite eight movies:  " " "

shawshank=media.Movie("Shawshank Redemption", "A friendship is formed through prison", "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco")

starwarsfive=media.Movie("Star Wars: Episode V", "Luke continues to battle against Darth Vader", "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg", "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

imitationgame=media.Movie("The Imitation Game", "Studying the life of Alan Turing as he cracks war code", "http://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg", "https://www.youtube.com/watch?v=S5CjKEFb-sM")

goodwill=media.Movie("Good Will Hunting", "An unlikely friendship forms between two", "http://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg", "https://www.youtube.com/watch?v=z02M3NRtkAA")

bridesmaids=media.Movie("Bridesmaids", "Comedy on the trials of being a bridesmaids", "http://upload.wikimedia.org/wikipedia/en/d/df/BridesmaidsPoster.jpg", "https://www.youtube.com/watch?v=FNppLrmdyug")

legallyblonde=media.Movie("Legally Blonde", "An unexpected lawyer shines", "http://upload.wikimedia.org/wikipedia/en/a/ac/Legally_blonde.jpg", "https://www.youtube.com/watch?v=E8I-Qzmbqnc")

raiders=media.Movie("Raiders of the Lost Ark", "Indiana Jones is pitted against a group of Nazis", "http://upload.wikimedia.org/wikipedia/en/4/4b/Raiders.jpg", "https://www.youtube.com/watch?v=0ZOcoxjeUYo")

backtothefuture=media.Movie("Back to the Future", "A teenager is sent back to time", "http://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Back_to_the_Future.jpg/220px-Back_to_the_Future.jpg", "https://www.youtube.com/watch?v=qvsgGtivCgs")

movies=[shawshank, starwarsfive, imitationgame, goodwill, bridesmaids, legallyblonde, raiders, backtothefuture]

fresh_tomatoes.open_movies_page(movies)

                       
                       

# Enhanced Spotify Music App with detailed output and song selection feature

class SpotifyMusicApp:
    def __init__(self):
        # Updated data structure holding detailed song metadata
        self.music_library = {
            "movies": {
                "Bahubali": [
                    {"song": "Bahubali Bhali Ra Bali", "songwriter": "M.M. Keeravani", "year": "2015"}
                ],
                "Inception": [
                    {"song": "Time", "songwriter": "Hans Zimmer", "year": "2010"}
                ]
            },
            "categories": {
                "private": [
                    {"song": "DJ Snake - Turn Down for What", "songwriter": "DJ Snake", "year": "2013"},
                    {"song": "DJ Alok - Hear Me Now", "songwriter": "Alok Achkar", "year": "2016"}
                ],
                "dj": [
                    {"song": "Marshmello - Alone", "songwriter": "Marshmello", "year": "2016"},
                    {"song": "Avicii - Wake Me Up", "songwriter": "Avicii", "year": "2013"}
                ],
                "devotional": [
                    {"song": "Gayatri Mantra", "songwriter": "Anuradha Paudwal", "year": "1980"},
                    {"song": "Hanuman Chalisa", "songwriter": "Gulshan Kumar", "year": "1992"}
                ]
            },
            "languages": {
                "Hindi": [
                    {"song": "Channa Mereya", "songwriter": "Arijit Singh", "year": "2016"}
                ],
                "Tamil": [
                    {"song": "Vaathi Coming", "songwriter": "Anirudh Ravichander", "year": "2020"}
                ],
                "English": [
                    {"song": "Shape of You", "songwriter": "Ed Sheeran", "year": "2017"}
                ]
            }
        }

    def search_by_movie(self, movie_name):
        # Search for songs related to a specific movie with detailed info
        songs = self.music_library["movies"].get(movie_name, [])
        if not songs:
            return "No songs found for this movie."
        
        for song in songs:
            print(f"Movie: {movie_name}")
            print(f"Song: {song['song']}")
            print(f"Songwriter: {song['songwriter']}")
            print(f"Published Year: {song['year']}\n")

    def search_by_category(self, category):
        # Search for songs by category (private, DJ, devotional) with song selection
        songs = self.music_library["categories"].get(category.lower(), [])
        if not songs:
            return "No songs found for this category."

        print(f"Songs in {category.capitalize()} category:")
        for i, song in enumerate(songs, start=1):
            print(f"{i}. {song['song']} by {song['songwriter']} ({song['year']})")
        
        # Ask user to select a song to play
        choice = int(input("Enter the song number you want to play (or 0 to cancel): "))
        if 1 <= choice <= len(songs):
            selected_song = songs[choice - 1]
            print(f"\nPlaying '{selected_song['song']}' by {selected_song['songwriter']} ({selected_song['year']})...")
        elif choice == 0:
            print("No song selected.")
        else:
            print("Invalid choice.")

    def search_by_language(self, language):
        # Search for songs by language with detailed info
        songs = self.music_library["languages"].get(language.capitalize(), [])
        if not songs:
            return "No songs found for this language."
        
        for song in songs:
            print(f"Language: {language.capitalize()}")
            print(f"Song: {song['song']}")
            print(f"Songwriter: {song['songwriter']}")
            print(f"Published Year: {song['year']}\n")

    def start_app(self):
        print("Welcome to the Spotify Music App!")
        while True:
            print("\nChoose an option to find songs:")
            print("1. Search by Movie Name")
            print("2. Search by Category (Private, DJ, Devotional)")
            print("3. Search by Language (Hindi, Tamil, English)")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                movie_name = input("Enter the movie name: ")
                print("Songs for movie:", movie_name)
                self.search_by_movie(movie_name)
            
            elif choice == "2":
                category = input("Enter the category (private/dj/devotional): ")
                self.search_by_category(category)
                
            elif choice == "3":
                language = input("Enter the language (Hindi/Tamil/English): ")
                self.search_by_language(language)
                
            elif choice == "4":
                print("Exiting Spotify Music App. Thank you!")
                break
            else:
                print("Invalid choice, please select again.")

# Run the SpotifyMusicApp
if __name__ == "__main__":
    app = SpotifyMusicApp()
    app.start_app()

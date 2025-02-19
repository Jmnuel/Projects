class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class User:
    def __init__(self, name):
        self.name = name
        self.preferences = []

    def add_preference(self, genre):
        self.preferences.append(genre)

class RecommendationSystem:
    def __init__(self, books):
        self.books = books

    def recommend_books(self, user):
        recommended_books = []
        for book in self.books:
            if book.genre.lower() in user.preferences:
                recommended_books.append(book)
        return recommended_books

def get_user_input(available_genres):
    name = input("Enter your name: ")
    print("Available book genres:", ', '.join(available_genres))
    
    valid_preferences = []
    invalid_preferences = []
    while True:
        preferences = input("Enter your book preferences (separated by commas): ").lower().split(',')
        valid_preferences = [preference.strip() for preference in preferences if preference.strip() in available_genres]
        invalid_preferences = [preference.strip() for preference in preferences if preference.strip() not in available_genres]
        
        if valid_preferences:
            break
        elif invalid_preferences:
            print("Invalid preferences: ", ', '.join(invalid_preferences))
    
    return name.strip(), valid_preferences, invalid_preferences
  
popular_books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
    Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
    Book("1984", "George Orwell", "Dystopian"),
    Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
    Book("Pride and Prejudice", "Jane Austen", "Romance"),
    Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"),
    Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
    Book("The Hunger Games", "Suzanne Collins", "Dystopian"),
    Book("The Da Vinci Code", "Dan Brown", "Mystery"),
    Book("The Alchemist", "Paulo Coelho", "Adventure")
]

available_genres = set(book.genre.lower() for book in popular_books)

if __name__ == "__main__":

    user_name, valid_preferences, invalid_preferences = get_user_input(available_genres)

    user = User(user_name)
    for preference in valid_preferences:
        user.add_preference(preference.strip())

    recommendation_system = RecommendationSystem(popular_books)

    recommendations = recommendation_system.recommend_books(user)

    if recommendations:
        print("\nRecommendations for", user.name + ":")
        for book in recommendations:
            print(book.title)
    else:
        print("No recommendations found for the provided preferences.")
    
    if invalid_preferences:
        print("\nNo recommendations found for the following preferences:")
        for preference in invalid_preferences:
            print(preference)

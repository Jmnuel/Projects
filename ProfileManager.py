class User:
    def __init__(self, first_name: str, last_name: str, like_count: int, friendlist: list):
        self.first_name = first_name
        self.last_name = last_name
        self.like_count = max(0, like_count)  
        self.friendlist = friendlist if friendlist else [] 

    def add_friend(self, friend_name: str):
        if friend_name not in self.friendlist and friend_name.strip():
            self.friendlist.append(friend_name.strip())
            print(f"Added {friend_name} to friends.")
        else:
            print("Friend already exists or name is invalid.")

    def remove_friend(self, friend_name: str):
        if friend_name in self.friendlist:
            self.friendlist.remove(friend_name)
            print(f"Removed {friend_name} from friends.")
        else:
            print(f"Friend {friend_name} not found.")

    def update_likes(self, new_likes: int):
        try:
            new_likes = max(0, int(new_likes)) 
            self.like_count = new_likes
            print(f"Updated likes to {new_likes}.")
        except ValueError:
            print("Invalid input! Likes must be a number.")

    def introduce(self):
        full_name = f"{self.first_name} {self.last_name}"
        friends_str = "\n        ".join(self.friendlist) if self.friendlist else "No friends yet"
        print(f"Hi, I am {full_name}.")
        print(f"""
Full Profile:
    Full name: {full_name}
    Likes    : {self.like_count}
    Friends  :
        {friends_str}
""")

def main():
    users = [] 
    initial_friends = ["Elon Musk", "Bill Gates", "Mark Zuck", "Jeff Bezos"]

    while True:
        print("\nProfile Manager System")
        print("1. Create a new user")
        print("2. View a user's profile")
        print("3. Update a user's likes")
        print("4. Add a friend to a user")
        print("5. Remove a friend from a user")
        print("6. List all users")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            try:
                first_name = input("First name: ").strip()
                last_name = input("Last name: ").strip()
                if not first_name or not last_name:
                    print("Names cannot be empty!")
                    continue
                like_count = int(input("Initial like count (non-negative): ") or 0)  
                new_user = User(first_name, last_name, like_count, initial_friends.copy()) 
                users.append(new_user)
                print(f"User {first_name} {last_name} created successfully!")
            except ValueError:
                print("Invalid input! Like count must be a number.")

        elif choice == '2':
            if not users:
                print("No users exist yet. Create a user first!")
                continue
            print("\nAvailable users:")
            for i, user in enumerate(users, 1):
                print(f"{i}. {user.first_name} {user.last_name}")
            try:
                user_idx = int(input("Select user by number: ")) - 1
                if 0 <= user_idx < len(users):
                    users[user_idx].introduce()
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            if not users:
                print("No users exist yet. Create a user first!")
                continue
            print("\nAvailable users:")
            for i, user in enumerate(users, 1):
                print(f"{i}. {user.first_name} {user.last_name}")
            try:
                user_idx = int(input("Select user by number to update likes: ")) - 1
                if 0 <= user_idx < len(users):
                    new_likes = input("Enter new like count: ")
                    users[user_idx].update_likes(new_likes)
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            if not users:
                print("No users exist yet. Create a user first!")
                continue
            print("\nAvailable users:")
            for i, user in enumerate(users, 1):
                print(f"{i}. {user.first_name} {user.last_name}")
            try:
                user_idx = int(input("Select user by number to add friend: ")) - 1
                if 0 <= user_idx < len(users):
                    friend_name = input("Enter friend's name: ").strip()
                    users[user_idx].add_friend(friend_name)
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            if not users:
                print("No users exist yet. Create a user first!")
                continue
            print("\nAvailable users:")
            for i, user in enumerate(users, 1):
                print(f"{i}. {user.first_name} {user.last_name}")
            try:
                user_idx = int(input("Select user by number to remove friend: ")) - 1
                if 0 <= user_idx < len(users):
                    friend_name = input("Enter friend's name to remove: ").strip()
                    users[user_idx].remove_friend(friend_name)
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '6':
            if not users:
                print("No users exist yet.")
            else:
                print("\nAll Users:")
                for i, user in enumerate(users, 1):
                    print(f"{i}. {user.first_name} {user.last_name} - Likes: {user.like_count}")

        elif choice == '7':
            print("Exiting Profile Manager System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
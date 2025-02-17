import instaloader
import os

instagram_username = "xxxxxxxxx"

def main(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\x1b[32m
     _____           _         _____                                      
    |_   _|         | |       / ____|                                     
      | |  _ __  ___| |_ __ _| (___   ___ _ __ __ _ _ __  _ __   ___ _ __ 
      | | | '_ \/ __| __/ _` |\___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|
     _| |_| | | \__ \ || (_| |____) | (__| | | (_| | |_) | |_) |  __/ |   
    |_____|_| |_|___/\__\__,_|_____/ \___|_|  \__,_| .__/| .__/ \___|_|   1.0
                                                   | |   | |              
                                                   |_|   |_|      \x1b[0m        
    """)

    username = input('\x1b[33mEnter the username: \x1b[0m')

    base_dir = f"{username}"
    os.makedirs(f"{base_dir}", exist_ok=True)

    # Login no Instagram
    L = instaloader.Instaloader()
    print("\x1b[32m", end="")
    try:
        L.load_session_from_file(instagram_username, f"session-{instagram_username}")
    except FileNotFoundError:
        print("\x1b[31m[X] Error: Session not found.\x1b[0m")
        return

    print("\x1b[35m[*] Searching profile...")
    profile = instaloader.Profile.from_username(L.context, username)

    print("\x1b[34m[*] Fetching followers...\x1b[0m")
    with open(f"{base_dir}/followers.txt", "w") as file:
        for follower in profile.get_followers():
            file.write(follower.username + "\n")

    print("\x1b[34m[*] Fetching followings...\x1b[0m")
    with open(f"{base_dir}/following.txt", "w") as file:
        for following in profile.get_followees():
            file.write(following.username + "\n")

    # Download posts
    print("\x1b[34m[*] Downloading posts...\x1b[0m")
    for post in profile.get_posts():
        L.download_post(post, target=f"{base_dir}")

    print("\x1b[32m[✔] Download successfull!\x1b[0m")

if __name__ == '__main__':
    main()

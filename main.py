"""
Basic Video Toolkit - Man Menu
"""
def main():
    print(('=' * 5) + " Basic Video Toolkit " + ('=' * 5))
    print("\t 1. Brows for videos")
    print("\t 2. Play selected video")
    print("\t 3. Webcam review")
    print("\t 4. Recorde video (press 's' to start/stop)")
    print("\t 5. Toggle motion detection")
    print("\t 6. Press 'q' to exit")
    choice = input("\nSelect an option (1-6): ")
    print(f"You selected {choice}") # TODO replace this with logic

if __name__ == '__main__':
    main()
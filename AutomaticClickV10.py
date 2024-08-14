import pyautogui
import time

# Function to get the initial click position
def get_click_position():
    print("Move your mouse to the position you want to click. Capturing position in 5 seconds.")
    time.sleep(5)  # Wait 5 seconds for the user to position the mouse
    position = pyautogui.position()  # Get the mouse position
    print(f"Click position set to: {position}")
    return position

# Main program
def main():
    click_position = get_click_position()

    print("Auto-clicking started. Click anywhere else to stop.")

    # Continuously click the specified position until a different position is clicked
    while True:
        pyautogui.click(click_position)
        time.sleep(0.3)  # Wait 0.3 seconds between clicks

        # Check if the current mouse position is different from the initial click position
        if pyautogui.position() != click_position:
            print("Detected a click on a different position. Exiting.")
            break

if __name__ == "__main__":
    main()
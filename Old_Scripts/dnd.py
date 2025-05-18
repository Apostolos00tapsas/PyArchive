import subprocess
import time

def adb_command(command):
    """Execute an ADB command."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr

def input_text(text):
    """Input text into the currently focused text field."""
    # Replace spaces with '+' for ADB input
    formatted_text = text.replace(" ", "+")
    adb_command(f"adb shell input text '{formatted_text}'")

def main():
    # Unlock the phone with the PIN
    adb_command("adb shell input keyevent 26")
    adb_command("adb shell input text 1993")
    # Launch the Messenger app (adjust the package and activity names as needed)
    adb_command("adb shell am start -n com.facebook.orca/com.facebook.orca.auth.StartScreenActivity")
    
    # Wait for a moment to let the app load
    time.sleep(2)
    adb_command("adb shell input tap 600 800")

    time.sleep(1)
    adb_command("adb shell input tap 600 2200")
    # Example text message to input
    message = "Vzaras"
    
    # Input the message
    input_text(message)

    # Optionally, simulate pressing Enter to send the message
    adb_command("adb shell input tap 1044 1343")

if __name__ == "__main__":
    main()

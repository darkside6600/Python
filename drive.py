import subprocess

def get_removable_drive_path():
    """
    Get the path of a removable drive in Linux.

    Returns:
        str: The mount path of the removable drive, or None if not found.
    """
    try:
        # Use the `lsblk` command to get information about block devices
        output = subprocess.check_output(["lsblk", "-o", "NAME,MOUNTPOINT,RM"], text=True)
        
        # Split output into lines and process each line
        for line in output.splitlines()[1:]:  # Skip the header line
            parts = line.split()
            if len(parts) < 3:
                continue
            name, mountpoint, removable = parts[0], parts[1] if len(parts) > 1 else None, parts[-1]
            
            # Check if the device is removable (RM=1) and has a mountpoint
            if removable == "1" and mountpoint:
                return mountpoint
        
        # If no removable drive is found
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    path = get_removable_drive_path()
    if path:
        print(f"Removable drive is mounted at: {path}")
    else:
        print("No removable drive found.")

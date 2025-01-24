import os
import subprocess

def banner():
    print("="*50)
    print("      Automated Nmap Scanner")
    print("="*50)

def get_target():
    target = input("Enter the target (IP or range): ")
    return target

def choose_scan_type():
    print("\nSelect the type of scan:")
    print("[1] Quick Scan")
    print("[2] Full Scan")
    print("[3] OS Detection")
    print("[4] Custom Scan")
    choice = input("Enter your choice (1-4): ")

    scan_types = {
        "1": "-T4 -F",  # Quick scan
        "2": "-p-",  # Full scan
        "3": "-A",  # OS detection
        "4": input("Enter custom Nmap options: ") 
    }
    return scan_types.get(choice, "-T4 -F")  # A defualt scan

def perform_scan(target, options):
    print("\nRunning Nmap scan...")
    output_file = f"nmap_scan_{target.replace('/', '_')}.txt"
    command = f"nmap {options} {target} -oN {output_file}"
    print(f"Executing: {command}\n")
    
    # Run the Nmap command
    subprocess.run(command, shell=True)

    print(f"Scan complete. Results saved to {output_file}")
    return output_file

def main():
    # Check if Nmap is installed
    if not shutil.which("nmap"):
        print("Nmap is not installed. Please install it and try again.")
        return
    
    banner()
    target = get_target()
    scan_type = choose_scan_type()
    perform_scan(target, scan_type)

if __name__ == "__main__":
    main()

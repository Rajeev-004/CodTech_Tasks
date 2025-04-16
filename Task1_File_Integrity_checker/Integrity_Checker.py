import hashlib
import os

def calculate_hash(file_path, algorithm='sha256'):
    
    #
    # 
    # Calculate the hash of a file using the specified algorithm.
    
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None

def generate_baseline(directory, output_file="baseline_hashes.txt"):
    
    #Generate a baseline hash file for all files in a directory.
    
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = calculate_hash(file_path)
                if file_hash:
                    outfile.write(f"{file_path},{file_hash}\n")
    print(f"\n✅ Baseline hashes saved to '{output_file}'")

def check_integrity(baseline_file):
    
    #Compare current file hashes to baseline to detect changes.
    
    
    print("\n🔍 Checking file integrity...\n")
    with open(baseline_file, 'r') as infile:
        for line in infile:
            file_path, original_hash = line.strip().split(',')
            current_hash = calculate_hash(file_path)
            if current_hash is None:
                print(f"❌ MISSING: {file_path}")
            elif current_hash != original_hash:
                print(f"⚠️  CHANGED: {file_path}")
                print(f"   OLD HASH: {original_hash}")
                print(f"   NEW HASH: {current_hash}\n")
            else:
                print(f"✅ UNCHANGED: {file_path}")

def main():
    print("\n=== FILE INTEGRITY CHECKER ===")
    print("1. Generate baseline")
    print("2. Check file integrity")
    choice = input("Select option (1/2): ")

    if choice == '1':
        folder = input("Enter full folder path to scan: ").strip('"')
        generate_baseline(folder)
    elif choice == '2':
        baseline = input("Enter path to baseline hash file: ").strip('"')
        check_integrity(baseline)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()

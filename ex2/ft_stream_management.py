import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    try:
        name = input("Input Stream active. Enter archivist ID: ")
        message = input("Input Stream active. Enter status report: ")
        sys.stdout.write(f"[STANDARD] Archive status from {name}: {message}\n")
        sys.stderr.write("[ALERT] System diagnostic: Communication"
                         " channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_crisis_response.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/17 07:53:27 by bfitte            #+#    #+#             #
#    Updated: 2026/01/17 07:53:28 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

class ArchiveError(Exception):
    def __init__(self, details: str = None):
        message = f"\nCRISIS ALERT: {details}"
        super().__init__(message)


class UnknowFileError(ArchiveError):
    pass


class ForbiddenFileError(ArchiveError):
    pass


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        try:
            with open("lost_archive.txt", "r") as f:
                print(f)
        except FileNotFoundError:
            print(UnknowFileError("Attempting access "
                                  "to 'lost_archive.txt'..."))
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        try:
            with open("corrupted_archive.txt", "r") as f:
                print(f)
        except PermissionError:
            print(ForbiddenFileError("Attempting access to"
                                     " 'corrupted_archive.txt'..."))
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        try:
            print("\nROUTINE ACCESS: Attempting access to "
                  "'standard_archive.txt'...")
            with open("standard_archive.txt", "r") as f:
                print(f"SUCCESS: Archive recovered - {f.read()}")
            print("STATUS: Normal operations resumed")
        except Exception as e:
            print(e)
            print("Attempting access to 'standard_archive.txt'...")
            print("RESPONSE: Houston! We've had a problem")
            print("STATUS: Crisis handled, security maintained")
        print("\nAll crisis scenarios handled successfully. Archives secure.")
    except Exception as e:
        print(e)
        print("An error occurs.")


if __name__ == "__main__":
    main()

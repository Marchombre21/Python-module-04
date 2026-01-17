# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_archive_creation.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/15 16:25:14 by bfitte            #+#    #+#             #
#    Updated: 2026/01/15 16:25:15 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

def main():
    datas = [
        "The lemur is the biggest drug addict in history.",
        "We are blind for 40 minutes a day.",
        "Archived by Data Archivist trainee."
    ]
    try:
        f = open("new_discovery.txt")
        f.close()
        print("You almost erase part of human history, you fool!!")
    except FileNotFoundError:
        try:
            print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
            print("Initializing new storage unit: new_discovery.txt")
            f = open("new_discovery.txt", "w")
            print("Storage unit created successfully...")
            print("\nInscribing preservation data...")
            for entry, data in enumerate(datas):
                print(f"[Entry 00{entry + 1}] {data}")
                f.write(f"[Entry 00{entry + 1}] {data}\n")
            f.close()
            print("\nData inscription complete. Storage unit sealed")
            print("Archive 'new_discovery.txt' ready for "
                  "long-term preservation.")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

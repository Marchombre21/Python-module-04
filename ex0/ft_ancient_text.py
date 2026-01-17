# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_ancient_text.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/15 15:44:40 by bfitte            #+#    #+#             #
#    Updated: 2026/01/15 15:44:41 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    try:
        f = open("ancient_fragment.txt")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("ERROR: Storage vault is like my motivation: "
              "nowhere to be found.")


if __name__ == "__main__":
    main()

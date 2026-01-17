# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_vault_security.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/17 07:27:46 by bfitte            #+#    #+#             #
#    Updated: 2026/01/17 07:27:47 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("\nSECURE EXTRACTION:")
    with open("classified_data.txt", "r") as f:
        print(f.read())
    try:
        f.read()
    except ValueError as e:
        print(e)
        print("Oops I almost erased some olds datas! Luckily, I protected "
              "it with the with statement!")
    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", "a") as f:
        f.write("\nVault automatically sealed upon completion")
    try:
        f.read()
    except ValueError:
        try:
            with open("security_protocols.txt", "r") as f:
                print(f.read())
        except ValueError:
            print("Oops I almost erased some olds datas! Luckily, I protected "
                  "it with the with statement!")


if __name__ == "__main__":
    main()

# Prog. 669
# Write a function to check whether the given ip address is valid or not using regex.

# References:
# - https://www.ibm.com/docs/en/ts4500-tape-library?topic=functionality-ipv4-ipv6-address-formats
# - https://regexone.com/lesson/nested_groups


import re

octet_pattern = r"((((2[0-4])|(1[0-9])|[1-9])?[0-9])|(25[0-5]))"
ip_v4_pattern = f"^({octet_pattern}.){{3}}{octet_pattern}$"

hex_digit_pattern = r"([0-9a-fA-F])" 
segment_pattern = f"({hex_digit_pattern}{{1,4}})"

ip_v6_pattern = f"^((({segment_pattern}:){{7}}{segment_pattern})|(({segment_pattern}:){{0,6}}{segment_pattern})?::)|(::({segment_pattern}:){{0,6}}{segment_pattern})$"

def is_valid_ip(ip_address: str) -> bool:
    match = None
    
    match = re.search(ip_v4_pattern, ip_address)

    if match is None:
        match = re.search(ip_v6_pattern, ip_address)

    return match is not None

if __name__ == "__main__":
    ip_address ="2001:0db8:0001:0000:0000:0ab9:C0A8:0102"
    
    print(is_valid_ip(ip_address))
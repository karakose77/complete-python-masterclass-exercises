def ip_divider():
    """
    Divides IP number segments and return separate segments with its lengths.
    """
    ip_address = input("Please enter the IP address: ")
    ip_address_dot = ip_address + "."
    segment = ""
    ip_segments = []
    print("")
    for char in ip_address_dot:
        if char != ".":
            segment += char
        elif char == "." and segment != "":
            ip_segments.append(segment)
            ip_segments.append(len(segment))
            print(f"Segment {segment:3} contains {len(segment)} characters.")
            segment = ""
    print("")
    return ip_segments


ip_divider()

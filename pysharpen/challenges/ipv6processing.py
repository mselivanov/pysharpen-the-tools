UNKNOW_IPV4_ADDRESS = '0.0.0.0'
UNKNOW_IPV6_ADDRESS = '0:0:0:0:0:0:0:0'
UNKNOW_IPV6_ADDRESS_LIST = UNKNOW_IPV6_ADDRESS.split(':')
IPV6_GROUPS_NUMBER = 8

def normalize_ipv6(ip_addr):
    """
    Function expands shorhand IPv6 notation :: into groups of zeroes
    :param ip_addr: list of ip address components
    return list of 8 ip address components
    """
    num_groups = len(ip_addr)
    if not ip_addr or num_groups < 3:
        raise ValueError('IP address must contain at least 3 groups')
    if num_groups == 3:
        if ip_addr == ['', '', '']:
            return UNKNOW_IPV6_ADDRESS_LIST
        if ip_addr[0] == '' and ip_addr[1] == '':
            normalized_ip_addr = ['0']*7
            normalized_ip_addr.append(ip_addr[2])
            return normalized_ip_addr
        if ip_addr[1] == '' and ip_addr[2] == '':
            normalized_ip_addr = [ip_addr[0]] + ['0'] * 7
            return normalized_ip_addr
    else:
        empty_groups_cnt = 0
        empty_group_idx = 0
        for idx, group in enumerate(ip_addr):
            if not group:
                empty_groups_cnt += 1
                empty_group_idx = idx
        if empty_groups_cnt > 1:
            ip_addr_str = ':'.join(ip_addr)
            raise ValueError(f'IP address {ip_addr_str} contains more than 1 empty group')
        elif empty_groups_cnt == 0:
            return ip_addr
        else:
            filler = ['0'] * (IPV6_GROUPS_NUMBER - num_groups + 1)
            normalized_ip_addr = ip_addr[:empty_group_idx]
            if num_groups == empty_group_idx + 1:
                normalized_ip_addr = normalized_ip_addr + filler
            else:
                normalized_ip_addr = normalized_ip_addr + filler + ip_addr[empty_group_idx+1:]
            return normalized_ip_addr


def main():
    # Empty IP address
    ip_addr = normalize_ipv6(['', '', ''])
    print(ip_addr)

    # First is set 
    ip_addr = normalize_ipv6(['2a00', '', ''])
    print(ip_addr)

    # Last is set 
    ip_addr = normalize_ipv6(['', '', '4b4c'])
    print(ip_addr)

    # Shortening in the middle 
    ip_addr = normalize_ipv6(['2a2b', '1c1d', '', '4b4c'])
    print(ip_addr)

    # Invalid address shortening 
    ip_addr = normalize_ipv6(['2003', 'dc', 'd705', '7000', '41f', ''])
    print(ip_addr)

if __name__ == '__main__':
    main()
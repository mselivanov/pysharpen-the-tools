
def print_header(header, header_line_len=50, filler_str='-'):    
    filler_len = (int)((header_line_len - len(header)) / 2 / len(filler_str))
    filler = filler_str*filler_len
    print(f'{filler}{header}{filler}')
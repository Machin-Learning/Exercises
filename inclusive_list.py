def inclusive_list(start,end):
    
    if start > end:
        output_list = [x for x in range(start,end-1,-1)]
    else:
        output_list = [x for x in range(start,end+1)]
    return (output_list)

print(inclusive_list(1,5))
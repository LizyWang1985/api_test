

def is_ip(ip):
    num_list=ip.split(".")
    if len(num_list)!=4:
        return False
    for num in num_list
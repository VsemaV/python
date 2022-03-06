with open('nginx_logs.txt', encoding='utf-8') as file_base:

    result = []
    result_dict = {}

    for line in file_base:
        remote_addr = line[:line.find(' -')]
        request_type = line[line.find(' "') + 2:line.find(' /')]
        requested_resource = line[line.find('T ') + 2:line.find(' H')]
        result.append((remote_addr, request_type, requested_resource))
        result_dict.setdefault(remote_addr, 0)
        result_dict[remote_addr] += 1


result_dict = sorted(result_dict.items(), key=lambda number: number[1])
print(result_dict[-1])

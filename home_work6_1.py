with open('nginx_logs.txt', encoding='utf-8') as file_base:

    result = []

    for line in file_base:
        remote_addr = line[:line.find(' -')]
        request_type = line[line.find(' "') + 2:line.find(' /')]
        requested_resource = line[line.find('T ') + 2:line.find(' H')]
        result.append((remote_addr, request_type, requested_resource))

    print(result)

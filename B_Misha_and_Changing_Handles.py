def handle_changes(q, requests):
    handle_mapping = {}
    for request in requests:
        old, new = request.split()
        if old in handle_mapping:
            handle_mapping[new] = handle_mapping[old]
            del handle_mapping[old]
        else:
            handle_mapping[new] = old

    users_changed = len(handle_mapping)
    print(users_changed)
    for new, old in handle_mapping.items():
        print(old, new)


# Read input
q = int(input())
requests = []
for _ in range(q):
    request = input()
    requests.append(request)

# Solve the problem
handle_changes(q, requests)

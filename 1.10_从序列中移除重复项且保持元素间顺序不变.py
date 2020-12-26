def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__ == '__main__':
    a = [1,2,3,4,5,2,3,4,]
    print(list(dedupe(a)))

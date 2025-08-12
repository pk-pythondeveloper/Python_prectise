# def repeat(num_times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")
text = "The quick brown fox jumps over the lazy dog. The fox was very quick"
# print(text.split())


def repeting_fields(text):
    texts=text.split()
    # print(texts)
    duplicate=[]
    matching=[]
    for i in texts:
        if i in matching:
            duplicate.append(i.lower())
        else:
            matching.append(i.lower())
    print(matching,duplicate,"this is both of")
print(repeting_fields(text))
            
        


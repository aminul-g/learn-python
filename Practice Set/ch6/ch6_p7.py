post = input("Enter the post content: ")
name = "Aminul"
if name.lower() in post.lower():
    print(f"talking about {name}")
else:
    print(f"not about {name}")
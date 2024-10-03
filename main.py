
def print_hi(name):
    first_name = input("your firstname: ")
    last_name = input("your lastname: ")
    age = input("your age: ")
    occupation = input("your occupation: ")
    print(f"""{first_name + " " + last_name} is a {age}-year-old {occupation} who specializes in creating visually
stunning brand identities. She has a passion for art and technology, blending both to bring her clients' visions to life.""")

if __name__ == '__main__':
    print_hi('JONNY')

book_reviews ={
    "the alchemist": "😊 A magical journey of dreams and destiny",
    "tuesdays with marrie": "🤍 Deep, emotional, and full of life lessons",
    "atomic habits": "🤗 Super practical and motivating!",
    "life of pi": "🙂A unique adventure that blends faith and survival ",
    "ikigai": "🌙Calm,simple and beautiful - that makes you rethink life"
}
book=input("Enter the name of the book: ").lower()

found = False
for title in book_reviews:
    if title in book:
        print(book_reviews[title])
        found= True
        break
if not found:
    print("😅Haven't read it yet, but you could be the first to review it!")    
chapter_count_data = """
Genesis – 50
Exodus – 40
Leviticus – 27
Numbers – 36
Deuteronomy – 34
Joshua – 24
Judges – 21
Ruth – 4
1 Samuel – 31
2 Samuel – 24
1 Kings – 22
2 Kings – 25
1 Chronicles – 29
2 Chronicles – 36
Ezra – 10
Nehemiah – 13
Esther – 10
Job – 42
Psalms – 150
Proverbs – 31
Ecclesiastes – 12
"""

# lets what chapter Ecclesiastes 1 is by summing up to the book before it + n 
chapter_count_data = chapter_count_data.strip().split('\n')
chapter_count_data = [x.strip().split(' – ') for x in chapter_count_data]

def sum_to_book(book):
    book = book.lower()
    for i in range(len(chapter_count_data)):
        if chapter_count_data[i][0].lower() == book:
            return sum([int(x[1]) for x in chapter_count_data[:i]])

chapters_prior = sum_to_book('ecclesiastes')
print(chapters_prior + 1)

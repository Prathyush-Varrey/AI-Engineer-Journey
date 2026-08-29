"""
7. 🔥 AI Document Chunk Analyzer

Imagine you have a document that needs to be divided into chunks before being processed by an AI system.

Ask the user:

Enter document text:

Your program should:

Remove unnecessary spaces at the beginning/end.
Calculate the total number of characters.
Calculate the number of words.
Ask the user for the maximum number of words allowed per chunk.
Calculate how many chunks are required.
Display the result.

Example:

Document: Python is powerful for building AI applications

Maximum words per chunk: 3

Total words: 8
Chunks required: 3

Because:

Chunk 1 → Python is powerful
Chunk 2 → for building AI
Chunk 3 → applications
Challenge

If the user enters:

Maximum words per chunk: 4

the number of chunks should automatically change.

Don't hard-code the number of chunks.

You're combining:

String methods + type casting + loops + math + conditions.
"""

import math

# Remove unnecessary spaces at the beginning/end.
doc_text = input("Enter Document Text: ").strip()

#Calculate the total number of characters.
total_chars = len(doc_text)

# Calculate the number of words.
words = doc_text.split()
total_words = len(words)

# Ask the user for the maximum number of words allowed per chunk.
max_words_per_chunk = int(input("Maximum words per chunk: "))

if max_words_per_chunk <= 0:
    print("Maximum words per chunk must be greater than 0.")
else:
    # Calculate how many chunks are required.
    chunks_required = math.ceil(total_words / max_words_per_chunk)

    print(f"Document: {doc_text}")
    print(f"Max words per chunk: {max_words_per_chunk}")
    print(f"Total characters: {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Chunks required: {chunks_required}")

    #the below sol given by AI

    # Move forward by the maximum words allowed each time.
    for start_index in range(0, total_words, max_words_per_chunk):
        chunk_number = start_index // max_words_per_chunk + 1
        chunk = " ".join(words[start_index : start_index + max_words_per_chunk])
        print(f"Chunk {chunk_number} -> {chunk}")

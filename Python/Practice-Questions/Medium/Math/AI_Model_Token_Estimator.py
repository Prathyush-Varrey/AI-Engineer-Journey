"""
5. AI Model Token Estimator

Imagine you're building a simple tool that estimates how many chunks a document needs.

A document contains:

Total words: 1275

Each chunk can contain a maximum of:

300 words

You cannot have a partial chunk.

So:

1275 ÷ 300 = 4.25

But you need 5 chunks.

Build a program that asks for:

Total number of words
Maximum words per chunk

Then calculates the number of chunks required.

Example:

Total words: 1275
Words per chunk: 300


Chunks required: 5

This is deliberately an AI-engineering-flavored problem.
Think about why ordinary rounding isn't necessarily the correct solution.
"""

import math as math


total_number_of_words = int(input("Enter Total Number Of Words :"))
maximum_words_per_chunk = int(input("Enter Maximum words per chunk :"))

chunks_required = math.ceil(total_number_of_words / maximum_words_per_chunk)
print(f"Chunks_required : {chunks_required}")
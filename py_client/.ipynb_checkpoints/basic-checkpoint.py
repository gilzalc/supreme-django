import praw
"""
Reddit:
id : 
uMDtYdkzqU6OEw5tqzNQBQ
secret: 
G1rN_T0bpOyVXz3xiONPdlnjcxrcBg
name: 
app123
user: 
Ok-Guess7756
"""
if __name__ == '__main__':
    sc.stop()
    from pyspark import SparkContext

    # Initialize SparkContext
    sc = SparkContext("local", "Text Processing Example")

    # Create an RDD from a text file
    lines_rdd = sc.textFile("prince.txt")

    # Split each line into words
    words_rdd = lines_rdd.flatMap(lambda line: line.split())

    # Map each word to a key-value pair with the word as key and count as value
    word_count_rdd = words_rdd.map(lambda word: (word, 1))

    # Reduce by key to aggregate word counts
    word_counts = word_count_rdd.reduceByKey(lambda x, y: x + y)

    # Sort the word counts by count in descending order
    sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=False)

    # Take the top 10 words by count
    top_words = sorted_word_counts.take(10)

    # Print the top words
    for word, count in top_words:
        print(f"{word}: {count}")


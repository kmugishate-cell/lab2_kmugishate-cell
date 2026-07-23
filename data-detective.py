import csv
import sys
import os


def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)

    return raw_tweets


def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    clean_tweets = []
    fixed_count = 0
    removed_count = 0

    for tweet in tweets:
        text = tweet.get("Text")

        # If Text is missing/empty, skip (remove) this tweet entirely
        if text is None or text.strip() == "":
            removed_count += 1
            continue

        row_was_fixed = False

        # Replace empty/missing Likes with 0
        likes = tweet.get("Likes")
        if likes is None or str(likes).strip() == "":
            tweet["Likes"] = "0"
            row_was_fixed = True

        # Replace empty/missing Retweets with 0
        retweets = tweet.get("Retweets")
        if retweets is None or str(retweets).strip() == "":
            tweet["Retweets"] = "0"
            row_was_fixed = True

        if row_was_fixed:
            fixed_count += 1

        clean_tweets.append(tweet)

    print(f"Data Audit Complete: {fixed_count} row(s) fixed, "
          f"{removed_count} row(s) removed.\n")

    return clean_tweets


def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
    if not tweets:
        print("No tweets available to check for a viral post.\n")
        return None

    top_tweet = tweets[0]
    highest_likes = int(top_tweet["Likes"])

    for tweet in tweets[1:]:
        current_likes = int(tweet["Likes"])
        if current_likes > highest_likes:
            highest_likes = current_likes
            top_tweet = tweet

    print("Most Viral Tweet:")
    print(f"  Username: {top_tweet.get('Username')}")
    print(f"  Likes:    {top_tweet.get('Likes')}")
    print(f"  Text:     {top_tweet.get('Text')}\n")

    return top_tweet


def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list
    by 'Likes' in descending order. NO .sort() allowed!
    """
    sorted_tweets = list(tweets)
    n = len(sorted_tweets)

    # Selection Sort (descending)
    for i in range(n):
        max_index = i
        max_likes = int(sorted_tweets[max_index]["Likes"])

        for j in range(i + 1, n):
            current_likes = int(sorted_tweets[j]["Likes"])
            if current_likes > max_likes:
                max_likes = current_likes
                max_index = j

        if max_index != i:
            sorted_tweets[i], sorted_tweets[max_index] = (
                sorted_tweets[max_index],
                sorted_tweets[i],
            )

    return sorted_tweets


def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    matches = []
    keyword_lower = keyword.lower()

    for tweet in tweets:
        text = tweet.get("Text", "")
        if keyword_lower in text.lower():
            matches.append(tweet)

    print(f"\nFound {len(matches)} tweet(s) matching '{keyword}':\n")
    for tweet in matches:
        print(f"  @{tweet.get('Username')}: {tweet.get('Text')}")
    print()

    return matches


if __name__ == "__main__":
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")

    clean_dataset = clean_data(dataset)
    print(f"{len(clean_dataset)} tweets remain after cleaning.\n")

    find_viral_tweet(clean_dataset)

    sorted_dataset = custom_sort_by_likes(clean_dataset)
    print("Top 10 Most Liked Tweets:")
    for i, tweet in enumerate(sorted_dataset[:10], start=1):
        print(f"  {i}. @{tweet.get('Username')} "
              f"({tweet.get('Likes')} likes): {tweet.get('Text')}")
    print()

    search_word = input("Enter a keyword to search for in tweets: ")
    search_tweets(clean_dataset, search_word)

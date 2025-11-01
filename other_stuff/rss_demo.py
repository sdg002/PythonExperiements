"""
https://stackoverflow.com/questions/22211795/python-feedparser-how-can-i-check-for-new-rss-data

What did I do ?
Get entries from BBC RSS feed using feedparser module.

What is the return value?
A dictionary containing feed information and entries. The 'entries' key contains a list of feed entries.

What did I learn?
etag and modified values can be used to check for updates in the feed. These were None for BBC feed.

What did not work?
In case of BBC feed, etag and modified values were None. So could not demonstrate their usage effectively.
When I passed a value for the modified parameter - it returned all entries again.
"""
import logging
import feedparser



BBC="http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml"

def main():
    try:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Starting the RSS demo script.")
        feed = feedparser.parse(BBC)
        logging.info("Feed title: %s", feed.feed.title)
        logging.info("Feed link: %s", feed.feed.link)
        logging.info("Feed description: %s", feed.feed.description)
        logging.info("Number of entries in feed: %d", len(feed.entries))
        for entry in feed.entries[:5]:  # Limiting to first 5 entries for brevity
            logging.info("Title: %s", entry.title)
            logging.info("Link: %s", entry.link)
            logging.info("Published: %s", entry.published)
            #logging.info("ETag: %s", entry.etag) #etag does not exist
            logging.info("-" * 40)
        logging.info("RSS demo script completed successfully.")
        last_etag   = feed.get('etag', None)
        last_modified = feed.get('modified', None)
        logging.info("ETag: %s", last_etag)
        logging.info("Last Modified: %s", last_modified)

        logging.info("Most recent entry published date: %s", feed.entries[0]["published"])
        logging.info("Oldest entry published date: %s", feed.entries[-1]["published"])

        logging.info("Query the feed again to check for updates. But this time use modified values.")
        middle_entry = feed.entries[len(feed.entries) // 2]
        middle_entry_date = middle_entry["published"]
        logging.info("Using published date of middle entry: %s", middle_entry_date)
        new_feed = feedparser.parse(BBC,  modified=middle_entry_date)
        logging.info("Number of entries in new feed: %d", len(new_feed.entries))
    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)

if __name__ == "__main__":
    main()

from collections import Counter


def get_lyrics():
    with open("C:\\BootCamp\\DataAnalyticsMW\\Week 15-Interactive-Visualizations-and-Dashboards\\3\\Activities\\Student\\Song_Lyrics\\Solved\\lyrics.txt") as fh:
        lyrics = [line.strip() for line in fh if line.strip()]
        return Counter(lyrics)


if __name__ == '__main__':
    lyrics = get_lyrics()
    labels, values = zip(*lyrics.items())

    print(labels, values)

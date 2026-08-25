# playlist.py (starter)
playlist = ["Here Comes the Sun", "Blue in Green", "All of Me"]


def add_song(title):
    """Add title to the global playlist. (No return)"""
    playlist.append(title)


def remove_song(title):
    """Remove first matching title from playlist.
    Returns True if removed, False if not found.
    """
    if title in playlist:
        playlist.remove(title)
        return True
    else:
        return False


def find_song(title):
    """Return the index of title if found, otherwise return -1."""
    if title in playlist:
        return playlist.index(title)
    else:
        return -1


def get_playlist_copy():
    """Return a shallow copy of the playlist."""
    return playlist.copy()


def replace_song(old, new):
    """Replace first occurrence of old with new.
    Return (index, new) if replaced, else None.
    """
    idx = find_song(old)

    if idx == -1:
        return None

    playlist[idx] = new
    return (idx, new)


def main():
    print("Initial playlist:", playlist)

    add_song("Dream a Little Dream")
    print("After add:", playlist)

    removed = remove_song("All of Me")
    print("Removed 'All of Me'?", removed)

    print("Index of 'Blue in Green':", find_song("Blue in Green"))

    copy = get_playlist_copy()
    print("Copy:", copy)

    rep = replace_song("Here Comes the Sun", "Here Comes the Night")
    print("Replace result:", rep)

    print("Final playlist:", playlist)


if __name__ == "__main__":
    main()
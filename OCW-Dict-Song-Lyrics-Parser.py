# -*- coding: utf-8 -*-
"""
Created on Mon Jan 04 2021 - 10:22
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Dictionaries 
This is an excercise from OCW MIT 6001 course

Lyrics parser with a dictionary

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
def toTextOnly(s):
    """
    Parameters
    ----------
    s : string
        Song lyrics string

    Returns
    -------
    converted : string
        A copy of s with removed punctuation and all letters turned to lowercase.

    """
    s = s.lower()
    converted = ''
    for c in s:
        if c in "abcdefghijklmnopqrstuvwxyz ":
            converted += c
    return converted

def populateDict(l,d):
    """ Assumes l is a list with strings and d is an empty dictionary
        Takes each string and checks if it exists as a key in the dict
        If it does - it increases the value of that key by 1
        If it doesn't - it creates the key with value 1
        
    Parameters
    ----------
    l : list
        list with strings.
    d : dict
        empty dictionary.

    Returns
    -------
    d : dict
        contains distinct list entries as keys and their number of occurences as values

    """
    for e in l:
        if e in d:
            d[e] = d[e] + 1
        else:
            d[e] = 1
    return d
    
# Start 

lyrics = """'A Place In This World

I don't know what I want, so don't ask me
Cause I'm still trying to figure it out
Don't know what's down this road, I'm just walking
Trying to see through the rain coming down
Even though I'm not the only one
Who feels the way I do

[Chorus:]
I'm alone, on my own, and that's all I know
I'll be strong, I'll be wrong, oh but life goes on
Oh, I'm just a girl, trying to find a place in this world

Got the radio on, my old blue jeans
And I'm wearing my heart on my sleeve
Feeling lucky today, got the sunshine
Could you tell me what more do I need
And tomorrow's just a mystery, oh yeah
But that's ok

[Chorus]

Maybe I'm just a girl on a mission
But I'm ready to fly

I'm alone, on my own, and that's all I know
I'll be strong, I'll be wrong, oh but life goes on
Oh I'm alone, on my own, and that's all I know
Oh I'm just a girl, trying to find a place in this world

Oh I'm just a girl
Oh I'm just a girl, oh, oh,
Oh I'm just a girl
"""

# 1 Step

lyricsTextOnly = toTextOnly(lyrics)

# 2 Step

lyricsList = lyricsTextOnly.split(" ")

# 3 Step

lyricsDict = {}
lyricsDict = populateDict(lyricsList,lyricsDict)

# 3 Step
print(lyricsDict)

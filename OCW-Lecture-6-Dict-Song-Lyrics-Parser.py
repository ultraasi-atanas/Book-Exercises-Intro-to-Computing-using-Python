# -*- coding: utf-8 -*-
"""
Created on Mon Jan 04 2021 - 10:22
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed

A complimentary exercise from the book companion, 
the OCW video lecture series - Lecture 6

Song Lyrics parser

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/index.htm


@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
def removePunctuation(s):
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



def lyrics_to_frequencies(l):
    """ Assumes l is a list with strings
        Takes each string and checks if it exists as a key in the dict
        If it does - it increases the value of that key by 1
        If it doesn't - it creates the key with value 1
        
    Parameters
    ----------
    l : list
        list with strings, words of song lyrics.

    Returns
    -------
    frequenciesDict : dict
        contains distinct list entries as keys and their number of occurences as values

    """
    frequenciesDict = {}
    for word in l:
        if word in frequenciesDict:
            frequenciesDict[word] = frequenciesDict[word] + 1
        else:
            frequenciesDict[word] = 1
    return frequenciesDict


def mostCommon(d):
    """
    Parameters
    ----------
    d : dict
        words and frequencies value pairs

    Returns
    -------
    a tuple containing the highest frequency and the respective word(s) list
    """
    mostCommonValue = max(d.values())
    results = []
    for e in d:
        if d[e] == mostCommonValue:
            results.append(e)
    return (results,mostCommonValue)
    
    
# 1 Step 

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

# 2 Step

lyricsNoLineEnds = lyrics.replace('\n',' ')
lyricsTextOnly = removePunctuation(lyricsNoLineEnds)
lyricsList = lyricsTextOnly.split(' ')    

# 3 Step

lyricsFrequencies = lyrics_to_frequencies(lyricsList)

# 4 Step

print(lyricsFrequencies)
print('Most common word is:', mostCommon(lyricsFrequencies))

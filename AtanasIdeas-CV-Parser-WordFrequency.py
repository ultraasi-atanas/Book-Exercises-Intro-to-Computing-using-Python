# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 2021 - 11:04
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed

CV Parser - Word Frequencies

See my other example called OCW-Lecture-6-Dict-Song-Lyrics-Parser

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



def cv_to_frequencies(l):
    """ Assumes l is a list with strings
        Takes each string and checks if it exists as a key in the dict
        If it does - it increases the value of that key by 1
        If it doesn't - it creates the key with value 1
        
    Parameters
    ----------
    l : list
        list with strings

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

cv = """• Managed an education centre of over 250 members; regularly monitoring KPI’s using Power BI and working towards challenging targets to increase membership.
• Ensured commercial success of the centre; Analysed Profit and Loss statements to monitor quarterly controllable costs with a successful record of centre efficiency through regular supervision of staff hours and outgoings. 
• Mastered skills in performance analysis to forecast sales targets and implement effective marketing strategies to grow the business. 
• Acting as a representative of the centre in a wide range of situations; thinking at both an operational and strategic level. 
• Head of recruitment; hired, trained and developed a team of part-time tutors to upskill them and improve quality of service.
• Researching and hosting marketing events and building a positive reputation for the centre in the local community, liaising with schools, libraries, the media and businesses.

Managerial role

• Managed an education centre of over 250 members; regularly monitoring KPI’s using Power BI and working towards challenging targets to increase membership.
• Ensured commercial success of the centre; Analysed Profit and Loss statements to monitor quarterly controllable costs with a successful record of centre efficiency through regular supervision of staff hours and outgoings. 
• Mastered skills in performance analysis to forecast sales targets and implement effective marketing strategies to grow the business. 
• Acting as a representative of the centre in a wide range of situations; thinking at both an operational and strategic level. 
• Head of recruitment; hired, trained and developed a team of part-time tutors to upskill them and improve quality of service.
• Researching and hosting marketing events and building a positive reputation for the centre in the local community, liaising with schools, libraries, the media and businesses.

Customer Service

• Advanced handling of processes and data to provide immediate support and advice to mechanics at vehicle breakdown scenes in a professional manner.
• Mastered mapping and tracking mechanics with advanced geographical knowledge to ensure they are sent to breakdowns of their ability securing a high-quality and efficient service. 
• Excellent communication with police and highway services to ensure immediate action and safety. Compromised with our contractors for prompt repair and storage of member vehicles.
• Excelled in performance of AA values; Courtesy, Care, Expertise, Collaboration and Dynamism. Proven outstanding telephone manner, cooperating in a team environment, working diligently to achieve KPI's and remaining calm in a fast-paced, pressured environment.

Food

• Responsible for smooth running of store; often having overall responsibility of taking orders, making desserts and serving customers in a timely manner.
• Implemented excellent marketing strategies to promote the business and built great rapport with customers.
• Participated frequently in managerial meetings and contributed with new ideas/recipes to expand the store variety and stand out from local competitors.


Retail

• Mastered retail duties of stocking shelves, serving customers at tills, operating fitting rooms and ensured tidiness of the store during promotional periods. 
• Proven ability to problem-solve during complex processes.
• Trained new staff on the shop floor, dealt with customer complaints and escalated issues to management level where necessary.

"""

# 2 Step

cvNoLineEnds = cv.replace('\n',' ')
cvTextOnly = removePunctuation(cvNoLineEnds)
cvList = cvTextOnly.split(' ')    

# 3 Step

cvFrequencies = cv_to_frequencies(cvList)

# 4 Step

print(cvFrequencies)
print('Most common word is:', mostCommon(cvFrequencies))

from music21 import *

b = corpus.parse('beethoven/opus18no1/movement3.mxl')
# b.show()

"""Select an excerpt, and chordify"""
b_asection = b.measures(1, 10)
b_asection_chords = b_asection.chordify()
# b_asection_chords.show()

"""For every dominant seventh chord, print the measure number, beat, and chord"""
# for this_chord in b_asection_chords.recurse().getElementsByClass('Chord'):
#     if this_chord.isDominantSeventh():
#         print(this_chord.measureNumber, this_chord.beatStr, this_chord)

"""Compress the chordified chords into closed position in a smaller range"""
for c in b_asection_chords.recurse().getElementsByClass('Chord'):
    c.closedPosition(forceOctave=4, inPlace=True)
# b_asection_chords.show()

"""Add a new staff to the score with the condensed chords"""
b_asection.insert(0, b_asection_chords)
# b_asection.show()

"""Identify the harmony of each chord. Either print or show."""
"""Music21 can identify extended tertian harmonies up to 13th, including chords with omitted pitches"""
for c in b_asection_chords.recurse().getElementsByClass('Chord'):
    harm = harmony.chordSymbolFigureFromChord(c, True)
    # print(harm)
    # c.addLyric(str(harm))

# b_asection.show()

"""Given a key, identify the roman numeral for each chord. This can give some crazy roman numerals"""
# for c in b_asection_chords.recurse().getElementsByClass('Chord'):
#     rn = roman.romanNumeralFromChord(c, key.Key('F'))
#     print(rn)
#     c.addLyric(str(rn.figure))
#
# b_asection.show()

"""You can create your own chord for music21 to identify"""
# harmony.addNewChordSymbol('Jenn_Chord', '1, 2, 3, -5, +8', ['JDH', 'jenn'])
# for p in harmony.ChordSymbol('F#jenn').pitches:
#     print(p)

"""Set or get the roman numeral based on key"""
# dom = roman.RomanNumeral('V')
# print(dom.pitches)  # Default key is C Major
# dom.key = key.Key('f#')
# print(dom.pitches)

"""Music21 can also do serial set-class analysis"""

"""You can find the pitch classes of a sonority"""
# for c in b_asection_chords.recurse().getElementsByClass('Chord'):
#     pc_string = c.orderedPitchClassesString
#     print(pc_string)

"""You can find the prime forms of every sonority"""
# for c in b_asection_chords.recurse().getElementsByClass('Chord'):
#     pf_string = c.primeFormString
#     print(pf_string)
#     c.addLyric(pf_string)
#
# b_asection.show()


"""You can set a tone row as a list. Make sure that 'a' and 'b' are strings!"""
mallalieu = serial.pcToToneRow([0, 1, 4, 2, 9, 5, 11, 3, 8, 10, 7, 6])
# mallalieu.show('text')

"""Show the row as a matrix"""
# mallalieu_matrix = mallalieu.matrix()
# print(mallalieu_matrix)

"""Print each of the intervals between notes in the row"""
# for i in mallalieu.getIntervalsAsString():
#     print(i)

"""Print the row as note names, not integers"""
# note_names = mallalieu.noteNames()
# print(note_names)

"""Is the row an all interval row?"""
# print(mallalieu.isAllInterval())

"""You can use historical rows as well"""
schoe = serial.getHistoricalRowByName('RowSchoenbergOp37')
schoe.show('text')

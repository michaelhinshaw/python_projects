

#parent class
class Progression:
    key = "Unknown"
    majorchords = "Unknown"
    minorchords = "Unknown"
    diminishedchords = "Unknown"
    cadence = "Unknown"
    diatonic = True

    def reference(self):
        msg = "Key: {}\nMajor Chords: {}\nMinor Chords: {}\nDiminished Chords: {}\nCadence: {}\n Diatonic: {}".format(self.key,self.majorchords,self.minorchords,self.diminishedchords,self.cadence,self.diatonic)
        return msg


class Major(Progression):
    key = 'Eb'
    majorchords = 'Eb, Ab, Bb'
    minorchords = 'Fm, Gm, Cm'
    cadence = 'Bb, Eb'
    sounds = 'peaceful'
    popular = True

    def basic(self):
        msg = "I use this key when I'm stuck writing. The Major Chords are {}\nand sprinkled with one or two of the Minor Chords {}\n the songs sound happy and {}.".format(self.majorchords,self.minorchords,self.sounds)
        return msg

class Diminished(Progression):
    key = 'C'
    majorchords = 'Cmaj7, A7'
    minorchords = 'Dm7, Em7'
    diminishedchords = 'C#7dim, D#7dim'
    cadence = 'Em7, A7'
    sounds = 'tense'
    diatonic = False
    chromatic = True
    genre = 'jazz'

    def tension(self):
        msg = "The diminished progressions contains chromatic movement with the {} chords.\nIt is prominent in {} music.".format(self.diminishedchords, self.genre)
        return msg
    
    




if __name__ == "__main__":
    major = Major()
    print(major.reference())
    print(major.basic())

    diminished = Diminished()
    print(diminished.tension())
    print(diminished.reference())
    

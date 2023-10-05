''' base class called Sequence'''
class Sequence:
    def __init__ (self, sequence):
        '''Initializes the sequence string object to be the DNA sequence'''
        self.sequence = sequence

    def get_sequence(self):
        '''returns the DNA sequence'''
        return self.sequence
    
    def calculate_length(self):
        '''calculates and returns length of the sequence'''
        return len(self.sequence)
    
    def count_nucleotides(self):
        '''counts and returns a dictionary that contains the number of each nucleotide (A, T, C, G) in the sequence'''
        count_nucleotides_dict = {
            'A' : 0,
            'T' : 0,
            'C' : 0,
            'G' : 0
        }
        for nucleotide in self.sequence:
            if nucleotide in count_nucleotides_dict:
                count_nucleotides_dict[nucleotide] = count_nucleotides_dict[nucleotide] + 1 #increments it by 1 each time the nucleotide at the particular index comes up in the sequence
        
        return count_nucleotides_dict

'''sub class called DNA that inherits from the sequence class (base)'''
class DNA(Sequence):
    def reverse_complement(self):
        '''returns the reverse complement of the DNA sequence'''
        nucleotide_complement_dict = {
            'A' : 'T',
            'T' : 'A',
            'C' : 'G',
            'G' : 'C'
        } # replaces each nucleotide with its complement (A with T, T with A, C with G, and G with C).
        reverse_sequence = self.sequence[::-1] #start at the end of the sequence(string) and end at position 0(beginning), move with the step -1(backwards)
        reverse_complement_sequence = ''

        for nucleotide in reverse_sequence:
            if nucleotide == 'A':
                reverse_complement_sequence = reverse_complement_sequence + 'T'
            elif nucleotide == 'T':
                reverse_complement_sequence = reverse_complement_sequence + 'A'
            elif nucleotide == 'C':
                reverse_complement_sequence = reverse_complement_sequence + 'G'
            elif nucleotide == 'G':
                reverse_complement_sequence = reverse_complement_sequence + 'C'
        
        return reverse_complement_sequence

    def find_pattern(self,pattern):
        '''returns the starting indices of all occurrences of a given pattern in the DNA sequence'''
        starting_indices = []
        for index in range(len(self.sequence) - len(pattern) + 1):
            if self.sequence[index:index + len(pattern)] == pattern:
                starting_indices.append(index)
        return starting_indices
    
    def calculate_gc_content(self):
        '''calculates and returns the GC content of the DNA sequence as a percentage'''
        if len(self.sequence) == 0:
            return 0
        count_gc = self.sequence.count('GC')  # Count 'GC' nucleotides
        count_gc_percentage = (count_gc * 2)/ (len(self.sequence)) * 100
        return count_gc_percentage
    
if __name__ == "__main__": 
    # Testing
    dna_sequence = "CGATTACGCTGAAAGCTTCGACGTGGTCCTT"

    # Create an instance of the DNA class
    dna = DNA(dna_sequence)

    # Test the implemented methods
    seq_length = dna.calculate_length()
    count_nucleotide = dna.count_nucleotides()
    reverse_complement = dna.reverse_complement()
    pattern_indices = dna.find_pattern('GG')
    gc_content = dna.calculate_gc_content()

    print("Original sequence:", dna.get_sequence())
    print("sequence length: ", seq_length)
    print("sequence nucleotides: ", count_nucleotide)
    print("Reverse complement:", reverse_complement)
    print("Pattern indices:", pattern_indices)
    print("GC content:", gc_content)
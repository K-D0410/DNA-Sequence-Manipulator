import unittest
from DNA_sequence import Sequence, DNA

class TestSequence(unittest.TestCase): 
    def setUp(self):
        """Attach attributes to TestCase object that are created fresh at the top of every test method below."""
        self.sequence = Sequence("CGATTACGCTGAAAGCTTCGACGTGGTCCTTA")
        self.sequence2 = Sequence("")

    def test_get_sequence(self):
        """test method get_sequence that returns the DNA sequence.""" 
        #Test a known sequence 
        self.assertEqual(self.sequence.get_sequence(), "CGATTACGCTGAAAGCTTCGACGTGGTCCTTA")
        #Test an empty sequence
        self.assertEqual(self.sequence2.get_sequence(), "")

    def test_calculate_length(self):
        """test method calculate_length that calculates the sequence length"""
        #Test a known sequence
        self.assertEqual(self.sequence.calculate_length(), 32)
        #Test an empty sequence
        self.assertEqual(self.sequence2.calculate_length(), 0)
    
    def test_count_nucleotides(self):
        """test method count_nucleotides that counts the number of each nucleotide in the sequence"""
        self.assertEqual(self.sequence.count_nucleotides(),{
            'A' : 7,
            'T' : 9,
            'C' : 8,
            'G' : 8
        })
    
class TestDNA(unittest.TestCase):
    def setUp(self):
        """Attach attributes to TestCase object that are created fresh at the top of every test method below."""
        self.dna = DNA("CGATTACGCTGAAAGCTTCGACGTGGTCCTTA")
        self.dna2 = DNA("")
    
    def test_reverse_complement(self):
        """test method reverse_complement that returns the reverse complement of the sequence"""
        self.assertEqual(self.dna.reverse_complement(), ("TAAGGACCACGTCGAAGCTTTCAGCGTAATCG"))
    
    def test_find_pattern(self):
        """test method find_pattern that returns the starting indices of a given pattern in the DNA sequence"""
        self.assertEqual(self.dna.find_pattern("GG"),[24])
    
    def test_calculate_gc_content(self):
        """test method calculate_gc_content that calculates the percentage of the GC content in the DNA sequence"""
        self.assertEqual(self.dna.calculate_gc_content(), 12.5)
        self.assertEqual(self.dna2.calculate_gc_content(), 0)

unittest.main()
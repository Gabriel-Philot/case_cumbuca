class DNA:
    def __init__(self, dna_seq, par_corresp=None):
        self.dna_seq = dna_seq.upper()
        if par_corresp is None:
            self.par_corresp = {
                'A': 'U',
                'C': 'G',
                'G': 'C',
                'T': 'A'
            }
        else:
            self.par_corresp = par_corresp
        
    def transcription(self):
        """
        Converte seq: DNA -> RNA.

        Retorna:
        str: seq de RNA.
        """
        rna_seq = ''
        for dnaitem in self.dna_seq:
            rna_corresp = self.par_corresp.get(dnaitem, '')
            rna_seq += rna_corresp
        return rna_seq
#open genomic dna text 
genomic_dna = open("genomic_dna.txt").read()

#opened exons txt 

exon_locations = open("exons.txt")

#created a variable to hold the sequence 

coding_sequence = ""

for line in exon_locations:

#split the line with a comma 
      positions = line.split(',')
#got the positions 
      start = int(positions[0])
      stop = int(positions[1])
#took the exons from the dna 
      exon = genomic_dna[start:stop]
#added the exons to the cooding sequence
      coding_sequence = coding_sequence + exon
#inputed it to another file 

output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()


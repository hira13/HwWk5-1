#open filed called input 
file = open("input.txt")

#print trimmed dna 
for dna in file:

   trimmed_dna = dna[14:]
   print(dna)

#open output file 

output = open("trimmed.txt", "w")

#trimmed length and printed after prcoessing 

trimmed_length = len(trimmed_dna)- 1

output.write(trimmed_dna)

print("processed sequence with length " + str(trimmed_length))

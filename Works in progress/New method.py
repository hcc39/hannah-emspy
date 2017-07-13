import csv
#generic function to extract information from CSV files and store them in a dictionary
def csv_export (file_location):
    generic_dict = {}
    with open(('C:/Users/HannahCharlotte/Documents/Research Projects/2017 HLA EMS Model/Hannah EMSPy/'+file_location), 'rb') as csvfile:
        list_reader = csv.reader(csvfile, delimiter = ',')
        for item in list_reader:
            k,v = item[0], item[1:]
            generic_dict[k] = v
    return generic_dict

#Dictionaries of each data set
aa_scores = csv_export('aa_scores.csv') # amino acid scores as a dictionary in form - Amino acid: [Hopp wooods score, EMS]
for k,(v,w) in aa_scores.iteritems(): #Convert amino acid scores into floats from strings
    aa_scores[k] = [float(v), float(w)]
hla_aa_sequence = csv_export('hla_aa_sequence.csv') # hla sequence as a dictionary in form - "A*01:01": ["A", "B", etc ].
hla_donor_recipient = csv_export('donor_recipient_hla.csv') # comparison as a dictionary in form - "1" : [Donor hla, Recipient hla x 6]

# Convert donor / recipient inputs into scored output
def score_conversion():
    for pairing in hla_donor_recipient: # Pairing refers to each comparison set to be run
        donor_aminoacid_sequence = hla_aa_sequence[hla_donor_recipient[pairing][0]] #Convert donor HLA to donor amino acid sequence
        recipient_aminoacid_sequences = [hla_aa_sequence[p] for p in hla_donor_recipient[pairing][1:]] #Convert recipient HLA(x6) to recipient amino acid sequences

        total_smallest_difference = [0,0]
        for i in range(len(donor_aminoacid_sequence)): #Iterate over all 276 amino acid residues
            for score_index in range(2): #Perform calculation for both of Hopp-Woods and EMS scores hence range = 2
                #Calculate difference between score for donor amino acid score at given residue and recipient equivalent score for each HLA:

                difference = [aa_scores[donor_aminoacid_sequence[i]][score_index] - aa_scores[r[i]][score_index] for r in recipient_aminoacid_sequences]
                if any(difference): #Filters out lines where all differences are equal to zero (ie lines where all amino acids are the same or have the same score)
                    smallest_difference = min([d for d in difference if d != 0], key=lambda x: abs(x)) #extracts the smallest non zero score for a comparison of residue scores
                    total_smallest_difference[score_index] += smallest_difference #Sum smallest difference in scores for both systems

        return total_smallest_difference
    pass


print score_conversion()

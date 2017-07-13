import csv

#Function: Export CSV inputs in variables
file_path = 'C:/Users/HannahCharlotte/Documents/Research Projects/2017 HLA EMS Model/Hannah EMSPy/'
def csv_export (file_name):
    generic_dict = {}
    with open((file_path+file_name), 'rb') as csvfile:
        list_reader = csv.reader(csvfile, delimiter = ',')
        for item in list_reader:
            k,v = item[0], item[1:]
            generic_dict[k] = v
    return generic_dict

#Create dictionary for each data input
aa_scores = csv_export('aa_scores.csv') # amino acid scores as a dictionary in form - Amino acid: [Hopp wooods score, EMS]
for k,(v,w) in aa_scores.iteritems(): #Convert amino acid scores into floats from strings
    aa_scores[k] = [float(v), float(w)]
hla_aa_sequence = csv_export('hla_aa_sequence.csv') # hla sequence as a dictionary in form - "A*01:01": ["A", "B", etc ].
hla_donor_recipient = csv_export('donor_recipient_hla.csv') # comparison as a dictionary in form - "1" : [Donor hla, Recipient hla x 6]

# Main function conversion
def score_conversion():
    score_output = {}
    for pairing in hla_donor_recipient:
    # Pairing refers to each comparison set to be run
        donor_aminoacid_sequence = hla_aa_sequence[hla_donor_recipient[pairing][0]]
        # Convert donor HLA to donor amino acid sequence
        recipient_aminoacid_sequences = [hla_aa_sequence[p] for p in hla_donor_recipient[pairing][1:]]
        # Convert recipient HLA(x6) to recipient amino acid sequences
        total_smallest_difference = [0,0]
        for i in range(len(donor_aminoacid_sequence)):
        # Iterate over all 276 amino acid residues
            for score_index in range(2):
            # Perform calculation for both of Hopp-Woods and EMS scores hence range = 2
                if donor_aminoacid_sequence[i] in aa_scores.keys():
                # Calculate score only if valid amino acid input at given residue on donor HLA i.e. filters out missing residues on donor
                        difference = [aa_scores[donor_aminoacid_sequence[i]][score_index] - aa_scores[r[i]][score_index] for r in recipient_aminoacid_sequences if r[i] in aa_scores.keys()]
                        #Calculate difference between donor score and each recipient score if recipient score is a valid amino acid
                        if any(difference):
                        #Filters out lines where all differences are zero
                            smallest_difference = min([d for d in difference if d != 0], key=lambda x: abs(x))
                            # Extracts the smallest non zero score for a comparison of residue scores
                            total_smallest_difference[score_index] += smallest_difference
                            # Sum smallest difference in scores for both systems
        score_output[pairing] = total_smallest_difference
        #Add scores to a dictionary of keys and values = output
    return score_output
output = score_conversion()

#Write output to a CSV file
with open(file_path+"output.csv", 'wb') as myfile:
    wr = csv.writer(myfile, delimiter=',')
    for k, v in output.items():
        v = [round(item,2) for item in v]
        wr.writerow([k] + v)
import csv
import pandas as pd

def data_extract (input):
    list_output = {}
    for number in input:
        k,v = row[0], row[1:]
        list_output[k] = v
    return list_output

aa_scores = {} #Populate amino acid scores dictionary. Format "Amino acid code": [Hopp woods score, electrostatic score]
with open('C:/Users/HannahCharlotte/Documents/Research Projects/2017 HLA EMS Model/Hannah EMSPy/aa_scores.csv', 'rb') as csvfile:
    aa_scores_reader = csv.reader(csvfile, delimiter = ',')
    for row in aa_scores_reader:
        k,v = row[0], row[1:]
        aa_scores[k] = v

aa_scores_2 = {}  # Populate amino acid scores dictionary. Format "Amino acid code": [Hopp woods score, electrostatic score]
with open('C:/Users/HannahCharlotte/Documents/Research Projects/2017 HLA EMS Model/Hannah EMSPy/aa_scores.csv', 'rb') as csvfile:
    aa_scores_reader = csv.reader(csvfile, delimiter=',')
    aa_scores_2 = data_extract(aa_scores_reader)

print aa_scores_2

#print pd.Series.from_csv('C:/Users/HannahCharlotte/Documents/Research Projects/2017 HLA EMS Model/Hannah EMSPy/aa_scores.csv', header=None).to_dict()

hla_aa_sequence = {} #Dictionary of HLA amino acid sequence in form "HLA name": [aa 1, aa2 etc]
with open('C:/Users/HannahCharlotte/Documents/Research Projects/2017 HLA EMS Model/Hannah EMSPy/hla_aa_sequence.csv', 'rb') as csvfile:
    hla_aa_sequence_reader = csv.reader(csvfile, delimiter = ',')
    for row in hla_aa_sequence_reader:
        k,v = row[0], row[1:]
        hla_aa_sequence[k] = v

hla_donor_recipient = {} #Dictionary of donor / recipient HLA in the form: Identifier: Donor HLA, Recipient HLA (x6)
with open('C:/Users/HannahCharlotte/Documents/Research Projects/2017 HLA EMS Model/Hannah EMSPy/donor_recipient_hla.csv', 'rb') as csvfile:
    next(csvfile)
    donor_recipient_hla_reader = csv.reader(csvfile, delimiter = ',')
    for row in donor_recipient_hla_reader:
        k,v = row[0], row[1:]
        hla_donor_recipient[k] = v

print hla_donor_recipient

class HLA_aminoacid_lists(object): #Create lists of donor / recipient hopp woods and electrostatic scores
    def __init__ (self, donor_hla, recipient_hla):
        self.donor_hla = donor_hla
        self.recipient_hla = recipient_hla
    def donor_hopp_woods(self):
        donor_hopp_woods_list = []
        for aminoacid in (hla_aa_sequence[self.donor_hla]):
            donor_hopp_woods_list.append(aa_scores[aminoacid][0])
        return donor_hopp_woods_list
    def donor_electrostatic (self):
        donor_electrostatic_list = []
        for aminoacid in (hla_aa_sequence[self.donor_hla]):
            donor_electrostatic_list.append(aa_scores[aminoacid][1])
        return donor_electrostatic_list
    def recipient_hopp_woods(self):
        recipient_amino_acids = []
        for hla in self.recipient_hla:
            recipient_amino_acids.append(hla_aa_sequence[hla])
        recipient_hopp_woods_list = []
        for list in recipient_amino_acids:
            half_list = []
            for aminoacid in list:
                half_list.append(aa_scores[aminoacid][0])
            recipient_hopp_woods_list.append(half_list)
        return recipient_hopp_woods_list

#Convert dictionaries into their scores and have one for hopp woods and one for electrostatic for each of donor and recipient
class HLA_score_conversion (object):
    def __init__(self, donor_aa_list, recipient_aa_list):
        self.donor_aa_list = donor_aa_list
        self.recipient_aa_list = recipient_aa_list
    def recipient_electrostatic (self):
        recipient_electrostatic_list = []
        for list in self.recipient_aa_list:
            half_list = []
            for aminoacid in list:
                half_list.append(aa_scores[aminoacid][1])
            recipient_electrostatic_list.append(half_list)
        return recipient_electrostatic_list

test_1 = HLA_aminoacid_lists("C*06:04", ["C*06:04", "A*66:04"])
#test_2 = HLA_score_conversion(test_1.donor_amino_acid_list(), test_1.recipient_amino_acid_list())
#print test_1.donor_hopp_woods()
#print test_1.donor_electrostatic()
#print test_1.recipient_hopp_woods()
#print test_2.recipient_electrostatic()


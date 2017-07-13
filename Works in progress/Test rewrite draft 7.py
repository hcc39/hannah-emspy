import csv
import numpy as np

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
aa_scores = csv_export('aa_scores.csv') # amino acid scores as a dictionary
hla_aa_sequence = csv_export('hla_aa_sequence.csv') # hla sequence as a dictionary with HLA as key
hla_donor_recipient = csv_export('donor_recipient_hla.csv') # comparison as a dictionary in form key: values = donor, recipient
hla_donor_recipient["2"] = ['B*53:01', 'A*24:02', 'A*24:02', 'A*24:02', 'A*24:02', 'A*24:02', 'A*24:02']


def amino_acid_comparison (hla_d_r):
    donor_and_recipient_list = [hla_d_r[key] for key in hla_d_r]
    multiple_donor_and_recipient_aminoacid_list = []
    for item in range(len(donor_and_recipient_list)):
        donor_and_recipient_aminoacid_list = [hla_aa_sequence[specific_hla] for specific_hla in(donor_and_recipient_list[item])]
        multiple_donor_and_recipient_aminoacid_list.append(donor_and_recipient_aminoacid_list)
    cross_section_list = [multiple_donor_and_recipient_aminoacid_list[0][x] for x in range (7)]
    #print cross_section_list

list = [[1,2,3,4],[11,12,13,14]],[[21,22,23,24],[211,212,213,214]]
b = list[0]
print b
c = np.array(b)
print c
d = c[:, [0]]
print d

a = amino_acid_comparison(hla_donor_recipient)
#multiple_donor_and_recipient_aminoacid_list = [pairing][hla][aminoacid]
print a
#print a[0][0][0]
#print a[1][0][0]

#def amino_acid_score_conversion(hla_d_r):
#    donor_and_recipient_list = [hla_d_r[key] for key in hla_d_r]
#    multiple_donor_and_recipient_aminoacid_list = []
#    for item in range(len(donor_and_recipient_list)):
#        donor_and_recipient_aminoacid_list = [hla_aa_sequence[specific_hla] for specific_hla in(donor_and_recipient_list[item])]
#        scores_list = []
#        for hla in donor_and_recipient_aminoacid_list:
#            for aminoacid in hla:
#                one_hla = [aa_scores[aminoacid] if aminoacid in aa_scores else "XXX" for aminoacid in hla]
#            scores_list.append(one_hla)
#        multiple_donor_and_recipient_aminoacid_list.append(scores_list)
#    return multiple_donor_and_recipient_aminoacid_list

#def score_calculator(scores_list_input, type):
#    cross_section_score = []
#    for residue in range(276):
#        cross_section_score.append([scores_list_input[x][residue][type] for x in range (7)])
#    cross_section_calculation = []
#    for position in cross_section_score:
#        intermediate = [(float(position[0]) - float(position[x])) for x in range(1,7)]
#        filtered = [x for x in intermediate if x != 0.0]
#        cross_section_calculation.append(filtered)
#    cross_section_shorten = [x for x in cross_section_calculation if x != []]
#    score_total = 0
#    for item in cross_section_shorten:
#        cross_section_smallest = min(item, key=lambda x:abs(x-0))
#        score_total+=cross_section_smallest
#    return score_total

#hla_donor_recipient["2"] = ['B*53:01', 'A*24:02', 'A*24:02', 'A*24:02', 'A*24:02', 'A*24:02', 'A*24:02']
#a = amino_acid_score_conversion(hla_donor_recipient)
# a = [set of donor and recipient info][hla][amino acid in given position][0 = hopp woods vs 1 = ems]
#if a[0][2] != a[1][2]:
#    print "no match"
#else:
#    print "match"

#b = a[0]
#c = a[1]

#print "Pair one:"
#print "Hopp Woods = ", score_calculator(b,0)
#print "EMS = ", score_calculator(b,1)

#example_scores_list = [[["a", "b"],["c", "d"]], [["1a", "1b"],["2a", "2b"]], [["3a", "3b"],["4a", "4b"]], [["5a", "5b"],["6a", "6b"]],  [["7a", "7b"],["8a", "8b"]], [["9a", "9b"],["10a", "10b"]], [["11a", "11b"],["12a", "12b"]]]
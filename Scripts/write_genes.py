import sys

#gene_file = sys.argv[1]
#out_file = sys.argv[2]
#print(gene_file)
#print(out_file)
dna_list=list('ACGT')
def getGeneList(gene_file):
    with open(gene_file, 'r') as humchr:
        tag = False
        gene_list = []
        for line in humchr:
            if line.startswith('Gene'):
                tag = True
            if tag:
                line_split = line.split()
                if len(line_split) != 0:
                    if '-' in line_split[0]:
                        continue
                    else:
                        gene_list.append(line_split[0])
    return gene_list[3:][:-2]

def writeGeneList(clean_gene_list,out_file):
    with open(out_file, 'w') as gene_names:
        for gene in clean_gene_list:
            gene_names.writelines(gene+'\n')
    print('Genes have been written Successfully')
    
#clean_gene_list = getGeneList(gene_file)
#writeGeneList(clean_gene_list,out_file)

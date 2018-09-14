#!/usr/bin/python3

import click
import pandas as pd

@click.command()
@click.argument('kraken_tsv')
@click.argument('new_file_name')
def kraken_classification(kraken_tsv, new_file_name):
    """replaces kraken taxonomy organism string as 'P' (plant), 'B' (bacteria), 'U' (unclassified), or 'F' (fungi)
    NOTE: more Tax IDs and their abbreviations can be added to the dictionary (rep_dict) as needed
    EXAMPLE:

    inputfile (tsv):
    transcript	Kraken_organism
    27_2_0	    Lupinus angustifolius (taxid 3871)
    27_2_73	    Glycine max (taxid 3847)
    27_2_421	unclassified (taxid 0)

    output file (csv):
    transcript	Kraken_organism
    27_2_0	    P
    27_2_73	    P
    27_2_421	U
"""
    rep_dict = dict([
    ('50 kb inversion clade (taxid 2231393)', 'P'),
    ('Cajanus cajan (taxid 3821)', 'P'), ('Brassica (taxid 3705)', 'P'),
    ('Brassica napus (taxid 3708)', 'P'), ('Brassica oleracea var. oleracea (taxid 109376)','P'),
    ('Brassica rapa (taxid 3711)', 'P'), ('Cajanus cajan (taxid 3821)', 'P'),
    ('Cicer arietinum (taxid 3827)', 'P'), ('Cucumis sativus (taxid 3659)', 'P'),
    ('Cucurbita pepo subsp. pepo (taxid 3664)','P'), ('Cynara cardunculus var. scolymus (taxid 59895)', 'P'),
    ('Daucus carota subsp. sativus (taxid 79200)', 'P'), ('Elaeis guineensis (taxid 51953)', 'P'),
    ('fabids (taxid 91835)', 'P'), ('Fragaria vesca subsp. vesca (taxid 101020)', 'P'),
    ('Glycine max (taxid 3847)', 'P'), ('Gossypium (taxid 3633)', 'P'),
    ('Gossypium arboreum (taxid 29729)', 'P'), ('Gossypium hirsutum (taxid 3635)', 'P'),
    ('Gossypium raimondii (taxid 29730)', 'P'), ('Helianthus annuus (taxid 4232)', 'P'),
    ('IRL clade (taxid 2233839)', 'P'), ('Lupinus angustifolius (taxid 3871)', 'P'),
    ('Medicago truncatula (taxid 3880)', 'P'), ('Phaseoleae (taxid 163735)', 'P'),
    ('Phaseolus vulgaris (taxid 3885)', 'P'), ('Rosales (taxid 3744)', 'P'), ('rosids (taxid 71275)', 'P'),
    ('Rosoideae (taxid 171638)', 'P'), ('Sesamum indicum (taxid 4182)', 'P'),
    ('Solanum pennellii (taxid 28526)', 'P'), ('Theobroma cacao (taxid 3641)', 'P'),
    ('unclassified (taxid 0)', 'U'), ('Vigna (taxid 3913)', 'P'), ('Vigna angularis (taxid 3914)', 'P'),
    ('Vigna radiata var. radiata (taxid 3916)', 'P'), ('Vitis vinifera (taxid 29760)', 'P'),
    ('Zea mays (taxid 4577)', 'P'), ('Ziziphus jujuba (taxid 326968)', 'P'),
    ('Asteraceae (taxid 4210)', 'P'), ('Arabidopsis thaliana (taxid 3702)', 'P'),
    ('Arachis (taxid 3817)', 'p'), ('Arachis duranensis (taxid 130453)', 'P'),
    ('Arachis ipaensis (taxid 130454)', 'P'), ('Asparagus officinalis (taxid 4686)', 'P'),
    ('Bacteria (taxid 2)', 'B'), ('Beta vulgaris subsp. vulgaris (taxid 3555)', 'P'),
    ('Camelina sativa (taxid 90675)', 'P'), ('Capsicum annuum (taxid 4072)', 'P'),
    ('Cercospora beticola (taxid 122368)', 'F'), ('Citrus sinensis (taxid 2711)', 'P'),
    ('Malus domestica (taxid 3750)', 'P'), ('malvids (taxid 91836)', 'P'),
    ('Manihot esculenta (taxid 3983)', 'P'), ('Mesangiospermae (taxid 1437183)', 'P'),
    ('Nicotiana attenuata (taxid 49451)', 'P'), ('Neurospora crassa OR74A (taxid 367110)', 'F'),
    ('NPAAA clade (taxid 2231382)', 'P'), ('Olea europaea var. sylvestris (taxid 158386)', 'P'),
    ('Oryza (taxid 4527)', 'P'), ('Oryza brachyantha (taxid 4533)', 'P'),
    ('Oryza sativa Japonica Group (taxid 39947)', 'P'), ('Panicum hallii (taxid 206008)', 'P'),
    ('Pentapetalae (taxid 1437201)', 'P'), ('Physcomitrella patens (taxid 3218)', 'P'),
    ('Pochonia chlamydosporia 170 (taxid 1380566)', 'F'), ('Populus trichocarpa (taxid 3694)', 'P'),
    ('Prunus (taxid 3754)', 'P'), ('Prunus mume (taxid 102107)', 'P'), ('Prunus persica (taxid 3760)', 'P'),
    ('Rosa chinensis (taxid 74649)', 'P'), ('Rosaceae (taxid 3745)', 'P'), ('Setaria italica (taxid 4555)', 'P'),
    ('Solanaceae (taxid 4070)', 'P'), ('Streptococcus (taxid 1301)', 'B'), ('Ananas comosus (taxid 4615)', 'P'),
    ('Enterobacteriaceae (taxid 543)', 'B'), ('Eukaryota (taxid 2759)', 'P'), ('Aspergillus fumigatus Af293 (taxid 330879)', 'P'),
    ('Aspergillus oryzae RIB40 (taxid 510516)', 'P'), ('Azospirillum sp. B510 (taxid 137722)', 'B'),
    ('Cucurbitaceae (taxid 3650)', 'P'),
    ])

    df = pd.read_table(kraken_tsv,sep='\t', index_col='transcript')
    new_table = df.replace(to_replace=rep_dict)
    new_table.to_csv(new_file_name)

if __name__ == '__main__':
    kraken_classification()

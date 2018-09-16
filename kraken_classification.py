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
    ('Arachis (taxid 3817)', 'P'), ('Arachis duranensis (taxid 130453)', 'P'),
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
    ('Cucurbitaceae (taxid 3650)', 'P'), ('asterids (taxid 71274)', 'P'), ('Musa acuminata subsp. malaccensis (taxid 214687)', 'P'),
    ('Sorghum bicolor (taxid 4558)', 'P'), ('Proteobacteria (taxid 1224)', 'B'), ('Thermothelomyces thermophila ATCC 42464 (taxid 573729)', 'F'),
    ('Amygdaloideae (taxid 171637)', 'P'), ('Paenibacillus beijingensis (taxid 1126833)', 'B'), ('Panicoideae (taxid 147369)', 'P'),
    ('Paenibacillus beijingensis (taxid 1126833)', 'B'), ('Poales (taxid 38820)', 'P'), ('Solanoideae (taxid 424551)', 'P'),
    ('Bacillus cohnii (taxid 33932)', 'B'), ('Botrytis cinerea B05.10 (taxid 332648)', 'F'), ('Brachypodium distachyon (taxid 15368)', 'P'),
    ('Brassicaceae (taxid 3700)', 'P'), ('Candida albicans SC5314 (taxid 237561)', 'F'), ('Colletotrichum higginsianum IMI 349063 (taxid 759273)', 'F'),
    ('Flavobacterium arcticum (taxid 1784713)', 'B'), ('Malpighiales (taxid 3646)', 'P'),('Malvaceae (taxid 3629)', 'P'),
    ('Corynebacterium timonense (taxid 441500)', 'B'), ('Arcanobacterium haemolyticum (taxid 28264)', 'B'),
    ('Bacillus coagulans (taxid 1398)', 'B'), ('Embryophyta (taxid 3193)', 'P'), ('Fusarium graminearum PH-1 (taxid 229533)', 'F'),
    ('Fusarium (taxid 5506)', 'F'), ('Fusarium fujikuroi IMI 58289 (taxid 1279085)', 'F'), ('Fusarium graminearum PH-1 (taxid 229533)', 'F'),
    ('Fusarium oxysporum f. sp. lycopersici 4287 (taxid 426428)', 'F'), ('Fusarium pseudograminearum CS3096 (taxid 1028729)', 'F'),
    ('Fusarium sambucinum species complex (taxid 569360)', 'F'), ('Fusarium venenatum (taxid 56646)', 'F'),
    ('Fusarium verticillioides 7600 (taxid 334819)', 'F'), ('Mycolicibacterium aurum (taxid 1791)', 'B'),
    ('spotted fever group (taxid 114277)', 'B'), ('Sordariales (taxid 5139)', 'F'), ('Pseudomonas savastanoi pv. phaseolicola 1448A (taxid 264730)', 'B'),
    ('Pseudomonas stutzeri (taxid 316)', 'B'), ('Rickettsia bellii (taxid 33990)', 'B'), ('Schizosaccharomyces pombe (taxid 4896)', 'F'),
    ('Staphylococcus epidermidis (taxid 1282)', 'B'), ('Staphylococcus pettenkoferi (taxid 170573)', 'B'), ('Streptococcus suis (taxid 1307)', 'B'),
    ('Tenacibaculum dicentrarchi (taxid 669041)', 'B'), ('Tenacibaculum maritimum (taxid 107401)', 'B'),
    ('Sugiyamaella lignohabitans (taxid 796027)', 'F'), ('Thielavia terrestris NRRL 8126 (taxid 578455)', 'F'),
    ('Streptomyces sp. TN58 (taxid 234612)', 'B'), ('Andropogoneae (taxid 147429)', 'P'), ('Aneurinibacillus soli (taxid 1500254)', 'B'),
    ('Acholeplasma palmae J233 (taxid 1318466)', 'B'), ('Buchnera aphidicola (Cinara pseudotaxifoliae) (taxid 655384)', 'B'),
    ('Calothrix sp. NIES-4101 (taxid 2005461)', 'B'), ('Eremothecium gossypii ATCC 10895 (taxid 284811)', 'F'),
         ])

    df = pd.read_table(kraken_tsv,sep='\t', index_col='transcript')
    new_table = df.replace(to_replace=rep_dict)
    new_table.to_csv(new_file_name, sep='\t')

if __name__ == '__main__':
    kraken_classification()

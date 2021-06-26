import os
directory = 'C:/Users/camro/PycharmProjects/BIO383_P2/data/'


def compare(this, that):
    name = that
    that = directory + that
    os.putenv("BLASTDB_LMDB_MAP_SIZE", "1000000")
    create_db = "makeblastdb -in {this_file} -input_type fasta -dbtype nucl"
    create_db = create_db.format(this_file=this)
    os.system(create_db)
    output = "blastn -query {that_file} -subject {this_file} -task blastn -max_hsps 1 -outfmt 6 >> {name_file}_results.txt"
    output = output.format(that_file=that, this_file=this, name_file=name)
    os.system(output)

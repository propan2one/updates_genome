# Check genome updates

Search in a database if your genome code protein at it several ORFs
## Table of contents

* [Description of the actual files :](#Description-of-the-actual-files)
    * [Installation](Installation)
    * [Commande line help](#Commande-line-help)
    * [Usages](#Usage)
    * [Issues](#issues)
* [History](#history)
* [License](#license)

## Installation
You must have python 3.0 installed

## Description of the actual files :
The different database add new sequence all the time, and do you know if proteins discover coded by several ORF are    You can run the script routinly

### Usage :
On your terminal 

```bash
python3 ~/PATH/check_updates.py -g ~/genomeFastaSequence.fasta -a ~/genomeGFF3Sequence.gff3 -o outputFile -n 4
```
- PATH -> is where did you put the file `check_updates.py`
- genomeFastaSequence.fasta -> is where you put the sequence of your genome in your computer, don't forget to write the path to this genome
- genomeGFF3Sequence.gff3 -> is the path and the name of the gff3 file of your genome


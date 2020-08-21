#! /usr/bin/env python

import unittest
import os, tempfile, shutil, filecmp
import genomon_sv 
import gzip

class TestParse(unittest.TestCase):

    def setUp(self):
        self.parser = genomon_sv.arg_parser.create_parser()

    def test1(self):

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_dir = tempfile.mkdtemp()

        input_file = cur_dir + "/data/bam/5929_tumor.markdup.bam"

        output_prefix = tmp_dir + "/5929_tumor"
        output_file1 = tmp_dir + "/5929_tumor.junction.clustered.bedpe.gz"
        output_file2 = tmp_dir + "/5929_tumor.junction.clustered.bedpe.gz.tbi"
        output_file3 = tmp_dir + "/5929_tumor.improper.clustered.bedpe.gz"
        output_file4 = tmp_dir + "/5929_tumor.improper.clustered.bedpe.gz.tbi"

        answer_file1 = cur_dir + "/data/parse/5929_tumor.junction.clustered.bedpe.gz"
        answer_file2 = cur_dir + "/data/parse/5929_tumor.junction.clustered.bedpe.gz.tbi"
        answer_file3 = cur_dir + "/data/parse/5929_tumor.improper.clustered.bedpe.gz"
        answer_file4 = cur_dir + "/data/parse/5929_tumor.improper.clustered.bedpe.gz.tbi"
 
        args = self.parser.parse_args(["parse", input_file, output_prefix])
        args.func(args)

        tmp_answer_file1 = tmp_dir+"/answer_5929_tumor.junction.clustered.bedpe"
        with gzip.open(answer_file1,"rt") as hin:
            with open(tmp_answer_file1,"w") as hout:
                shutil.copyfileobj(hin,hout)

        tmp_output_file1 = tmp_dir+"/output_5929_tumor.junction.clustered.bedpe"
        with gzip.open(output_file1,"rt") as hin:
            with open(tmp_output_file1,"w") as hout:
                shutil.copyfileobj(hin,hout)

        tmp_answer_file3 = tmp_dir+"/answer_5929_tumor.improper.clustered.bedpe"
        with gzip.open(answer_file3,"rt") as hin:
            with open(tmp_answer_file3,"w") as hout:
                shutil.copyfileobj(hin,hout)

        tmp_output_file3 = tmp_dir+"/output_5929_tumor.improper.clustered.bedpe"
        with gzip.open(output_file3,"rt") as hin:
            with open(tmp_output_file3,"w") as hout:
                shutil.copyfileobj(hin,hout)

        self.assertTrue(filecmp.cmp(tmp_output_file1, tmp_answer_file1, shallow=False))
        self.assertTrue(filecmp.cmp(output_file2, answer_file2, shallow=False))
        self.assertTrue(filecmp.cmp(tmp_output_file3, tmp_answer_file3, shallow=False))
        self.assertTrue(filecmp.cmp(output_file4, answer_file4, shallow=False))

        shutil.rmtree(tmp_dir)


if __name__ == "__main__":
    unittest.main()


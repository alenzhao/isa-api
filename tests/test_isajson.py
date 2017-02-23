import unittest
from isatools import isajson
import json
from tests import utils
import os


def setUpModule():
    if not os.path.exists(utils.DATA_DIR):
        raise FileNotFoundError("Could not fine test data directory in {0}. Ensure you have cloned the ISAdatasets "
                                "repository using "
                                "git clone -b tests --single-branch git@github.com:ISA-tools/ISAdatasets {0}"
                                .format(utils.DATA_DIR))


class TestIsaJson(unittest.TestCase):

    def setUp(self):
        self._json_data_dir = utils.JSON_DATA_DIR

    def test_json_load_and_dump_bii_i_1(self):
        # Load into ISA objects
        ISA = isajson.load(open(os.path.join(utils.JSON_DATA_DIR, 'BII-I-1', 'BII-I-1.json')))

        # Dump into ISA JSON from ISA objects
        ISA_J = json.loads(json.dumps(ISA, cls=isajson.ISAJSONEncoder))

        self.assertListEqual([s['filename'] for s in ISA_J['studies']], ['s_BII-S-1.txt', 's_BII-S-2.txt'])  # 2 studies in i_investigation.txt

        study_bii_s_1 = [s for s in ISA_J['studies'] if s['filename'] == 's_BII-S-1.txt'][0]

        self.assertEqual(len(study_bii_s_1['materials']['sources']), 18)  # 18 sources in s_BII-S-1.txt
        self.assertEqual(len(study_bii_s_1['materials']['samples']), 164)  # 164 study samples in s_BII-S-1.txt
        self.assertEqual(len(study_bii_s_1['processSequence']), 18)  # 18 study processes in s_BII-S-1.txt

        self.assertListEqual([a['filename'] for a in study_bii_s_1['assays']], ['a_proteome.txt', 'a_metabolome.txt', 'a_transcriptome.txt'])  # 2 assays in s_BII-S-1.txt

        assay_proteome = [a for a in study_bii_s_1['assays'] if a['filename'] == 'a_proteome.txt'][0]

        self.assertEqual(len(assay_proteome['materials']['samples']), 8)  # 8 assay samples in a_proteome.txt
        self.assertEqual(len(assay_proteome['materials']['otherMaterials']), 19)  # 19 other materials in a_proteome.txt
        self.assertEqual(len(assay_proteome['dataFiles']), 7)  # 7 data files  in a_proteome.txt
        self.assertEqual(len(assay_proteome['processSequence']), 25)  # 25 processes in in a_proteome.txt

        assay_metabolome = [a for a in study_bii_s_1['assays'] if a['filename'] == 'a_metabolome.txt'][0]

        self.assertEqual(len(assay_metabolome['materials']['samples']), 92)  # 92 assay samples in a_metabolome.txt
        self.assertEqual(len(assay_metabolome['materials']['otherMaterials']), 92)  # 92 other materials in a_metabolome.txt
        self.assertEqual(len(assay_metabolome['dataFiles']), 111)  # 111 data files  in a_metabolome.txt
        self.assertEqual(len(assay_metabolome['processSequence']), 203)  # 203 processes in in a_metabolome.txt

        assay_transcriptome = [a for a in study_bii_s_1['assays'] if a['filename'] == 'a_transcriptome.txt'][0]

        self.assertEqual(len(assay_transcriptome['materials']['samples']), 48)  # 48 assay samples in a_transcriptome.txt
        self.assertEqual(len(assay_transcriptome['materials']['otherMaterials']), 96)  # 96 other materials in a_transcriptome.txt
        self.assertEqual(len(assay_transcriptome['dataFiles']), 49)  # 49 data files  in a_transcriptome.txt
        self.assertEqual(len(assay_transcriptome['processSequence']), 193)  # 203 processes in in a_transcriptome.txt

        study_bii_s_2 = [s for s in ISA_J['studies'] if s['filename'] == 's_BII-S-2.txt'][0]

        self.assertEqual(len(study_bii_s_2['materials']['sources']), 1)  # 1 sources in s_BII-S-2.txt
        self.assertEqual(len(study_bii_s_2['materials']['samples']), 2)  # 2 study samples in s_BII-S-2.txt
        self.assertEqual(len(study_bii_s_2['processSequence']), 1)  # 1 study processes in s_BII-S-2.txt

        self.assertEqual(len(study_bii_s_2['assays']), 1)  # 1 assays in s_BII-S-2.txt
        self.assertListEqual([a['filename'] for a in study_bii_s_2['assays']], ['a_microarray.txt'])  # 1 assays in s_BII-S-2.txt
        
        assay_microarray = [a for a in study_bii_s_2['assays'] if a['filename'] == 'a_microarray.txt'][0]

        self.assertEqual(len(assay_microarray['materials']['samples']), 2)  # 2 assay samples in a_microarray.txt
        self.assertEqual(len(assay_microarray['materials']['otherMaterials']), 28)  # 28 other materials in a_microarray.txt
        self.assertEqual(len(assay_microarray['dataFiles']), 15)  # 15 data files  in a_microarray.txt
        self.assertEqual(len(assay_microarray['processSequence']), 45)  # 45 processes in in a_microarray.txt

    def test_json_load_and_dump_bii_s_3(self):
        # Load into ISA objects
        ISA = isajson.load(open(os.path.join(utils.JSON_DATA_DIR, 'BII-S-3', 'BII-S-3.json')))

        # Dump into ISA JSON from ISA objects
        ISA_J = json.loads(json.dumps(ISA, cls=isajson.ISAJSONEncoder))
    
        self.assertListEqual([s['filename'] for s in ISA_J['studies']], ['s_BII-S-3.txt'])  # 1 studies in i_gilbert.txt
    
        study_bii_s_3 = [s for s in ISA_J['studies'] if s['filename'] == 's_BII-S-3.txt'][0]
    
        self.assertEqual(len(study_bii_s_3['materials']['sources']), 4)  # 4 sources in s_BII-S-1.txt
        self.assertEqual(len(study_bii_s_3['materials']['samples']), 4)  # 4 study samples in s_BII-S-1.txt
        self.assertEqual(len(study_bii_s_3['processSequence']), 4)  # 4 study processes in s_BII-S-1.txt

        self.assertListEqual([a['filename'] for a in study_bii_s_3['assays']], ['a_gilbert-assay-Gx.txt', 'a_gilbert-assay-Tx.txt'])  # 2 assays in s_BII-S-1.txt
    
        assay_gx = [a for a in study_bii_s_3['assays'] if a['filename'] == 'a_gilbert-assay-Gx.txt'][0]
    
        self.assertEqual(len(assay_gx['materials']['samples']), 4)  # 4 assay samples in a_gilbert-assay-Gx.txt
        self.assertEqual(len(assay_gx['materials']['otherMaterials']), 4)  # 4 other materials in a_gilbert-assay-Gx.txt
        self.assertEqual(len(assay_gx['dataFiles']), 6)  # 6 data files  in a_gilbert-assay-Gx.txt
        self.assertEqual(len(assay_gx['processSequence']), 18)  # 18 processes in in a_gilbert-assay-Gx.txt

        assay_tx = [a for a in study_bii_s_3['assays'] if a['filename'] == 'a_gilbert-assay-Tx.txt'][0]
    
        self.assertEqual(len(assay_tx['materials']['samples']), 4)  # 4 assay samples in a_gilbert-assay-Tx.txt
        self.assertEqual(len(assay_tx['materials']['otherMaterials']), 4)  # 4 other materials in a_gilbert-assay-Tx.txt
        self.assertEqual(len(assay_tx['dataFiles']), 24)  # 24 data files  in a_gilbert-assay-Tx.txt
        self.assertEqual(len(assay_tx['processSequence']), 36)  # 36 processes in in a_gilbert-assay-Tx.txt

    def test_json_load_and_dump_bii_s_7(self):
        # Load into ISA objects
        ISA = isajson.load(open(os.path.join(utils.JSON_DATA_DIR, 'BII-S-7', 'BII-S-7.json')))

        # Dump into ISA JSON from ISA objects
        ISA_J = json.loads(json.dumps(ISA, cls=isajson.ISAJSONEncoder))
    
        self.assertListEqual([s['filename'] for s in ISA_J['studies']], ['s_BII-S-7.txt'])  # 1 studies in i_gilbert.txt
    
        study_bii_s_7 = [s for s in ISA_J['studies'] if s['filename'] == 's_BII-S-7.txt'][0]
    
        self.assertEqual(len(study_bii_s_7['materials']['sources']), 29)  # 29 sources in s_BII-S-1.txt
        self.assertEqual(len(study_bii_s_7['materials']['samples']), 29)  # 29 study samples in s_BII-S-1.txt
        self.assertEqual(len(study_bii_s_7['processSequence']), 29)  # 29 study processes in s_BII-S-1.txt
    
        self.assertListEqual([a['filename'] for a in study_bii_s_7['assays']], ['a_matteo-assay-Gx.txt'])  # 1 assays in s_BII-S-1.txt
    
        assay_gx = [a for a in study_bii_s_7['assays'] if a['filename'] == 'a_matteo-assay-Gx.txt'][0]
    
        self.assertEqual(len(assay_gx['materials']['samples']), 29)  # 29 assay samples in a_matteo-assay-Gx.txt
        self.assertEqual(len(assay_gx['materials']['otherMaterials']), 29)  # 29 other materials in a_matteo-assay-Gx.txt
        self.assertEqual(len(assay_gx['dataFiles']), 29)  # 29 data files  in a_matteo-assay-Gx.txt
        self.assertEqual(len(assay_gx['processSequence']), 116)  # 116 processes in in a_matteo-assay-Gx.txt


class UnitTestISAJSONEncoder(unittest.TestCase):

    def setUp(self):
        self.encoder = isajson.ISAJSONEncoder()

    def test_remove_nulls(self):
        d = {
            "a": None,
            "b": "b"
        }
        expected_result = {
            "a": "",
            "b": "b"
        }
        result = self.encoder.nulls_to_str(d=d)
        self.assertEqual(result, expected_result)

    # def test_nulls_to_str(self):
    #     self.fail("test not implemented")

    def test_list_of(self):
        class SimpleObject:
            def __init__(self, a, b):
                self.a = a
                self.b = b

        def get_simple_object(o):
            return {
                "a": o.a,
                "b": o.b
            }
        o = SimpleObject(a="a", b="b")
        result = self.encoder.list_of(get_simple_object, [o])
        expected_result = [{
            "a": "a",
            "b": "b"
        }]
        self.assertEqual(result, expected_result)

    def test_get_comment(self):
        from isatools.model.v1 import Comment
        o = Comment(name="k")
        o.value = "v"
        result = self.encoder.get_comment(o)
        expected_result = {
            "name": "k",
            "value": "v"
        }
        self.assertEqual(result, expected_result)

    def test_get_ontology_source(self):
        from isatools.model.v1 import OntologySource
        o = OntologySource(name="k")
        o.description = "d"
        o.file = "f"
        o.version = "v"
        result = self.encoder.get_ontology_source(o)
        expected_result = {
                "name": "k",
                "description": "d",
                "file": "f",
                "version": "v"
            }
        self.assertEqual(result, expected_result)

    def test_get_ontology_annotation(self):
        from isatools.model.v1 import OntologyAnnotation
        o = OntologyAnnotation()
        o.term = "term"
        o.term_accession = "accession"
        result = self.encoder.get_ontology_annotation(o)
        expected_result = {
                "@id": "#" + str(id(o)),
                "annotationValue": "term",
                "termAccession": "accession",
                "termSource": ""
            }
        self.assertEqual(result, expected_result)

    def test_get_ontology_annotation_with_ontology_source(self):
        from isatools.model.v1 import OntologyAnnotation, OntologySource
        o = OntologyAnnotation()
        o.term = "term"
        o.term_accession = "accession"
        o.term_source = OntologySource(name="k")
        result = self.encoder.get_ontology_annotation(o)
        expected_result = {
            "@id": "#" + str(id(o)),
            "annotationValue": "term",
            "termAccession": "accession",
            "termSource": "k"
        }
        self.assertEqual(result, expected_result)

    def test_get_person(self):
        from isatools.model.v1 import Person
        o = Person()
        o.first_name = "first"
        o.last_name = "last"
        o.mid_initials = "mid"
        o.phone = "555-1865"
        o.fax = "555-1866"
        o.address = "address"
        o.affiliation = "affiliation"
        o.email = "first@affiliation"
        result = self.encoder.get_person(o)
        expected_result = {
            "phone": "555-1865", 
            "email": "first@affiliation",
            "roles": [], 
            "address": "address", 
            "comments": [], 
            "lastName": "last", 
            "affiliation": "affiliation", 
            "firstName": "first", 
            "fax": "555-1866", 
            "midInitials": "mid"
        }
        self.assertEqual(result, expected_result)

    def test_get_publication(self):
        from isatools.model.v1 import Publication, OntologyAnnotation
        o = Publication()
        o.pubmed_id = "000001"
        o.doi = "doi"
        o.author_list = "a. author, b. author"
        o.title = "title"
        o.status = OntologyAnnotation(term="published")
        result = self.encoder.get_publication(o)
        expected_result = {
            "doi": "doi", 
            "authorList": "a. author, b. author", 
            "pubMedID": "000001", 
            "status": {
                "termAccession": "", 
                "annotationValue": "published", 
                "@id": "#" + str(id(o.status)),
                "termSource": ""
            }, 
            "title": "title"
        }

        self.assertEqual(result, expected_result)

    # def test_get_protocol(self):
    #     self.fail("test not implemented")
    #
    # def test_get_source(self):
    #     self.fail("test not implemented")
    #
    # def test_get_characteristic(self):
    #     self.fail("test not implemented")
    #
    # def test_get_value(self):
    #     self.fail("test not implemented")
    #
    # def test_get_characteristic_category(self):
    #     self.fail("test not implemented")
    #
    # def test_get_sample(self):
    #     self.fail("test not implemented")
    #
    # def test_get_factor(self):
    #     self.fail("test not implemented")
    #
    # def test_get_other_material(self):
    #     self.fail("test not implemented")
    #
    # def test_get_process(self):
    #     self.fail("test not implemented")
    #
    # def test_get_parameter_value(self):
    #     self.fail("test not implemented")
    #
    # def test_get_study(self):
    #     self.fail("test not implemented")
    #
    # def test_get_assay(self):
    #     self.fail("test not implemented")
    #
    # def test_get_data_file(self):
    #     self.fail("test not implemented")

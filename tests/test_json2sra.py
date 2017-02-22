from unittest import TestCase
import os
import shutil
from isatools.convert import json2sra
from lxml import etree
from tests import utils
import tempfile


def setUpModule():
    if not os.path.exists(utils.DATA_DIR):
        raise FileNotFoundError("Could not fine test data directory in {0}. Ensure you have cloned the ISAdatasets "
                                "repository using "
                                "git clone -b tests --single-branch git@github.com:ISA-tools/ISAdatasets {0}"
                                .format(utils.DATA_DIR))


class TestJsonToSra(TestCase):

    def setUp(self):
        self._json_data_dir = utils.JSON_DATA_DIR
        self._unit_json_data_dir = utils.UNIT_JSON_DATA_DIR
        self._configs_json_data_dir = utils.JSON_DEFAULT_CONFIGS_DATA_DIR
        self._sra_data_dir = utils.SRA_DATA_DIR
        self._sra_configs_dir = utils.DEFAULT2015_XML_CONFIGS_DATA_DIR
        self._tmp_dir = tempfile.mkdtemp()

        self._expected_submission_xml_biis3 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-3', 'submission.xml'), 'rb').read())
        self._expected_project_set_xml_biis3 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-3', 'project_set.xml'), 'rb').read())
        self._expected_sample_set_xml_biis3 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-3', 'sample_set.xml'), 'rb').read())
        self._expected_experiment_set_xml_biis3 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-3', 'experiment_set.xml'), 'rb').read())
        self._expected_run_set_xml_biis3 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-3', 'run_set.xml'), 'rb').read())

        self._expected_submission_xml_biis7 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-7', 'submission.xml'), 'rb').read())
        self._expected_project_set_xml_biis7 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-7', 'project_set.xml'), 'rb').read())
        self._expected_sample_set_xml_biis7 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-7', 'sample_set.xml'), 'rb').read())
        self._expected_experiment_set_xml_biis7 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-7', 'experiment_set.xml'), 'rb').read())
        self._expected_run_set_xml_biis7 = etree.fromstring(open(os.path.join(self._sra_data_dir, 'BII-S-7', 'run_set.xml'), 'rb').read())

        self._sra_default_config = {
            "sra_broker": "",
            "sra_center": "OXFORD",
            "sra_project": "OXFORD",
            "sra_lab": "Oxford e-Research Centre",
            "sra_broker_inform_on_status": "proccaserra@gmail.com",
            "sra_broker_inform_on_error": "proccaserra@gmail.com",
            "sra_broker_contact_name": "PRS"
        }

    def tearDown(self):
        shutil.rmtree(self._tmp_dir)

    def test_sra_dump_file_set(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-3', 'BII-S-3.json')), self._tmp_dir, validate_first=False)
        # SRA should always produce experiment_set.xml, run_set.xml, sample_set.xml study.xml and submission.xml
        expected_sra_path = os.path.join(self._tmp_dir)
        expected_file_set = {'experiment_set.xml', 'run_set.xml', 'sample_set.xml', 'project_set.xml', 'submission.xml'}
        if os.path.exists(expected_sra_path):
            actual_file_set = set(os.listdir(expected_sra_path))
            extra_files_found = actual_file_set - expected_file_set
            if len(extra_files_found) > 0:
                self.fail("Unexpected file found in SRA output: " + str(extra_files_found))
            expected_files_missing = expected_file_set - actual_file_set
            if len(expected_files_missing) > 0:
                self.fail("Unexpected file found in SRA output: " + str(expected_files_missing))
        
    def test_sra_dump_submission_xml_biis3(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-3', 'BII-S-3.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        submission_xml = open(os.path.join(self._tmp_dir, 'submission.xml'), 'rb').read()
        actual_submission_xml_biis3 = etree.fromstring(submission_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_submission_xml_biis3, actual_submission_xml_biis3))

    def test_sra_dump_study_xml_biis3(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-3', 'BII-S-3.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        project_set_xml = open(os.path.join(self._tmp_dir, 'project_set.xml'), 'rb').read()
        actual_project_set_xml_biis3 = etree.fromstring(project_set_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_project_set_xml_biis3, actual_project_set_xml_biis3))

    def test_sra_dump_sample_set_xml_biis3(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-3', 'BII-S-3.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        sample_set_xml = open(os.path.join(self._tmp_dir, 'sample_set.xml'), 'rb').read()
        actual_sample_set_xml_biis3 = etree.fromstring(sample_set_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_sample_set_xml_biis3, actual_sample_set_xml_biis3))

    def test_sra_dump_experiment_set_xml_biis3(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-3', 'BII-S-3.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        experiment_set_xml = open(os.path.join(self._tmp_dir, 'experiment_set.xml'), 'rb').read()
        actual_experiment_set_xml_biis3 = etree.fromstring(experiment_set_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_experiment_set_xml_biis3, actual_experiment_set_xml_biis3))

    def test_sra_dump_run_set_xml_biis3(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-3', 'BII-S-3.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        run_set_xml = open(os.path.join(self._tmp_dir, 'run_set.xml'), 'rb').read()
        actual_run_set_xml_biis3 = etree.fromstring(run_set_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_run_set_xml_biis3, actual_run_set_xml_biis3))

    def test_sra_dump_submission_xml_biis7(self):
        sra_settings = self._sra_default_config
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-7', 'BII-S-7.json')), self._tmp_dir, sra_settings=sra_settings, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        submission_xml = open(os.path.join(self._tmp_dir, 'submission.xml'), 'rb').read()
        actual_submission_xml_biis7 = etree.fromstring(submission_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_submission_xml_biis7, actual_submission_xml_biis7))

    def test_sra_dump_project_set_xml_biis7(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-7', 'BII-S-7.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        study_xml = open(os.path.join(self._tmp_dir, 'project_set.xml'), 'rb').read()
        actual_project_set_xml_biis7 = etree.fromstring(study_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_project_set_xml_biis7, actual_project_set_xml_biis7))

    def test_sra_dump_sample_set_xml_biis7(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-7', 'BII-S-7.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        sample_set_xml = open(os.path.join(self._tmp_dir, 'sample_set.xml'), 'rb').read()
        actual_sample_set_xml_biis7 = etree.fromstring(sample_set_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_sample_set_xml_biis7, actual_sample_set_xml_biis7))

    def test_sra_dump_experiment_set_xml_biis7(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-7', 'BII-S-7.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        experiment_set_xml = open(os.path.join(self._tmp_dir, 'experiment_set.xml'), 'rb').read()
        actual_experiment_set_xml_biis7 = etree.fromstring(experiment_set_xml)
        self.assertTrue(utils.assert_xml_equal(self._expected_experiment_set_xml_biis7, actual_experiment_set_xml_biis7))

    def test_sra_dump_run_set_xml_biis7(self):
        json2sra.convert(open(os.path.join(self._json_data_dir, 'BII-S-7', 'BII-S-7.json')), self._tmp_dir, validate_first=False)
        # Now try load the SRA output in test and compare against the expected output in test data directory
        run_set_xml = open(os.path.join(self._tmp_dir, 'run_set.xml'), 'rb').read()
        actual_run_set_xml_biis7 = etree.fromstring(run_set_xml)
        self.assertTrue( utils.assert_xml_equal(self._expected_run_set_xml_biis7, actual_run_set_xml_biis7))

#!/usr/bin/env python

"""test_reasoner.py: Test phyloreferences against reasoner."""

import os
import fnmatch
import rdflib
import subprocess
import xml.sax
from libreasoner import validateWithReasoner

def test_execute():
    """ Validate every tree against its phyloreferences; 
    the phyloreference files contains pairs of classes
    that must contain the same set of individuals for
    the validation to pass.
    """

    examples_dir = "examples/trees";

    count = 0
    for file_omn in os.listdir(examples_dir):
        if fnmatch.fnmatch(file_omn, '*.omn'):
            path_omn = examples_dir + "/" + file_omn
            path_owl = examples_dir + "/" + file_omn[:-13] + "owl"
            if os.path.isfile(path_owl):
                print "Validating " + path_owl + " against phyloreferences in " + path_omn
                validateWithReasoner(path_owl, path_omn)
                count += 1

    assert count > 0

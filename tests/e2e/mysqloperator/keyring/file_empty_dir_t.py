# Copyright (c) 2022, Oracle and/or its affiliates.
#
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl/
#

import unittest
from setup.config import g_ts_cfg
from e2e.mysqloperator.keyring.keyring_base import KeyRingBase


# test the key ring file with EmptyDir storage
@unittest.skipIf(g_ts_cfg.enterprise_skip, "Enterprise test cases are skipped")
class KeyRingFileEmptyDir(KeyRingBase):

    def test_1_run(self):
        keyring_spec = f"""
  keyring:
    file:
      fileName: "/tmp/component_keyring_file"
      readOnly: false
      storage:
        emptyDir: {{}}
"""

        self.create_cluster(keyring_spec)
        self.create_keyring()
        self.encrypt_tables()
        self.check_variables()

    def test_9_destroy(self):
        self.destroy_cluster()

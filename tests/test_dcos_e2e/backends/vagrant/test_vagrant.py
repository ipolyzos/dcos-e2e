"""
Tests for the Vagrant backend.
"""

import subprocess
import uuid
from pathlib import Path
from typing import Set

from dcos_e2e.backends import Vagrant
from dcos_e2e.cluster import Cluster


# We skip these tests because VirtualBox is not available on Travis CI.
class TestRunIntegrationTest:  # pragma: nocover
    """
    Tests for functionality specific to the Vagrant backend.
    """

    def test_run_integration_test(
        self,
        oss_artifact: Path,
    ) -> None:
        """
        It is possible to run DC/OS integration tests on Vagrant.
        This test module only requires a single master node.
        """
        with Cluster(
            cluster_backend=Vagrant(),
            masters=1,
            agents=1,
            public_agents=1,
        ) as cluster:
            cluster.install_dcos_from_path(
                build_artifact=oss_artifact,
                dcos_config=cluster.base_config,
                log_output_live=True,
            )

            cluster.wait_for_dcos_oss()

            # No error is raised with a successful command.
            cluster.run_integration_tests(
                pytest_command=['pytest', '-vvv', '-s', '-x', 'test_units.py'],
                log_output_live=True,
            )

# We skip these tests because VirtualBox is not available on Travis CI.
class TestVMDescription:  # pragma: nocover
    """
    XXX
    """

    def _vm_names(self) -> Set[str]:
        """
        XXX
        """
        args = ['VboxManage', 'list', 'vms']
        list_result = subprocess.run(
            args=args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        list_stdout = list_result.stdout
        return set(list_stdout.decode().strip().split('\n'))


    def test_default(self):
        """
        XXX
        """
        with Cluster(
            cluster_backend=Vagrant(),
            masters=1,
            agents=0,
            public_agents=0,
        ) as master:
            new_vm_name = get_vm_from_node

    def test_custom(self):
        """
        XXX
        """
        return
        suffix = uuid.uuid4().hex
        with Cluster(
            cluster_backend=Vagrant(vm_name_suffix=suffix),
            masters=1,
            agents=0,
            public_agents=0,
        ):
            pass

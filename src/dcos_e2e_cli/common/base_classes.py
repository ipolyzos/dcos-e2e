"""
Abstract base classes for making CLIs.
"""

import abc
from pathlib import Path
from typing import Any, Dict, Iterable, Set, Tuple, Type

from dcos_e2e.node import Node, Output


class ClusterRepresentation(abc.ABC):
    """
    A representation of a cluster.
    """

    @abc.abstractmethod
    def to_node(self, node_representation: Any) -> None:
        """
        Return the ``Node`` that is represented.
        """

    @abc.abstractmethod
    def to_dict(self, node_representation: Any) -> Dict[str, str]:
        """
        Return information to be shown to users which is unique to this node.
        """

    @property
    @abc.abstractmethod
    def ssh_default_user(self) -> str:
        """
        A user which can be used to SSH to any node using
        ``self.ssh_key_path``.
        """

    @property
    @abc.abstractmethod
    def ssh_key_path(self) -> str:
        """
        A key which can be used to SSH to any node.
        """

    @property
    @abc.abstractmethod
    def masters(self) -> Set[Any]:
        """
        All DC/OS master node representations.
        """

    @property
    @abc.abstractmethod
    def agents(self) -> Set[Any]:
        """
        All DC/OS agent node representations.
        """

    @property
    @abc.abstractmethod
    def public_agents(self) -> Set[Any]:
        """
        All DC/OS agent node representations.
        """

    @abc.abstractmethod
    def destroy(self) -> None:
        """
        Destroy all nodes in the cluster.
        """

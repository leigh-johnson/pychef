import pytest
import json
import os
from unittest import mock
from chef.api import autoconfigure_v2
from chef.tests import TEST_ROOT


@pytest.fixture
def mock_client_key():
    return os.path.join(TEST_ROOT, "client.pem")


@pytest.fixture
def mock_client_config(mock_client_key):
    """
    Example load_config_json output
    """

    return json.dumps(
        {
            "log_location": "",
            "config_file": "/etc/chef/client.rb",
            "log_level": "warn",
            "node_name": "example-hostname",
            "client_key": "{client_key}".format(client_key=mock_client_key),
            "chef_server_url": "https://chef.example.com/organizations/example/",
            "syntax_check_cache_path": "",
            "cookbook_path": [
                "/home/username/src/example.com/chef/cookbooks",
                "/home/username/src/example.com/chef/site-cookbooks",
            ],
            "color": True,
            "script_path": [
                "/home/username/.chef/scripts",
                "/home/username/.chef/scripts",
            ],
            "file_backup_path": "/var/lib/chef",
            "file_cache_path": "/var/cache/chef",
            "pid_file": "/var/run/chef/client.pid",
            "ssl_verify_mode": "verify_peer",
            "automatic_attribute_blacklist": [
                "filesystem",
                "filesystem2",
                "counters",
                "sysconf",
                "etc/group",
                "pci",
                "block_device",
                "sessions",
            ],
            "rubygems_url": "https://rubygems.org/",
            "force_logger": False,
            "force_formatter": False,
            "profile_ruby": False,
        }
    )


@mock.patch("subprocess.check_call")
def test_autoconfigure_v2_ssl_verify_peer(mock_proc, mock_client_config):
    mock_proc.return_value = mock_client_config
    client = autoconfigure_v2()

    assert client.url == "https://chef.example.com/organizations/example"
    assert client.ssl_verify == True
    assert client.client == "example-hostname"


@mock.patch("subprocess.check_call")
def test_autoconfigure_v2_malformed(mock_proc):
    mock_proc.return_value = "No such file or directory"

    with pytest.raises(ValueError):
        autoconfigure_v2()

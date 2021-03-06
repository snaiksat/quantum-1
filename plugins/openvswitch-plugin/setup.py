try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys

Name = 'quantum-openvswitch-plugin'
ProjecUrl = ""
Version = '0.1'
License = 'Apache License 2.0'
# Change as required
Author = 'Open vSwitch Team'
AuthorEmail = 'discuss@openvswitch.org'
Maintainer = ''
Summary = 'OpenVSwitch plugin for Quantum'
ShortDescription = Summary
Description = Summary

requires = [
    'quantum-common',
    'quantum-server',
]

EagerResources = [
    'quantum',
]

ProjectScripts = [
]

PackageData = {
}

# If we're installing server-wide, use an aboslute path for config
# if not, use a relative path
config_path = '/etc/quantum/plugins/openvswitch'
relative_locations = ['--user', '--virtualenv', '--venv']
if [x for x in relative_locations if x in sys.argv]:
    config_path = 'etc/quantum/plugins/openvswitch'

DataFiles = [
    (config_path,
    ['etc/ovs_quantum_plugin.ini'])
]

setup(
    name=Name,
    version=Version,
    author=Author,
    author_email=AuthorEmail,
    description=ShortDescription,
    long_description=Description,
    license=License,
    scripts=ProjectScripts,
    install_requires=requires,
    include_package_data=True,
    packages=find_packages('lib'),
    package_data=PackageData,
    data_files=DataFiles,
    package_dir={'': 'lib'},
    eager_resources=EagerResources,
    namespace_packages=['quantum'],
)

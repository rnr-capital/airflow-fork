#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE
# OVERWRITTEN WHEN PREPARING PACKAGES.
#
# IF YOU WANT TO MODIFY IT, YOU SHOULD MODIFY THE TEMPLATE
# `SETUP_TEMPLATE.py.jinja2` IN the `dev/provider_packages` DIRECTORY

"""Setup.py for the apache-airflow-providers-amazon package."""

from setuptools import find_namespace_packages, setup

version = "8.0.1.dev0"


def do_setup():
    """Perform the package apache-airflow-providers-amazon setup."""
    setup(
        version=version,
        extras_require={
            "apache.hive": ["apache-airflow-providers-apache-hive"],
            "cncf.kubernetes": ["apache-airflow-providers-cncf-kubernetes"],
            "common.sql": ["apache-airflow-providers-common-sql"],
            "exasol": ["apache-airflow-providers-exasol"],
            "ftp": ["apache-airflow-providers-ftp"],
            "google": ["apache-airflow-providers-google"],
            "imap": ["apache-airflow-providers-imap"],
            "mongo": ["apache-airflow-providers-mongo"],
            "salesforce": ["apache-airflow-providers-salesforce"],
            "ssh": ["apache-airflow-providers-ssh"],
            "pandas": ["pandas>=0.17.1"],
            "aiobotocore": ["aiobotocore[boto3]>=2.2.0"],
        },
        packages=find_namespace_packages(
            include=[
                "airflow.providers.amazon",
                "airflow.providers.amazon.*",
                "airflow.providers.amazon_vendor",
                "airflow.providers.amazon_vendor.*",
            ],
        ),
    )


if __name__ == "__main__":
    do_setup()
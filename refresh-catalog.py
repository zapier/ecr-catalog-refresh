#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import boto3
import json
import time
import logging


def get_current_repositories(registry_id):
    client = boto3.client('ecr')
    resp = client.describe_repositories(
        registryId=registry_id,
    )

    catalog_file = {
      'repositories': [],
    }
    for repository in resp['repositories']:
        catalog_file['repositories'].append(repository['repositoryName'])
    return catalog_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a docker registry catalog file from ECR.')
    parser.add_argument("--catalog-file", help="Location to write catalog file to.", required=True)
    parser.add_argument("--registry-id", help="registry to read from.", required=True)

    args = parser.parse_args()

    while True:
        try:
            with open(args.catalog_file, 'w') as outfile:
                json.dump(get_current_repositories(args.registry_id), outfile)
                print('Catalog file {} written!'.format(args.catalog_file))
            time.sleep(1800)
        except Exception as e:
            logging.exception("Exception occurred, retrying in 120 seconds")
            time.sleep(120)  # shorter sleep if there is a failure

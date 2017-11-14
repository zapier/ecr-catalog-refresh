#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import boto3
import json
import time


def get_current_repositories():
    client = boto3.client('ecr')
    resp = client.describe_repositories()

    catalog_file = {
      'repositories': [],
    }
    for repository in resp['repositories']:
        catalog_file['repositories'].append(repository['repositoryName'])
    return catalog_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a docker registry catalog file from ECR.')
    parser.add_argument("--catalog-file", help="Location to write catalog file to.", required=True)

    args = parser.parse_args()

    while True:
        with open(args.catalog_file, 'w') as outfile:
            json.dump(get_current_repositories(), outfile)
            print('Catalog file {} written!'.format(args.catalog_file))
        time.sleep(1800)


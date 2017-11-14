# ecr-catalog-refresh
Really simple script to generate a catalog file from ECR to take the place of the missing `/v2/_catalog` endpoint so that ECR can integrate nicely with other applications.

## Building It
Docker build -t ecr-catalog-refresh .

## Running It
You'll likely want to run this with the `--catalog-file` parameter writing to a mounted volume that other containers can read from. The default is  `/opt/catalog/repos.json`.


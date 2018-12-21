#!/usr/bin/env python
import os
import sys
import shutil
import yaml
import subprocess

MANIFEST = "manifest.yml"


def delete_resources_for_disabled_features():
    with open(MANIFEST) as manifest_file:
        manifest = yaml.load(manifest_file)
        for feature in manifest["features"]:
            if not feature["enabled"]:
                for resource in feature["resources"]:
                    delete_resource(resource)


def delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
    elif os.path.isdir(resource):
        shutil.rmtree(resource)


if __name__ == "__main__":
    ret = subprocess.call(["cookie_scripts/initialize_project.sh"])
    if ret != 0:
        sys.exit(ret)

    delete_resources_for_disabled_features()
    delete_resource('cookie_scripts')
    delete_resource('install_python_requirements.sh')
    delete_resource(MANIFEST)

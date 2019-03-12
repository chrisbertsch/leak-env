#!/usr/bin/python -tt

import os

DOCUMENTATION = '''
---
module: environ
version_added: 2.7
short_description: get environment variables
description:
  - Reads Environment Variables
options: {}
author: "Chris Bertsch (@chrisbertsch)"
'''

EXAMPLES = '''
# Retrieve Environment Variables
 - name: Gather Environment Variables
   environ:
'''

import os
from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    facts = {}

    facts['environ'] = dict(os.environ)

    module.exit_json(ansible_facts=facts)


if __name__ == '__main__':
    main()

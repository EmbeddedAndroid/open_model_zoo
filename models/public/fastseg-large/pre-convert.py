#!/usr/bin/env python3

# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import subprocess
import sys

from pathlib import Path

BACKBONE = 'MobileV3Large'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', type=Path)
    parser.add_argument('output_dir', type=Path)
    args = parser.parse_args()

    subprocess.run([sys.executable, '--',
        str(args.input_dir / 'model/onnx_export.py'),
        '{}'.format(args.output_dir / 'fastseg-large.onnx'),
        '--checkpoint={}'.format(args.output_dir / 'mobilev3large-lraspp-f128-9cbabfde.pt'),
        '--model={}'.format(BACKBONE),
        '--num_filters={}'.format('128')
    ], check=True)

if __name__ == '__main__':
    main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import logging
import re
import subprocess
from csv import DictWriter

CONFIGS = [
    'DEFAULT',
    'HARDENED_USERCOPY',
    'MEMCG',
    'PAGE_TABLE_ISOLATION',
    'RETPOLINE',
    'SLAB_FREELIST_RANDOM',
    'TRANSPARENT_HUGEPAGE_ALWAYS',
    'USERFAULTFD',
]
PASSES = 5
VERSION = '5.5.2'

pattern = re.compile(r'(\w+) ?(.*) (\d+)us')


def load_current():
    with open('current', 'r') as f:
        return f.read()


def set_current(current):
    with open('current', 'w') as f:
        return f.write(current)


def run_bench_script():
    result = subprocess.run(['bash', 'run_bench.sh'], capture_output=True)

    return result.stdout.decode('UTF-8')


def parse_results(output):
    results = {}
    for line in output.split('\n'):
        matches = pattern.match(line.strip())
        if matches is None:
            continue

        results[matches.group(1)] = {
            'params': matches.group(2),
            'time': int(matches.group(3)),
        }

    return results


def accumulate(accumulated_results, results):
    for key, value in results.items():
        if key in accumulated_results:
            accumulated_results[key]['time'] += value['time']
        else:
            accumulated_results[key] = value.copy()


def average(accumulated_results):
    results = []
    for key, value in accumulated_results.items():
        results.append({
            'name': key,
            'params': value['params'],
            'time': int(value['time'] / PASSES),
        })

    return results


def save_results(current, results):
    logging.info(f'saving results: {results}')
    with open(f'output/{current}.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'params', 'time']
        writer = DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(results)


def prepare_next(current):
    current_index = CONFIGS.index(current)
    if current_index == len(CONFIGS) - 1:
        return False

    next = CONFIGS[current_index + 1]
    logging.info(f'Setting {next} as next config')
    package = f'/home/pavle/compiled/linux-{VERSION}-{next}.pkg.tar.zst'
    set_current(next)
    subprocess.run(['sudo', 'pacman', '-U', '--noconfirm', package])
    subprocess.run(['sudo', 'efibootmgr', '-n', '0007'])

    return True


def run_benchmark(current):
    accumulated_results = {}
    for i in range(PASSES):
        logging.info(f'pass {i+1} of {PASSES}')
        output = run_bench_script()
        logging.debug(f'raw benchmark output: {output}')
        results = parse_results(output)
        accumulate(accumulated_results, results)
        logging.debug(f'pass results: {results}')
        logging.debug(f'accumulated results: {accumulated_results}')

    final_results = average(accumulated_results)
    logging.debug(f'Final results: {final_results}')
    save_results(current, final_results)


def main():
    current = load_current()
    logging.info(f'Current config: {current}')
    run_benchmark(current)
    if prepare_next(current):
        subprocess.run(['sudo', 'reboot'])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

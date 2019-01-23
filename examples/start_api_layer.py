from pprint import pprint

from pybright.cli import bright


def start_not_running_tasks_of_api_layer():
    prefix = "MASA"
    expected_suffixes = {
        "ca31": ['GW1', 'DS1', 'AC1'],
        "ca32": ['GW2', 'DS2']
    }

    active_jobs = []
    for job in bright(f"zos-jobs list jobs --prefix {prefix}* --owner MASSERV"):
        if job['status'] == 'ACTIVE':
            active_jobs.append(job['jobname'])

    print("Active jobs:")
    print(", ".join(active_jobs))

    for system, expected_suffixes in expected_suffixes.items():
        for suffix in expected_suffixes:
            jobname = prefix + suffix
            if jobname not in active_jobs:
                print(f"Job {jobname} is not active on system {system}. Starting...")
                bright(f'zos-console issue command --sysplex-system {system} "S {jobname}"')
    
    
if __name__ == '__main__':
    start_not_running_tasks_of_api_layer()
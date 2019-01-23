from pprint import pprint

from pybright.cli import bright


def list_my_jobs():
    jobs = bright("zos-jobs list jobs")
    pprint(jobs)
    for job in jobs:
        print(f"{job['jobname']} {job['jobid']} {job['retcode']}")


def list_my_failed_jobs():
    for job in bright("zos-jobs list jobs"):
        if job['retcode'] not in ['CC 0000', None]:
            print(f"{job['jobname']} {job['jobid']} {job['retcode']}")


def list_sysout_of_api_gateway_failed_started_tasks():
    for job in bright("zos-jobs list jobs --prefix MAS* --owner MASSERV"):
        if job['retcode'] not in ['CC 0000', None]:
            print(f"{job['jobname']} {job['jobid']} {job['retcode']}")
            for spool_file in bright(f"zos-jobs list spool-files-by-jobid {job['jobid']}"):
                if spool_file['ddname'] == 'SYSOUT':
                    sysout = bright(f"zos-jobs view spool-file-by-id {job['jobid']} {spool_file['id']}")
                    print(sysout)


def main():
    list_my_jobs()
    list_my_failed_jobs()
    list_sysout_of_api_gateway_failed_started_tasks()


if __name__ == '__main__':
    main()

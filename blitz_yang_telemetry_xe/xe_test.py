########################################################
# To run the job:
# pyats run job  path/to/my/job/file/myjob.py \
#        -testbed_file path/to/my/yaml/file/myyaml.yaml
########################################################
from genie.harness.main import gRun


def main():
    trigger_uids = [
        'native_oper_interface_statistics_get',
        'native_netconf_cpu_statistics_subscribe',
    ]

    gRun(trigger_uids=trigger_uids,
         trigger_datafile="xe_trigger.yaml",
         mapping_datafile="xe_mapping.yaml",
         subsection_datafile="xe_subsection.yaml")


if __name__ == '__main__':
    main()
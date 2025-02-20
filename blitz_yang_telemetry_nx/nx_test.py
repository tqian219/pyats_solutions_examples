########################################################
# To run the job:
# pyats run job  path/to/my/job/file/myjob.py \
#        -testbed_file path/to/my/yaml/file/myyaml.yaml
########################################################
from genie.harness.main import gRun


def main():
    trigger_uids = [
        #'nexus_openconfig_gnmi_fan_statistics_subscribe',
        'nexus_netconf_ospf_state_get',
    ]

    gRun(trigger_uids=trigger_uids,
         trigger_datafile="nx_trigger.yaml",
         mapping_datafile="nx_mapping.yaml",
         subsection_datafile="nx_subsection.yaml")


if __name__ == '__main__':
    main()

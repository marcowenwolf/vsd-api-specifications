{
    "attributes": {
        "DSCP": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "DSCP match condition to be set in the rule. It is either * or from 0-63",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "ICMPCode": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The ICMP Code when protocol selected is ICMP.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "ICMPType": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The ICMP Type when protocol selected is ICMP.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "action": {
            "allowed_chars": null,
            "allowed_choices": [
                "DROP",
                "FORWARD",
                "REDIRECT"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry Possible values are DROP, FORWARD, REDIRECT, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        },
        "addressOverride": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Overrides the source IP for Ingress and destination IP for Egress, macentries will use this adress as the match criteria.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "associatedApplicationID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The associated application ID",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "associatedApplicationObjectID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The associated application object ID",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "associatedApplicationObjectType": {
            "allowed_chars": null,
            "allowed_choices": [
                "ACLENTRY_LOCATION",
                "ADDRESS_RANGE",
                "ADDRESS_RANGE_STATE",
                "ALARM",
                "APPD_APPLICATION",
                "APPD_EXTERNAL_APP_SERVICE",
                "APPD_FLOW",
                "APPD_FLOW_FORWARDING_POLICY",
                "APPD_FLOW_SECURITY_POLICY",
                "APPD_SERVICE",
                "APPD_TIER",
                "APPLICATION",
                "AUTO_DISC_GATEWAY",
                "BACK_HAUL_SERVICE_RESP",
                "BGPPEER",
                "BGP_NEIGHBOR",
                "BGP_NEIGHBOR_MED_RESPONSE",
                "BGP_PROFILE",
                "BGP_PROFILE_MED_RESPONSE",
                "BOOTSTRAP",
                "BOOTSTRAP_ACTIVATION",
                "BRIDGEINTERFACE",
                "CERTIFICATE",
                "CHILD_ENTITY_POLICY_CHANGE",
                "CLOUD_MGMT_SYSTEM",
                "CUSTOMER_VRF_SEQUENCENO",
                "DC_CONFIG",
                "DHCP_ALLOC_MESSAGE",
                "DHCP_CONFIG_RESP",
                "DHCP_OPTION",
                "DISKSTATS",
                "DOMAIN",
                "DOMAIN_CONFIG",
                "DOMAIN_CONFIG_RESP",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "DOMAIN_TEMPLATE",
                "DSCP_FORWARDING_CLASS_MAPPING",
                "DSCP_FORWARDING_CLASS_TABLE",
                "EGRESS_ACL",
                "EGRESS_ACL_ENTRY",
                "EGRESS_ACL_TEMPLATE",
                "EGRESS_ACL_TEMPLATE_ENTRY",
                "EGRESS_QOS_MR",
                "EGRESS_QOS_PRIMITIVE",
                "EGRESS_QOS_QUEUE_MR",
                "ENDPOINT",
                "ENTERPRISE",
                "ENTERPRISE_CONFIG",
                "ENTERPRISE_CONFIG_RESP",
                "ENTERPRISE_NETWORK",
                "ENTERPRISE_PERMISSION",
                "ENTERPRISE_PROFILE",
                "ENTERPRISE_SECURED_DATA",
                "ENTERPRISE_SECURITY",
                "ENTITY_METADATA_BINDING",
                "ESI_SEQUENCENO",
                "EVENT_LOG",
                "EVPN_BGP_COMMUNITY_TAG_ENTRY",
                "EVPN_BGP_COMMUNITY_TAG_SEQ_NO",
                "EXPORTIMPORT",
                "EXTERNAL_SERVICE",
                "FLOATINGIP",
                "FLOATINGIP_ACL",
                "FLOATINGIP_ACL_ENTRY",
                "FLOATING_IP_ACL_TEMPLATE",
                "FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "GATEWAY",
                "GATEWAY_CONFIG",
                "GATEWAY_CONFIG_RESP",
                "GATEWAY_SECURED_DATA",
                "GATEWAY_SECURITY",
                "GATEWAY_SECURITY_PROFILE_REQUEST",
                "GATEWAY_SECURITY_PROFILE_RESPONSE",
                "GATEWAY_SECURITY_REQUEST",
                "GATEWAY_SECURITY_RESPONSE",
                "GATEWAY_SERVICE_CONFIG",
                "GATEWAY_SERVICE_CONFIG_RESP",
                "GATEWAY_TEMPLATE",
                "GATEWAY_VPORT_CONFIG",
                "GATEWAY_VPORT_CONFIG_RESP",
                "GEO_VM_EVENT",
                "GEO_VM_REQ",
                "GEO_VM_RES",
                "GROUP",
                "GROUPKEY_ENCRYPTION_PROFILE",
                "HEALTH_REQ",
                "HOSTINTERFACE",
                "HSC",
                "IKEV2_ENCRYPTION_PROFILE",
                "IKEV2_GATEWAY",
                "INFRASTRUCTURE_CONFIG",
                "INFRASTRUCTURE_GATEWAY_PROFILE",
                "INFRASTRUCTURE_PORT_PROFILE",
                "INFRASTRUCTURE_VSC_PROFILE",
                "INGRESS_ACL",
                "INGRESS_ACL_ENTRY",
                "INGRESS_ACL_TEMPLATE",
                "INGRESS_ACL_TEMPLATE_ENTRY",
                "INGRESS_ADV_FWD",
                "INGRESS_ADV_FWD_ENTRY",
                "INGRESS_ADV_FWD_TEMPLATE",
                "INGRESS_ADV_FWD_TEMPLATE_ENTRY",
                "INGRESS_EXT_SERVICE",
                "INGRESS_EXT_SERVICE_ENTRY",
                "INGRESS_EXT_SERVICE_TEMPLATE",
                "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY",
                "IP_BINDING",
                "JOB",
                "KEYSERVER_MEMBER",
                "KEYSERVER_MONITOR",
                "KEYSERVER_MONITOR_ENCRYPTED_SEED",
                "KEYSERVER_MONITOR_SEED",
                "KEYSERVER_MONITOR_SEK",
                "KEYSERVER_NOTIFICATION",
                "L2DOMAIN",
                "L2DOMAIN_SHARED",
                "L2DOMAIN_TEMPLATE",
                "LDAP_CONFIG",
                "LIBVIRT_INTERFACE",
                "LICENSE",
                "LOCATION",
                "MC_CHANNEL_MAP",
                "MC_LIST",
                "MC_RANGE",
                "METADATA",
                "METADATA_TAG",
                "MIRROR_DESTINATION",
                "MONITORING_PORT",
                "MULTI_NIC_VPORT",
                "NATMAPENTRY",
                "NETWORK_ELEMENT",
                "NETWORK_LAYOUT",
                "NETWORK_MACRO_GROUP",
                "NETWORK_POLICY_GROUP",
                "NEXT_HOP_RESP",
                "NODE_EXECUTION_ERROR",
                "NSGATEWAY",
                "NSGATEWAY_CONFIG",
                "NSGATEWAY_TEMPLATE",
                "NSG_NOTIFICATION",
                "NSPORT",
                "NSPORT_STATIC_CONFIG",
                "NSPORT_TEMPLATE",
                "NSREDUNDANT_GW_GRP",
                "NS_REDUNDANT_PORT",
                "PATCONFIG_CONFIG_RESP",
                "PATNATPOOL",
                "PERMISSION",
                "PERMITTED_ACTION",
                "POLICING_POLICY",
                "POLICY_DECISION",
                "POLICY_GROUP",
                "POLICY_GROUP_TEMPLATE",
                "PORT",
                "PORT_MR",
                "PORT_TEMPLATE",
                "PUBLIC_NETWORK",
                "QOS_PRIMITIVE",
                "RATE_LIMITER",
                "RD_SEQUENCENO",
                "REDUNDANT_GW_GRP",
                "RESYNC",
                "ROUTING_POLICY",
                "ROUTING_POL_MED_RESPONSE",
                "RTRD_ENTITY",
                "RTRD_SEQUENCENO",
                "SERVICES_GATEWAY_RESPONSE",
                "SERVICE_GATEWAY_RESPONSE",
                "SERVICE_VRF_SEQUENCENO",
                "SHAPING_POLICY",
                "SHARED_RESOURCE",
                "SITE",
                "SITE_REQ",
                "SITE_RES",
                "STATIC_ROUTE",
                "STATIC_ROUTE_RESP",
                "STATISTICS",
                "STATSSERVER",
                "STATS_COLLECTOR",
                "STATS_POLICY",
                "STATS_TCA",
                "SUBNET",
                "SUBNET_ENTRY",
                "SUBNET_MAC_ENTRY",
                "SUBNET_POOL_ENTRY",
                "SUBNET_TEMPLATE",
                "SYSTEM_CONFIG",
                "SYSTEM_CONFIG_REQ",
                "SYSTEM_CONFIG_RESP",
                "SYSTEM_MONITORING",
                "UNSUPPORTED",
                "UPLINK_RD",
                "USER",
                "VIRTUAL_IP",
                "VIRTUAL_MACHINE",
                "VIRTUAL_MACHINE_REPORT",
                "VLAN",
                "VLAN_CONFIG_RESPONSE",
                "VLAN_TEMPLATE",
                "VMWARE_RELOAD_CONFIG",
                "VMWARE_VCENTER",
                "VMWARE_VCENTER_CLUSTER",
                "VMWARE_VCENTER_DATACENTER",
                "VMWARE_VCENTER_EAM_CONFIG",
                "VMWARE_VCENTER_HYPERVISOR",
                "VMWARE_VCENTER_VRS_BASE_CONFIG",
                "VMWARE_VCENTER_VRS_CONFIG",
                "VMWARE_VRS_ADDRESS_RANGE",
                "VM_DESCRIPTION",
                "VM_INTERFACE",
                "VNID_SEQUENCENO",
                "VPN_CONNECT",
                "VPORT",
                "VPORTTAG",
                "VPORTTAGTEMPLATE",
                "VPORT_GATEWAY_RESPONSE",
                "VPORT_MEDIATION_REQUEST",
                "VPORT_MIRROR",
                "VPORT_TAG_BASE",
                "VPRN_LABEL_SEQUENCENO",
                "VRS",
                "VSC",
                "VSD",
                "VSD_COMPONENT",
                "VSG_REDUNDANT_PORT",
                "VSP",
                "WAN_SERVICE",
                "ZONE",
                "ZONE_TEMPLATE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The associated application object type Refer to API section for supported types.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        },
        "associatedLiveEntityID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "description": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Description of the ACL entry",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "destinationPort": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "etherType": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "flowLoggingEnabled": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Is flow logging enabled for this particular template",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": "no"
        },
        "locationID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The ID of the location entity (Subnet/Zone/VportTag)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "locationType": {
            "allowed_chars": null,
            "allowed_choices": [
                "ANY",
                "POLICYGROUP",
                "REDIRECTIONTARGET",
                "SUBNET",
                "VPORTTAG",
                "ZONE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Type of the location entity.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        },
        "mirrorDestinationID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Destination ID of the mirror destination object.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "networkID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The destination network entity that is referenced(subnet/zone/macro)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "networkType": {
            "allowed_chars": null,
            "allowed_choices": [
                "ANY",
                "ENDPOINT_DOMAIN",
                "ENDPOINT_SUBNET",
                "ENDPOINT_ZONE",
                "ENTERPRISE_NETWORK",
                "INTERNET_POLICYGROUP",
                "NETWORK_MACRO_GROUP",
                "POLICYGROUP",
                "PUBLIC_NETWORK",
                "SUBNET",
                "ZONE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Type of the source network.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        },
        "policyState": {
            "allowed_chars": null,
            "allowed_choices": [
                "DRAFT",
                "LIVE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "State of the policy.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        },
        "priority": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The priority of the ACL entry that determines the order of entries",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": 0,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": "no"
        },
        "protocol": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Protocol number that must be matched",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "reflexive": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": true,
            "description": "True means that this ACL entry is reflexive, so there will be a corresponding rule that will be created by OVS in the network. False means that there is no corresponding rule created by OVS in the network.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": "no"
        },
        "sourcePort": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "stateful": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "True means that this ACL entry is stateful, so there will be a corresponding rule that will be created by OVS in the network. False means that there is no corresponding rule created by OVS in the network.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": "no"
        },
        "statsID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "statsLoggingEnabled": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Is stats logging enabled for this particular template",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": "no"
        }
    },
    "children": {
        "job": {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": true,
            "delete": false,
            "deprecated": false,
            "get": false,
            "relationship": "child",
            "update": false
        },
        "statistics": {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": false,
            "get": true,
            "relationship": "child",
            "update": false
        }
    },
    "model": {
        "create": false,
        "delete": true,
        "description": "Defines the template of Ingress ACL entries",
        "entity_name": "IngressACLEntryTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy/acl",
        "resource_name": "ingressaclentrytemplates",
        "rest_name": "ingressaclentrytemplate",
        "root": false,
        "update": true
    }
}
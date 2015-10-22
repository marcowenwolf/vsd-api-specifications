{
    "resource_name": "domaintemplates", 
    "description": "Domains in VSD are created from domain templates. This object provides the definition of the DomainTemplate", 
    "entity_name": "DomainTemplate", 
    "package": "/network", 
    "update": true, 
    "rest_name": "domaintemplate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "attributes": {
        "policyChangeStatus": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "ENABLED", 
                "DISABLED"
            ], 
            "availability": null, 
            "default_value": null, 
            "default_order": false, 
            "filterable": false, 
            "creation_only": false, 
            "max_length": null, 
            "orderable": false, 
            "type": "enum", 
            "channel": null, 
            "read_only": false, 
            "allowed_chars": null, 
            "description": "", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "description": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": null, 
            "availability": null, 
            "default_value": null, 
            "default_order": false, 
            "filterable": false, 
            "creation_only": false, 
            "max_length": null, 
            "orderable": false, 
            "type": "string", 
            "channel": null, 
            "read_only": false, 
            "allowed_chars": null, 
            "description": "Domain template description provided by the user", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "encryption": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "ENABLED", 
                "DISABLED"
            ], 
            "availability": null, 
            "default_value": null, 
            "default_order": false, 
            "filterable": false, 
            "creation_only": false, 
            "max_length": null, 
            "orderable": false, 
            "type": "enum", 
            "channel": null, 
            "read_only": false, 
            "allowed_chars": null, 
            "description": "Determines whether IPSEC is enabled. Possible values are ENABLED, DISABLED, .", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "associatedMulticastChannelMapID": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": null, 
            "availability": null, 
            "default_value": null, 
            "default_order": false, 
            "filterable": false, 
            "creation_only": false, 
            "max_length": null, 
            "orderable": false, 
            "type": "string", 
            "channel": null, 
            "read_only": false, 
            "allowed_chars": null, 
            "description": "The ID of the Multi Cast Channel Map  this domain template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "multicast": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "ENABLED", 
                "INHERITED", 
                "DISABLED"
            ], 
            "availability": null, 
            "default_value": null, 
            "default_order": false, 
            "filterable": false, 
            "creation_only": false, 
            "max_length": null, 
            "orderable": false, 
            "type": "enum", 
            "channel": null, 
            "read_only": false, 
            "allowed_chars": null, 
            "description": "multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "name": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": null, 
            "availability": null, 
            "default_value": null, 
            "default_order": false, 
            "filterable": false, 
            "creation_only": false, 
            "max_length": null, 
            "orderable": false, 
            "type": "string", 
            "channel": null, 
            "read_only": false, 
            "allowed_chars": null, 
            "description": "The name of the domain template, that is unique within an enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": true
        }
    }, 
    "get": true, 
    "children": {
        "domain": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "qos": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "permission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "egressacltemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ingressadvfwdtemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "group": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "policygrouptemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "zonetemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "redirectiontargettemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "subnettemplate": {
            "relationship": "child", 
            "get": true
        }, 
        "ingressexternalservicetemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ingressacltemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }, 
    "delete": true
}
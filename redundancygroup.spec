{
    "resource_name": "redundancygroups", 
    "description": "Represents Redundant Group formed by two Gateways", 
    "entity_name": "RedundancyGroup", 
    "package": "/gateway", 
    "update": true, 
    "rest_name": "redundancygroup", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "attributes": {
        "redundantGatewayStatus": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "SUCCESS", 
                "FAILED"
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
            "description": "The status of  Redundant Group, possible values are FAILED, SUCCESS Possible values are FAILED, SUCCESS, .", 
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
            "description": " Description of the Redundancy Group", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "permittedAction": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
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
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "gatewayPeer2AutodiscoveredGatewayID": {
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
            "description": "The Auto Discovered Gateway  peer in this Redundant Group", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "gatewayPeer2ID": {
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
            "description": "The gateway peer in this Redundant Group. when Redundant Group is deleted this gateway will not recieve vport associations ", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "enterpriseID": {
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
            "description": "The enterprise associated with this Redundant Group. This is a read only attribute", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "gatewayPeer2Name": {
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
            "description": "The gateway peer name in this Redundant Group", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "gatewayPeer1ID": {
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
            "description": "The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations ", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "gatewayPeer1Name": {
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
            "description": "The gateway   configuration owner name in this Redundant Group", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "personality": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "DC7X50", 
                "OTHER", 
                "VRSG", 
                "VSG", 
                "VSA", 
                "HARDWARE_VTEP", 
                "NSG"
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
            "description": "derived personality of the Redundancy Group - VSG,VRSG,NSG,OTHER Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "gatewayPeer1AutodiscoveredGatewayID": {
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
            "description": "The Auto Discovered Gateway configuration owner in this Redundant Group. ", 
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
            "description": "Name of the Redundancy Group ", 
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
        "service": {
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
        "alarm": {
            "relationship": "child", 
            "get": true
        }, 
        "enterprisepermission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "port": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "gateway": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }
    }, 
    "delete": true
}
{
    "resource_name": "tcas", 
    "description": "Provides the definition of the Threshold Control Alarms", 
    "entity_name": "TCA", 
    "package": "/stats", 
    "update": true, 
    "rest_name": "tca", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "attributes": {
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
            "description": "Desription of the TCA", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "metric": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "BYTES_IN", 
                "EGRESS_BYTE_COUNT", 
                "PACKETS_IN_ERROR", 
                "PACKETS_OUT_DROPPED", 
                "BYTES_OUT", 
                "PACKETS_IN_DROPPED", 
                "INGRESS_BYTE_COUNT", 
                "PACKETS_IN", 
                "PACKETS_OUT_ERROR", 
                "PACKETS_DROPPED_BY_RATE_LIMIT", 
                "INGRESS_PACKET_COUNT", 
                "PACKETS_OUT", 
                "EGRESS_PACKET_COUNT"
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
            "description": "The metric associated with the TCA - PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR and PACKETS_DROPPED_BY_RATE_LIMIT Possible values are PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT, PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR, PACKETS_DROPPED_BY_RATE_LIMIT, INGRESS_BYTE_COUNT, INGRESS_PACKET_COUNT, EGRESS_BYTE_COUNT, EGRESS_PACKET_COUNT, .", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": true
        }, 
        "period": {
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
            "type": "long", 
            "channel": null, 
            "read_only": false, 
            "allowed_chars": null, 
            "description": "The averaging period", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": true
        }, 
        "URLEndPoint": {
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
            "description": "URL endpoint to post Alarm data to when TCA is triggered", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "threshold": {
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
            "type": "long", 
            "channel": null, 
            "read_only": false, 
            "allowed_chars": null, 
            "description": "The threshold that must be exceeded before an alarm is issued", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": true
        }, 
        "scope": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "LOCAL", 
                "GLOBAL"
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
            "description": "GLOBAL or LOCAL scope. Global refers to aggregate values across subnets, zones or domains. Local refers to traffic from/to individual VMs Possible values are GLOBAL, LOCAL, .", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": true
        }, 
        "type": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [
                "ROLLING_AVERAGE", 
                "BREACH"
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
            "description": "Rolling average or sequence of samples over the averaging period - ROLLING_AVERAGE or BREACH Possible values are ROLLING_AVERAGE, BREACH, .", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": true
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
            "description": "The name of the TCA", 
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
        "alarm": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }, 
    "delete": true
}
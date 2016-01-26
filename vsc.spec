{
    "attributes": {
        "address": {
            "description": "The IP of the VRS entity",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 1,
            "max_length": 50,
            "uniqueScope": "no"
        },
        "alreadyMarkedForUnavailable": {
            "description": "Flag to indicate that it is already marked a unavailable.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "averageCPUUsage": {
            "description": "Average CPU usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "subtype": "double",
            "uniqueScope": "no"
        },
        "averageMemoryUsage": {
            "description": "Average memory usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "subtype": "double",
            "uniqueScope": "no"
        },
        "currentCPUUsage": {
            "description": "Current CPU usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "subtype": "double",
            "uniqueScope": "no"
        },
        "currentMemoryUsage": {
            "description": "Current memory usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "subtype": "double",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the entity.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "disks": {
            "description": "Set of disk usage details.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "object",
            "uniqueScope": "no"
        },
        "lastStateChange": {
            "description": "Last state change timestamp (in millis).",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "location": {
            "description": "Identifies the entity to be associated with a location.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 128,
            "uniqueScope": "no"
        },
        "managementIP": {
            "description": "The management IP of the VSC/HSC entity",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 1,
            "max_length": 50,
            "uniqueScope": "no"
        },
        "messages": {
            "description": "An array of degraded messages.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Identifies the entity with a name.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 128,
            "uniqueScope": "no"
        },
        "peakCPUUsage": {
            "description": "Peek CPU usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "subtype": "double",
            "uniqueScope": "no"
        },
        "peakMemoryUsage": {
            "description": "Peek memory usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "subtype": "double",
            "uniqueScope": "no"
        },
        "productVersion": {
            "description": "Product version supported by this entity.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 50,
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "DOWN",
                "UP",
                "ADMIN_DOWN"
            ],
            "description": "Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "unavailableTimestamp": {
            "description": "The duration the controller is unavailable (in millis).",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "vsds": {
            "description": "A collection of VSD id(s) which are identified by this controller.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "alarm": {
            "get": true,
            "relationship": "child"
        },
        "bgppeer": {
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "job": {
            "create": true,
            "relationship": "child"
        },
        "monitoringport": {
            "get": true,
            "relationship": "child"
        },
        "vrs": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "System Monitoring details for VSC",
        "entity_name": "VSC",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "sysmon",
        "resource_name": "vscs",
        "rest_name": "vsc",
        "update": true
    }
}
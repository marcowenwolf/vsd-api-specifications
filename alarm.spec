{
    "attributes": {
        "acknowledged": {
            "description": "Flag to indicate that alarm is already acknowledged or not", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the alarm", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterpriseID": {
            "description": "Enterprise that this alarm belongs to", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "errorCondition": {
            "description": "Identifies the error condition", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "The alarm name.  Each type of alarm will generate its own name", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "numberOfOccurances": {
            "description": "Number of times that the alarm was triggered", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "reason": {
            "description": "Provides a description of the alarm", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "severity": {
            "allowed_choices": [
                "MINOR", 
                "MAJOR", 
                "WARNING", 
                "CRITICAL", 
                "INFO"
            ], 
            "description": "Severity of the alarm.  Possible values are MAJOR, MINOR, CRITICAL, INFO, WARNING, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "targetObject": {
            "description": "Identifies affected Entity.  Example: Alarm generated by TCA for Domain domain1(Packets towards a VM, Breach)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "timestamp": {
            "description": "Indicates the time that the alarm was triggered", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "The alarm API allows the management of system alarms.", 
    "entity_name": "Alarm", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/alarm", 
    "resource_name": "alarms", 
    "rest_name": "alarm", 
    "update": true
}
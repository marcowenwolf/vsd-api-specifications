{
    "resource_name": "permissions", 
    "description": "Represents  Permitted action on an  entity for a group", 
    "entity_name": "PermittedAction", 
    "package": "/usermgmt", 
    "update": true, 
    "rest_name": "permission", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "attributes": {
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
            "description": "Name of the  Permission", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "permittedEntityType": {
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
            "description": "Type of the entity for which we have given permission.", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "permittedEntityDescription": {
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
            "description": "Description for the permittedEntity", 
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
            "description": "The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": true
        }, 
        "permittedEntityName": {
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
            "description": "Name of the entity for which we have given permission.", 
            "format": null, 
            "max_value": null, 
            "min_value": null, 
            "transient": false, 
            "unique": false, 
            "min_length": null, 
            "required": false
        }, 
        "permittedEntityID": {
            "exposed": true, 
            "autogenerated": false, 
            "allowed_choices": [], 
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
            "description": "The  entity ID for which this permission action is associated against Possible values are .", 
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
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }, 
    "delete": true
}
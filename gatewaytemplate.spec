{
  "apis": {
    "children": {
      "/gatewaytemplates/id/metadatas": {
        "RESTName": "metadata",
        "entityName": "Metadata",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          },
          {
            "availability": null,
            "method": "POST"
          }
        ],
        "resourceName": "metadatas"
      },
      "/gatewaytemplates/{id}/porttemplates": {
        "RESTName": "porttemplate",
        "entityName": "PortTemplate",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          },
          {
            "availability": null,
            "method": "POST"
          }
        ],
        "resourceName": "porttemplates"
      }
    },
    "parents": {
      "/enterprises/{id}/gatewaytemplates": {
        "RESTName": "enterprise",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          },
          {
            "availability": null,
            "method": "POST"
          }
        ],
        "resourceName": "enterprises"
      },
      "/gatewaytemplates": {
        "RESTName": "gatewaytemplate",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          },
          {
            "availability": null,
            "method": "POST"
          }
        ],
        "resourceName": "gatewaytemplates"
      }
    },
    "self": {
      "/gatewaytemplates/{id}": {
        "RESTName": "gatewaytemplate",
        "operations": [
          {
            "availability": null,
            "method": "PUT"
          },
          {
            "availability": null,
            "method": "DELETE"
          },
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "gatewaytemplates"
      }
    }
  },
  "model": {
    "RESTName": "gatewaytemplate",
    "attributes": {
      "description": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "A description of the Gateway",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "string",
        "unique": false
      },
      "enterpriseID": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "The enterprise associated with this Gateway. This is a read only attribute",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "string",
        "unique": false
      },
      "entityScope": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Specify if scope of entity is Data center or Enterprise level",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "EntityScope",
        "unique": false
      },
      "name": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Name of the Gateway",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": true,
        "transient": false,
        "type": "string",
        "unique": false
      },
      "personality": {
        "allowedChars": null,
        "allowedChoices": [
          "DC7X50",
          "OTHER",
          "VRSG",
          "VSG",
          "VSA",
          "HARDWARE_VTEP",
          "NSG"
        ],
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Personality of the Gateway - VSG,VRSG,NSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": true,
        "transient": false,
        "type": "enum",
        "unique": false
      }
    },
    "description": "Represents Gateway Template object",
    "entityName": "GatewayTemplate",
    "package": "/gateway",
    "resourceName": "gatewaytemplates"
  }
}
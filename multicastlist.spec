{
  "apis": {
    "children": {
      "/multicastlists/id/metadatas": {
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
      "/multicastlists/{id}/multicastchannelmaps": {
        "RESTName": "multicastchannelmap",
        "entityName": "MultiCastChannelMap",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          },
          {
            "availability": null,
            "method": "PUT"
          }
        ],
        "resourceName": "multicastchannelmaps"
      }
    },
    "parents": {
      "/enterpriseprofiles/{id}/multicastlists": {
        "RESTName": "enterpriseprofile",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "enterpriseprofiles"
      },
      "/enterprises/{id}/multicastlists": {
        "RESTName": "enterprise",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "enterprises"
      }
    },
    "self": {
      "/multicastlists/{id}": {
        "RESTName": "multicastlist",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "multicastlists"
      }
    }
  },
  "model": {
    "RESTName": "multicastlist",
    "attributes": {
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
      "mcastType": {
        "allowedChars": null,
        "allowedChoices": [
          "SEND",
          "RECEIVE"
        ],
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Type of multicast list - send or receive Possible values are SEND, RECEIVE, .",
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
        "type": "enum",
        "unique": false
      }
    },
    "description": "This is the definition of a MultiCast Channel List",
    "entityName": "MultiCastList",
    "package": "/network",
    "resourceName": "multicastlists"
  }
}
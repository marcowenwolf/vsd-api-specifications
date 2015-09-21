{
  "apis": {
    "children": {},
    "parents": {
      "/bridgeinterfaces/{id}/statistics": {
        "RESTName": "bridgeinterface",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "bridgeinterfaces"
      },
      "/domains/{id}/statistics": {
        "RESTName": "domain",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "domains"
      },
      "/egressaclentrytemplates/{id}/statistics": {
        "RESTName": "egressaclentrytemplate",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "egressaclentrytemplates"
      },
      "/hostinterfaces/{id}/statistics": {
        "RESTName": "hostinterface",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "hostinterfaces"
      },
      "/ingressaclentrytemplates/{id}/statistics": {
        "RESTName": "ingressaclentrytemplate",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "ingressaclentrytemplates"
      },
      "/ingressadvfwdentrytemplates/{id}/statistics": {
        "RESTName": "ingressadvfwdentrytemplate",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "ingressadvfwdentrytemplates"
      },
      "/ingressexternalserviceentrytemplates/{id}/statistics": {
        "RESTName": "ingressexternalserviceentrytemplate",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "ingressexternalserviceentrytemplates"
      },
      "/l2domains/{id}/statistics": {
        "RESTName": "l2domain",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "l2domains"
      },
      "/subnets/{id}/statistics": {
        "RESTName": "subnet",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "subnets"
      },
      "/tiers/{id}/statistics": {
        "RESTName": "tier",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "tiers"
      },
      "/vminterfaces/{id}/statistics": {
        "RESTName": "vminterface",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "vminterfaces"
      },
      "/vports/{id}/statistics": {
        "RESTName": "vport",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "vports"
      },
      "/zones/{id}/statistics": {
        "RESTName": "zone",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "zones"
      }
    },
    "self": {}
  },
  "model": {
    "RESTName": "statistics",
    "attributes": {
      "endTime": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "End time for the statistics to be retrieved",
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
        "type": "long",
        "unique": false
      },
      "numberOfDataPoints": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Number of data points between start time and end time",
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
        "type": "int",
        "unique": false
      },
      "startTime": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Start time for the statistics to be retrieved",
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
        "type": "long",
        "unique": false
      },
      "statsData": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packets_out_errors, packets_dropped_rate_limit",
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
        "type": "Map",
        "unique": false
      },
      "version": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Version of this Sequence number.",
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
        "type": "long",
        "unique": false
      }
    },
    "description": "Retrieves the statistics for a particular domain, zone, subnet, or VM",
    "entityName": "Statistics",
    "package": "/stats",
    "resourceName": "statistics"
  }
}
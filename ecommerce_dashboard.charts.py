{
  "exportVersion": 10,
  "dashboards": {
    "dashboard-ecommerce-1": {
      "title": "E-Commerce Real-Time Orders Dashboard",
      "layout": [
        { "w": 2, "h": 2, "x": 0, "y": 0, "i": "item-revenue" },
        { "w": 4, "h": 3, "x": 2, "y": 0, "i": "item-status" },
        { "w": 4, "h": 3, "x": 0, "y": 2, "i": "item-payment" }
      ],
      "description": "Live dashboard analyzing consumed streaming order and payment data from Kafka.",
      "embedding": { "anonymousAuthEnabled": true },
      "filters": []
    }
  },
  "items": {
    "item-revenue": {
      "title": "Total Sales Revenue ($)",
      "description": "Live sum of all order amounts.",
      "dashboardId": "dashboard-ecommerce-1",
      "dataSourceId": "data-source-orders",
      "iconValue": "number",
      "itemType": "chart",
      "filters": [],
      "missedFields": [],
      "lookupFields": [],
      "convertedFields": [],
      "calculatedFields": [],
      "channels": {
        "value": {
          "field": "amount",
          "type": "quantitative",
          "inferredType": "Number",
          "channelType": "aggregation",
          "aggregate": "sum"
        }
      },
      "reductions": {},
      "customisations": {
        "options": {},
        "axes": {},
        "channels": {
          "value": {
            "numberFormatting": { "enabled": true, "value": "Custom" },
            "numberDecimals": { "enabled": true, "value": "2" }
          }
        },
        "conditionalFormatting": []
      },
      "chartType": "Number",
      "meta": {},
      "sample": false,
      "query": null,
      "queryId": null,
      "interactiveFiltering": "highlight"
    },
    "item-status": {
      "title": "Order Status Breakdown",
      "description": "Monitors the ratio of successful payments to failed payments.",
      "dashboardId": "dashboard-ecommerce-1",
      "dataSourceId": "data-source-orders",
      "iconValue": "donut",
      "itemType": "chart",
      "filters": [],
      "missedFields": [],
      "lookupFields": [],
      "convertedFields": [],
      "calculatedFields": [],
      "channels": {
        "label": {
          "field": "status",
          "type": "nominal",
          "inferredType": "String",
          "channelType": "category",
          "isLimiting": true,
          "limitingSize": "10",
          "allOthers": true
        },
        "value": {
          "field": "_id",
          "type": "quantitative",
          "inferredType": "String",
          "channelType": "aggregation",
          "aggregate": "count"
        }
      },
      "reductions": {},
      "customisations": {
        "options": {},
        "axes": { "value": {} },
        "channels": {
          "label": { "labelOverride": { "enabled": true, "value": "Status" } },
          "value": { "numberFormatting": { "enabled": true, "value": "Default" } }
        },
        "conditionalFormatting": []
      },
      "chartType": "Donut",
      "meta": {},
      "sample": false,
      "query": null,
      "queryId": null,
      "interactiveFiltering": "highlight"
    },
    "item-payment": {
      "title": "Revenue by Payment Method",
      "description": "Compares order volume across Credit Card, UPI, PayPal, and Debit Card.",
      "dashboardId": "dashboard-ecommerce-1",
      "dataSourceId": "data-source-orders",
      "iconValue": "bar-grouped",
      "itemType": "chart",
      "filters": [],
      "missedFields": [],
      "lookupFields": [],
      "convertedFields": [],
      "calculatedFields": [],
      "channels": {
        "x": {
          "field": "payment_method",
          "type": "nominal",
          "inferredType": "String",
          "channelType": "category",
          "isLimiting": true,
          "limitingSize": "10"
        },
        "y": {
          "field": "amount",
          "type": "quantitative",
          "inferredType": "Number",
          "channelType": "aggregation",
          "aggregate": "sum"
        }
      },
      "reductions": {},
      "customisations": {
        "options": { "colorDiscrete": { "enabled": true, "value": ["#16CC62"] } },
        "axes": { "x": {}, "y": {} },
        "channels": {
          "x": { "labelOverride": { "enabled": true, "value": "Payment Method" } },
          "y": { "labelOverride": { "enabled": true, "value": "Total Revenue" }, "numberFormatting": { "enabled": true, "value": "Default" } }
        },
        "conditionalFormatting": []
      },
      "chartType": "Grouped Column",
      "meta": {},
      "sample": false,
      "query": null,
      "queryId": null,
      "interactiveFiltering": "highlight"
    }
  },
  "dataSources": {
    "data-source-orders": {
      "alias": "Kafka Consumed Data: Orders",
      "collection": "orders",
      "database": "ecommerce_streaming",
      "deployment": "my-atlas-cluster",
      "sourceType": "cluster"
    }
  },
  "queries": {}
}
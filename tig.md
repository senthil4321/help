# tig
## telegraph

## influxdb
### line protocol
```
temperature,location=north value=60.0
```
```lineprotocol
// Syntax
<measurement>[,<tag_key>=<tag_value>[,<tag_key>=<tag_value>]] <field_key>=<field_value>[,<field_key>=<field_value>] [<timestamp>]

// Example
myMeasurement,tag1=value1,tag2=value2 fieldKey="fieldValue" 1556813561098000000
```
### http api
* https://docs.influxdata.com/influxdb/v2.0/reference/api/
### Ref.
* https://docs.influxdata.com/influxdb/v1.8/introduction/get-started/

## grafana

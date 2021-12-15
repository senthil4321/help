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


| Protocol |
| - |
| Measurement |
| Tag key |
| Tag value |
| Field key |
| Field value |

### influx db ui
Influx db has its own ui
## grafana
### cognitive load
Dashboards should reduce cognitive load, not add to it
Cognitive load is basically how hard you need to think about something in order to figure it out. Make your dashboard easy to interpret. Other users and future you (when you’re trying to figure out what broke at 2AM) will appreciate it.

Ask yourself:

Can I tell what exactly each graph represents? Is it obvious, or do I have to think about it?
If I show this to someone else, how long will it take them to figure it out? Will they get lost?

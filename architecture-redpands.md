Redpanda is the **event bus / streaming backbone** sitting between the edge and the data platform — it's what lets telemetry get consumed by multiple independent things at once without the edge-gateway needing to know or care who's downstream.

**Where it sits in the pipeline:**

```
device → Mosquitto (MQTT) → edge-gateway → REDPANDA → consumers → Postgres
```
The edge-gateway validates each MQTT message and *produces* it onto Redpanda as one of 4 topics (confirmed live earlier): `telemetry.v1`, `device-status.v1`, `audit.v1`, `alerts.v1`. It doesn't talk to Postgres directly at all.

**Why it's there instead of the gateway just writing to Postgres itself:**

1. **Multiple independent readers, one write.** Three separate consumer groups all read the *same* topics independently: `persister` (writes to `telemetry`/`device_status` tables), `alert-evaluator` (checks threshold breaches), `audit-writer` (builds the hash-chained audit log). Each can be slow, crash, or fall behind without affecting the others or the gateway — they each track their own offset.

2. **It's the buffer that makes store-and-forward real, not just at the edge.** You saw this happen for real today: when the `consumers` container's DB threads died on boot, telemetry kept flowing gateway→Redpanda just fine and queued up there — nothing was lost, it just sat unconsumed until I restarted `consumers`, which then drained the backlog. That's the whole point of a durable log in the middle: producer and consumer availability are decoupled.

3. **Per-device ordering + horizontal scale.** Each topic has 3 partitions, keyed by `device_id` — so all of `dev-0001`'s messages land in order in the same partition (sequence numbers stay meaningful), while different devices can be processed in parallel across partitions.

4. **Replay.** Topics retain 7 days (`retention.ms=604800000`, set at topic creation). If a consumer's logic was buggy and you fix it, you can reprocess the last week of history — you're not limited to "whatever was in the DB," which is a real strength in a system tracking safety-relevant medical device data.

**Why Redpanda specifically, not "real" Kafka:** it speaks the identical Kafka wire protocol (the project's own `confluent-kafka` client code would work unmodified against real Kafka/MSK), but it's a single C++ binary with no JVM and no ZooKeeper — much lighter for a single-host demo running on a disk/memory-constrained VM. In a real AWS deployment this slot is filled by **MSK or Kinesis** (per the architecture's AWS mapping table) — the consumer-group semantics carry over to MSK unchanged since it's the same protocol.

One thing worth being honest about for a demo host: replication factor is `1` here (single broker, single copy of each partition) — fine for a demo, but the thing that would need to change first for anything resembling production durability.

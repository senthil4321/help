# hc

## server

- HL7 MLLP server
- Mirth Connect

## Standard

- HL7 v2.x standard

## Store, Aggregate, and Forward

1. **StoreAction:**
   The intermediate node (like a gateway, edge device, or router) receives incoming data packets and temporarily writes them to a local storage buffer, memory, or disk.

   **Purpose:** It ensures data integrity. By storing the data locally, the system can verify that the packets are complete and error-free before doing anything else with them.

2. **AggregateAction:**
   The node combines, filters, or processes the stored data. Instead of handling each packet individually, it groups data based on specific rules (e.g., by time window, data type, or source).

   **Purpose:** It reduces bandwidth and increases efficiency. For example, instead of sending 60 separate temperature readings every second, it aggregates them into a single average reading sent once.

3. **ForwardAction:**
   The node transmits the newly aggregated and optimized data package over the network to the next destination or central cloud server.

   **Purpose:** It delivers the final, processed information to its destination only when the network link is available and optimized for transmission.

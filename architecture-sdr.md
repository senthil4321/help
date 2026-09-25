# ADR-[NUMBER]: [Short, Action-Oriented Title]

* **Status:** [Proposed | Accepted | Rejected | Superseded by ADR-XXXX | Deprecated]
* **Date:** YYYY-MM-DD
* **Deciders:** [List of key stakeholders and engineers involved]
* **Technical Context:** [Link to JIRA ticket, GitHub issue, or PRD]

## Context
[Describe the architectural issue or business requirement. Explain the background, current state, and the problem that needs to be solved. Keep this objective and focused on facts.]

## Decision Drivers
* [Driver 1: e.g., Sub-100ms latency requirement for checkout]
* [Driver 2: e.g., Need strong ACID compliance for order processing]
* [Driver 3: e.g., Operational budget limits for cloud infrastructure]

## Options Considered
* **Option 1:** [Option 1 Name]
* **Option 2:** [Option 2 Name]
* **Option 3:** [Option 3 Name]

## Decision Outcome
Chosen Option: **[Option Name]**, because [state core rationale briefly].

### Positive Consequences
* [Benefit 1]
* [Benefit 2]

### Negative Consequences & Trade-offs
* [Drawback or risk 1, plus any planned mitigation]
* [Drawback or risk 2]

## Pros and Cons of Options

### Option 1: [Option 1 Name]
* **Good, because** [Pro 1]
* **Good, because** [Pro 2]
* **Bad, because** [Con 1]

### Option 2: [Option 2 Name]
* **Good, because** [Pro 1]
* **Bad, because** [Con 1]
* **Bad, because** [Con 2]

--- 

# ADR-0012: Adopt gRPC for Inter-Service Communication

* **Status:** Accepted
* **Date:** 2026-03-15
* **Deciders:** Jane Doe (Lead Architect), John Smith (Backend Staff Engineer)
* **Technical Context:** [PROJ-4021] Core Payment Pipeline Performance Optimization

## Context
Our internal microservice communication relies entirely on HTTP/REST with JSON payloads. As the platform expanded to over 40 services, payload sizes and HTTP/1.1 connection overhead have caused latency spikes in our checkout pipeline. We need a faster, type-safe serialization format for high-throughput internal communication.

## Decision Drivers
* Internal P99 API response time must remain under 50ms during peak load.
* Strong type safety across Go and Node.js microservices.
* Minimal operational overhead for maintaining API schemas.

## Options Considered
* **Option 1:** REST over HTTP/1.1 with JSON payloads (Status Quo)
* **Option 2:** gRPC over HTTP/2 with Protocol Buffers
* **Option 3:** GraphQL over HTTP/1.1

## Decision Outcome
Chosen Option: **Option 2 (gRPC)**, because it delivers significantly smaller binary payloads, multiplexing over HTTP/2, and strict contract generation across multiple languages.

### Positive Consequences
* **Performance:** Payload sizes reduced by ~60% and network latency decreased by 35% in staging benchmarks.
* **Type Safety:** Automated code generation via `.proto` files eliminates manual API client construction.
* **Streaming:** Enables native bidirectional streaming for real-time order tracking services.

### Negative Consequences & Trade-offs
* **Debugging Friction:** Binary payloads make inspection via traditional tools (e.g., standard `curl`) harder without dedicated tooling like `grpcurl`.
* **Browser Limitations:** Web clients cannot consume gRPC directly without gRPC-Web proxies (REST will be retained for public-facing edge APIs).

## Pros and Cons of Options

### Option 1: REST over HTTP/1.1 with JSON
* **Good, because** simple to debug with standard tools and universally understood by developers.
* **Bad, because** JSON serialization and text-based HTTP payloads introduce high CPU and bandwidth overhead.
* **Bad, because** API contracts rely on OpenAPI specs that frequently drift out of sync with code implementations.

### Option 2: gRPC over HTTP/2 with Protocol Buffers
* **Good, because** binary protocol offers superior serialization speed and lower network footprint.
* **Good, because** HTTP/2 multiplexing allows multiple concurrent calls over a single TCP connection.
* **Bad, because** steeper learning curve for team members unfamiliar with Protocol Buffers and gRPC tooling.

### Option 3: GraphQL over HTTP/1.1
* **Good, because** allows callers to query exact data fields required.
* **Bad, because** introduces query-parsing CPU overhead and complex caching requirements for internal service-to-service calls.

---

# ADR-0019: Adopt DTLS for Real-Time Edge Sensor Telemetry

* **Status:** Accepted
* **Date:** 2026-09-20
* **Deciders:** Edge Systems Architecture Team, Security Operations Group
* **Technical Context:** `[IOT-884]` Real-Time Gateway Telemetry Streaming Architecture

## Context

Our industrial edge gateways transmit high-frequency sensor readings (50 Hz) and status telemetry to cloud ingest nodes over unstable cellular (LTE/5G) and satellite links. Currently, telemetry is sent via MQTT over **TLS (TCP)**.

On lossy or high-jitter network connections, TCP's packet loss recovery mechanisms cause head-of-line blocking. A single dropped packet stalls the entire TCP stream, causing queue build-up on the edge gateway and unacceptable latency spikes for live telemetry dashboards and anomaly detection alerts. We need a secure transport layer protocol that eliminates head-of-line blocking while maintaining transport-layer security and identity verification.

## Decision Drivers

* **Latency & Jitter:** Telemetry transport overhead must not stall current data frames due to retransmission of stale historical frames.
* **Network Efficiency:** Transport must handle packet loss and intermittent network dropouts smoothly over cellular/satellite links.
* **Security & Compliance:** Must provide mutual authentication (mTLS/mDTLS via X.509 certificates) and strong cipher suites (AES-GCM, ChaCha20-Poly1305) identical to TLS standards.
* **Resource Constraints:** Low memory and processing overhead on memory-constrained edge hardware.

## Options Considered

* **Option 1:** TLS 1.3 over TCP (Status Quo)
* **Option 2:** DTLS 1.3 over UDP
* **Option 3:** IPSec / WireGuard Tunnel (Network-layer VPN)

## Decision Outcome

Chosen Option: **Option 2 (DTLS 1.3 over UDP)**.

DTLS (Datagram Transport Layer Security) provides equivalent security guarantees to TLS (encryption, integrity, and authentication) while operating over UDP datagrams. Because datagrams are independent, lost packets do not stall subsequent sensor metrics, preserving real-time data flow.

### Positive Consequences

* **Elimination of Head-of-Line Blocking:** Dropped datagrams are simply skipped by the receiver, keeping live telemetry stream latency low and predictable.
* **Lower Handshake & Reconnection Overhead:** DTLS 1.3 features optimized handshakes (including 0-RTT resumption) that allow edge devices to reconnect rapidly after total signal dropouts.
* **Equivalent Security Posture:** Uses the same cryptographic primitives, cipher suites, and X.509 certificate validation pipelines as standard TLS.

### Negative Consequences & Trade-offs

* **Unreliable Transport Handling:** The application layer must handle out-of-order packets or missing sequence numbers if specific non-telemetry data requires guaranteed delivery.
* **Path MTU Discovery (PMTU) Complexity:** DTLS record sizes must be strictly managed to avoid IP-level fragmentation, which degrades performance across heterogeneous cellular routes.
* **NAT Timeout Management:** UDP mappings on network NAT devices expire faster than TCP connections, requiring lightweight application-level heartbeats (keep-alives).

---

## Pros and Cons of Options

### Option 1: TLS 1.3 over TCP

* **Good, because** guarantees ordered, reliable byte stream delivery without application-layer sequencing logic.
* **Good, because** widespread native library support across all languages, OSs, and middleboxes/firewalls.
* **Bad, because** TCP retransmission and congestion control stall the entire stream during packet loss (head-of-line blocking).
* **Bad, because** retransmitting outdated sensor values wastes precious satellite bandwidth when only the latest metric matters.

### Option 2: DTLS 1.3 over UDP

* **Good, because** independent datagram delivery prevents stream freezing on lossy networks.
* **Good, because** provides TLS-grade encryption and mutual authentication specifically designed for datagram transports.
* **Good, because** ideal for time-sensitive, loss-tolerant telemetry streams where fresh data is more valuable than old retransmitted data.
* **Bad, because** requires explicit application logic or higher-level protocols (e.g., CoAP) to handle payload ordering and explicit reliability when needed.
* **Bad, because** some strict corporate firewalls block non-standard UDP traffic by default.

### Option 3: IPSec / WireGuard Tunnel

* **Good, because** secures all IP traffic between edge gateway and cloud at the OS level without modifying application code.
* **Bad, because** adds significant operational complexity managing tunnel states and key distribution across thousands of remote edge devices.
* **Bad, because** tunneling TCP inside an un-tuned encrypted tunnel can exacerbate TCP meltdowns over poor connections.

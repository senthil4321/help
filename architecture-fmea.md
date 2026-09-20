**Failure Mode and Effects Analysis (FMEA)** is a structured, proactive methodology used across engineering, manufacturing, healthcare, and software development to identify potential failure points in a system, assess their business or safety impact, and implement controls before failures occur.

---

## Key Applications of FMEA

### 1. Primary Types

* **Design FMEA (DFMEA):** Applied during product development to analyze component design, material selection, and tolerances before hardware production (e.g., preventing a brake pad from overheating under high loads).
* **Process FMEA (PFMEA):** Applied to manufacturing and assembly lines to spot human errors, machine calibration drifts, or environmental risks (e.g., preventing a torque wrench from under-tightening a critical bolt).
* **System / Concept FMEA (SFMEA):** Evaluates high-level system architecture, cross-component interactions, and subsystem interfaces (e.g., assessing failure paths between a car's battery management system and engine controller).
* **Software FMEA:** Analyzes code routines, API integrations, data corruption paths, and exception-handling routines in mission-critical applications.

### 2. When to Perform an FMEA

* **New Development:** Designing a new product, service, or process from scratch.
* **Modification:** Changing an existing design, substituting raw materials, or altering a manufacturing sequence.
* **Environment Shift:** Deploying an existing product or process in a new operating condition or location.
* **Root Cause Follow-Up:** Following up on severe field failures or customer complaints to prevent repeat issues.
* **Compliance Standards:** Fulfilling industry-mandated safety standards (e.g., **ISO 26262** for automotive functional safety, **ISO 14971** for medical devices, or **IATF 16949** for automotive quality systems).

---

## How FMEA Measures Risk

Every potential failure mode is evaluated against three criteria, typically scored on a **1 to 10 scale**:

1. **Severity (S):** How severe is the impact on the end user or system if the failure occurs? *(1 = Unnoticeable, 10 = Hazardous without warning)*
2. **Occurrence (O):** How frequently is the failure cause expected to happen? *(1 = Extremely unlikely, 10 = Inevitable/Constant)*
3. **Detection (D):** How likely is current testing/inspection to catch the flaw before it reaches the customer? *(1 = Guaranteed detection, 10 = Undetectable)*

### Risk Metrics

Historically, teams calculated a **Risk Priority Number (RPN)**:


$$\text{RPN} = \text{Severity (S)} \times \text{Occurrence (O)} \times \text{Detection (D)}$$

Modern standards (such as the **AIAG-VDA FMEA** standard) favor **Action Priority (AP)** tables, which prioritize **Severity first** to ensure high-hazard risks are mitigated regardless of low occurrence rates.

---

## Example FMEA Analysis Matrix

| Process / Item | Potential Failure Mode | Potential Effect | **S** | Potential Cause | **O** | Current Controls | **D** | **RPN** | Recommended Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Battery Cable Assembly** | Cable connection loose at terminal | Intermittent vehicle electrical failure | **8** | Incorrect torque during assembly | **5** | Visual inspection | **7** | **280** | Install automated shut-off torque wrench with logging. |
| **Medical Pump Software** | Flow rate calculation overruns buffer | Inaccurate medication dosage delivered | **10** | Unhandled floating-point division by zero | **2** | Unit test suite | **4** | **80** | Implement static analysis tooling and strict bounds checking. |

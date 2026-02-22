# Bus Station Management System – Design Diagrams

PlantUML source for the diagrams referenced in **IST607 Group 3 System Design** (aligned with Group II reference document).

| Figure | File | Description |
|--------|------|-------------|
| **Figure 1** | `01-high-level-architecture.puml` | High-level system architecture (Presentation, Application, Data, Integration layers) |
| **Figure 2** | `02-network-topology.puml` | Network topology (hierarchical star: central hub, stations, mobile/remote) |
| **Figure 3** | *(see below)* | Entity Relationship Diagram (ERD) – **see parent folder** `erd-bus-station-management.puml` |
| **Figure 4** | `04-security-layered-defense.puml` | Security design – layered defense model (Physical, Network, Application, Data) |
| **Figure 5** | `05-external-system-integration.puml` | External system integration (Payment Gateway, GPS, SMS, Email) |

## How to generate images

- **VS Code:** Install "PlantUML" extension, open a `.puml` file, then `Alt+D` (or right‑click → Preview).
- **Command line:** `java -jar plantuml.jar diagrams/*.puml` (output in same folder or use `-o`).
- **Online:** Copy content into [plantuml.com](https://www.plantuml.com/plantuml).

## ER diagram (Figure 3)

The ER diagram source is in the parent folder:

- **Source:** `../erd-bus-station-management.puml`
- **Exported image for document:** Save as `03-erd.png` in this `diagrams/` folder so `IST607-Group-3-System-Design.md` can embed it.

## Image files used in the document

`IST607-Group-3-System-Design.md` embeds the diagrams using these paths (place exported PNGs here):

| Figure | Filename |
|--------|----------|
| Figure 1 | `diagrams/01-high-level-architecture.png` |
| Figure 2 | `diagrams/02-network-topology.png` |
| Figure 3 (ERD) | `diagrams/03-erd.png` |
| Figure 4 | `diagrams/04-security-layered-defense.png` |
| Figure 5 | `diagrams/05-external-system-integration.png` |

All diagrams use colors for layers or component types as described in the System Design document.

# CTA Flowing Heatmap (Home → Work → Home) — Network-Based Simulation

This project generates an animated **“flowing” heatmap** over the Chicago CTA rail network. The heat is not a static density map: it **moves along the train lines** as commuters travel from **homes to jobs in the morning** and from **jobs back to homes in the evening**.

> **GIF interpretation**
> - **Colored dots/paths**: CTA rail lines (a simplified network graph).
> - **Heat (yellow → red)**: estimated **passenger presence** on/near the rail corridors at that time step.
> - The animation advances in **15-minute frames**, showing how demand **concentrates and propagates** toward/away from downtown.

---

## Data Sources

We simulate flows using two datasets:

1) **CTA rail stops / station geometry**
- Used to build station nodes and line membership (e.g., `MAP_ID`, line flags, coordinates).
```text
CTA - System Information - List of 'L' Stops (Chicago Data Portal)
https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme


https://github.com/user-attachments/assets/d589c471-f112-4a8e-af58-ac6d27090189



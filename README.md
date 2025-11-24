# NC4 to GeoJSON Converter

A sleek, client-side web application to convert NetCDF4 (`.nc4`) files to GeoJSON directly in your browser. Powered by `h5wasm` and WebAssembly.

## Features
- **Client-Side Processing**: No server required. Your data stays on your device.
- **Sleek UI**: Modern, dark-themed design with a premium feel.
- **Fast**: Uses WebAssembly for high-performance parsing.
- **Data Preview**: Inspect your GeoJSON data before downloading.
- **Smart Output**: Automatically cleans up filenames (e.g., `data.nc4` -> `data.geojson`).

## How to Run Locally
Since this app uses WebAssembly, it must be served over HTTP (not `file://`).

1.  Open a terminal in the project directory.
2.  Run a simple HTTP server:
    ```bash
    python -m http.server 8080
    ```
3.  Open [http://localhost:8080](http://localhost:8080) in your browser.

## Deploying to GitHub Pages
This project is ready for GitHub Pages!

1.  Push this repository to GitHub.
2.  Go to **Settings** > **Pages**.
3.  Under **Source**, select `main` branch and `/` (root) folder.
4.  Click **Save**.
5.  Your site will be live at `https://<username>.github.io/<repo-name>/`.

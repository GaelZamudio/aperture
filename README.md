# Aperture

An open-source tool under development, written in Python, to diagnose networks
and automate the authorized publication of web services without relying on
external tunnels such as ngrok.

## Status

Preparing for version 0.1.0. The command-line entry point supports help and
version output. Diagnostic and publishing features are not implemented yet.
Windows will be the initial platform, and HuellaRed will serve as a future test application.

## First goal

Build read-only network diagnostics, step by step, before implementing
changes to the router or firewall.

Future development will evaluate IPv4, IPv6, NAT, UPnP, PCP, and NAT-PMP to
select authorized publishing strategies, configure the local firewall, and verify
accessibility from the internet. These capabilities are not implemented yet.

Aperture cannot guarantee inbound access on every network. When no authorized
publishing path is available, it should explain the obstacle. It must not bypass
institutional network restrictions.

## Run locally

From the repository root, create a virtual environment once:

```powershell
python -m venv .venv
```

Run Aperture using the environment's Python, without activating it:

```powershell
.\.venv\Scripts\python.exe -m aperture
.\.venv\Scripts\python.exe -m aperture --help
.\.venv\Scripts\python.exe -m aperture --version
```

If the environment is already activated, use `python` instead of the full path.
Running without options displays help. No third-party packages are required.

`pyproject.toml` contains the initial project metadata. Packaging and installation
commands have not been defined yet. For now, the version in `aperture/__init__.py`
must match the version in `pyproject.toml`.

An open-source license will be chosen before distributing the project;
a license file has not been added yet.

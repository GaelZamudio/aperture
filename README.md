# Aperture

An open-source tool under development, written in Python, to diagnose networks
and automate the authorized publication of web services without relying on
external tunnels such as ngrok.

## Status

Preparing for version 0.1.0. Only the initial project configuration exists;
there are no executable commands or diagnostic or publishing features yet.
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

`pyproject.toml` contains the initial project metadata. Packaging, dependencies,
and installation commands have not been defined yet.

An open-source license will be chosen before distributing the project;
a license file has not been added yet.

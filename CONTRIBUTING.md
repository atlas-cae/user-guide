# Contributing to Atlas user-guide

This repository contains user-facing documentation for the Atlas GPU/HPC cluster.

## Contribution workflow

1. Create a branch for your change.
2. Open a pull request into the default branch.
3. Wait for review from the `admins` team.
4. Resolve all review comments before merge.

Do not push directly to the default branch.

## Branch naming

Use lowercase, hyphen-separated names with one of these prefixes:

- `docs/<short-description>`
- `fix/<short-description>`

Examples:

- `docs/submitting-jobs`
- `fix/cuda-example-command`

## File naming

Use lowercase, hyphen-separated names. Do not use spaces.

Good:

- `submitting-first-job.md`
- `using-containers.md`

Bad:

- `Submitting First Job.md`
- `final_version.md`
- `notes2.md`

## Markdown conventions

- Use one `#` H1 heading per file.
- Use clear section headings.
- Prefer short sections over long unstructured pages.
- Use fenced code blocks for commands.
- Mark shell commands with `bash` when useful.

## Security rule

Never commit secrets, passwords, tokens, private keys, MUNGE keys, database credentials, VPN credentials, or internal credentials.

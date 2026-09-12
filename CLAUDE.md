# Project rules for Claude Code

This is a fork of [arsenetar/dupeguru](https://github.com/arsenetar/dupeguru). Work done here is
meant to be contributed upstream, so anything pushed to a repository is read by people outside this
account.

## Never publish session links

Never put a Claude Code session link (`https://claude.ai/code/session_...`) in anything pushed to a
repository or posted to GitHub: commit messages (including a `Claude-Session:` trailer), pull
request titles and bodies, issue and review comments, or code comments. Those links are private and
never resolve for anyone else, so they are dead links for every reader. Keep them in chat replies
only.

A `Co-Authored-By:` trailer and the public https://claude.com/claude-code link are fine.

## Contribution branches

Cut branches meant for an upstream pull request from upstream `master` rather than from this fork's
`master`. This file lives on the fork's `master` only and should never show up in an upstream diff.

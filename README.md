# requeue-cimpler-jobs

Easily requeue all your [cimpler] jobs.

## Motivation

Sometimes all our CI builds fail because we've broken something in the
infrastructure or we accidentally merged something into master that breaks the
tests.  After we fix the problem, we'd like to rerun all our CI builds to get
useful information on the branches.

We used to have a little PHP-and-curl script that did this, but it did manual
header parsing and didn't support 2FA, and really wasn't more than a quick
hack.  This is a slightly less quick hack that leverages other people's hard
work.

[cimpler]: https://github.com/danielbeardsley/cimpler


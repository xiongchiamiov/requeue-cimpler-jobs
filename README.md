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

## Installation

    [$]> pip install requeue-cimpler-jobs

or

    [$]> easy_install requeue-cimpler-jobs

## Hacking

I highly recommend using virtualenv:

    [$]> virtualenv --no-site-packages --distribute env
    [$]> source env/bin/activate
    [$]> pip install -r requirements.txt
    [$]> pip install -e . # So we can import the version from inside bin/ .

[cimpler]: https://github.com/danielbeardsley/cimpler


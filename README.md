# python-web-stub

Barebones stub for web python projects

## Motivations

I wanted to be able to quickly spin up a containerized web server to test some ideas out.

## Choice of Technology

### python

Really easy and comfortable language to quickly prototype ideas in.  If performance is ever an issue, I can always use FFI out to C/C++/Rust

### docker

The defacto containerization library afaik.  I don't want to pollute my laptop with environments and libraries so this was an obvious initial choice

### Tornado

I wanted a library that's lighter than django and heavier than flask.  Tornado seems like a cool project with a focus on concurrency and async io

### Postgres

Pretty robust database, I'd rather have a full featured production db than to start with sqlite and regret it later

# pwn-schema

A simple example Elastic schema for red team tools to leverage for collaboration 
without coordination. 

### About the Project

Competitive Red Team events often have multiple users leveraging multiple C2s
to perform engagement activities. Instead of trying to talk someone out of using 
their favorite C2 framework, pwn-schema focuses on having a common logging schema
so you can know who has what where.


## Setting up a Dev Environment
### PwnSchema - Setting up a Local ELK Env

0. Expand amount of virtual memory for processes
```
sudo sysctl -w vm.max_map_count=262144
```

1. ensure docker & docker-compose are installed.

2. Bring up the local instance
```
docker-compose up -d 
```
*Note, this listens on all interfaces*

3. Access Kibana locally (http://localhost:5601)

4. Add mapping to PWN interface
* Use dev tools or the bash script.


### Ingest Fake Data
0. install requirements.txt
```
pip3 install -r ./schema-tools/requirements.txt
```

1. python3 ./schema-tools/gen_pwn_data.py
*This runs in an infinite loop to populate data between November 13th and November 15th*


## Shipping Real Logs
0. Modify your C2 framework to log data to a CSV
1. Leverage filebeat to ship to a central Elastic server.

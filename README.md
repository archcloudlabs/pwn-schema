# pwn-schema
PWN Schema for ELK

### PwnSchema - Local ELK Env

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

5. Use dev tools or the bash script


### Ingest Fake Data
0. install requirements.txt
```
pip3 install -r requirements.txt
```

1. python3 gen_pwn_data.py

### Basic C2 Artifacts

Regardless of what C2 framework you're using, the following content is required
for pwn-schema:

0. Timestamp
1. IP_Addr
2. Agent's PID
3. User agent's is running as
4. Agent name
5. Red Team operator responsible for that C2 framework


Example can be seen below:
```
{
	'@timestamp': 2020-11-13 13:36:06,
	'Host': 'PfSense',
	'IPv4': '10.0.0.11',
	'Agent': 'molevar',
	'Proc': 'bind',
	'PID': 48911,
	'operator': 'user_4'
}
```

CSV output is prefered for shipping data via filebeat. However JSON is also accepted via filebeat.

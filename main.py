import toml
import sys

file = "alert_example.toml"
present_fields = []
missing_fields = []

with open(file) as t:
    alert = toml.load(t)

if alert['rule']['type'] == "query":
    required_fields = ['author', 'description', 'from', 'name', 'note', 'references', 'risk_score', 'rule_id', 'severity', 'tags', 'type', 'query']
elif alert['rule']['type'] == "eql":
    required_fields = ['author', 'description', 'from', 'name', 'note', 'references', 'risk_score', 'rule_id', 'severity', 'tags', 'type', 'query', 'language']
elif alert['rule']['type'] == "threshold":
    required_fields = ['author', 'description', 'from', 'name', 'note', 'references', 'risk_score', 'rule_id', 'severity', 'tags', 'type', 'query', 'threshold']


for table in alert:
    for field in alert[table]:
        present_fields.append(field)

for i in required_fields:
    if i not in present_fields:
        missing_fields.append(i)

if missing_fields:
    for f in missing_fields:
        print(f"Missing {f} field")
else:
        print("All fields present")

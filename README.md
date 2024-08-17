# Sample application using kafka and zookeeper

### Prerequisites
- Docker
- Python >= 3

### Execution
- `cd kafka-zooker`
- Create virtual environment using `python3 -m venv venv`
- `source venv/bin/activate`
- `docker compose up -d`
- `pip install -r requirements.txt`
- `python producer.py`
- `python consumer.py`


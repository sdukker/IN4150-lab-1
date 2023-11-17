NUM_NODES=4
NUM_CONS=2
python3 src/util.py $NUM_NODES $NUM_CONS topologies/election.yaml election
#docker compose build   # do this manually
docker compose up --build
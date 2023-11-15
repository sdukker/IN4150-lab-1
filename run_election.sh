NUM_NODES=6
NUM_CONS=3
python3 src/util.py $NUM_NODES $NUM_CONS topologies/election.yaml election
#docker compose build   # do this manually
docker compose up
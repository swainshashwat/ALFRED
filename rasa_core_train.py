# importing the packages
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.agent import Agent

# setting the Agent
agent = Agent('data/domain.yml', policies=[KerasPolicy()])

# loading training dialogues
training_data = agent.load_data('data/stories.md')
agent.train(
        training_data,
        validation_split=0.0,
        epochs=200
        )
agent.persist('models/dialogue')

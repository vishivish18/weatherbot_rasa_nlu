from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUConfig(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')


def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/weathernlu', RasaNLUConfig('config_sapcy.json'))
	print(interpreter.parse(u"I am planning a trip to NewYork, is it the right weather?"))



if __name__  == "__main__":
	#train_nlu('./data/data.json','./config_sapcy.json','./models/nlu')
	run_nlu();



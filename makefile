train_model:
	cd train_model
	python prepare_dateset.py
	# rm pickled/embedded_vector_map.p
	python prepare_embedding_senses.py
	cd ../

deploy_model:
	cp -a train_model/bert_model/. emoprint/bert_model/
	cp train_model/pickled/embedded_vector_map.p emoprint/pickled/embedded_vector_map.p

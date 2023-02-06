# @see http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help

.PHONY: help launch-api-tests lint-python

help: ## provides cli help for this makefile (default) 📖
        @grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


construire-image-airflow: ## 🛠 Création de l'image docker Airflow
	docker build -t airflow:python3.10 .

lancer-airflow: ## ▶️ Lancer airflow sous docker compose sans mode détacher
	docker compose up


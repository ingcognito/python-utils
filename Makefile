PROJECT_NAME=PYTHON-UTILS

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

qrcode: ## Creates a QR code based off string
	python ./qr-code/qr-code.py

#!/bin/bash

apt-get update -y

apt-get install -y wget unzip chromium-browser chromium-driver

chromium-browser --version
chromedriver --version
#!/usr/bin/env bash

modelPackageName=$(head -1 src/main/java/com/mymodel/h2o/FraudDetectionModel.java)
if [ "$modelPackageName" != "package com.mymodel.h2o;" ]
then
  echo 'package com.mymodel.h2o;' | cat - src/main/java/com/mymodel/h2o/FraudDetectionModel.java > temp && mv temp src/main/java/com/mymodel/h2o/FraudDetectionModel.java
  rm -rf temp
fi
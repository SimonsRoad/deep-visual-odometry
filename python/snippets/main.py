#!/usr/local/lib/python3.5/dist-packages
import sys
import json
import formatData

netNum = '3'
sys.path.append('/home/sexy/source/deep-visual-odometry/models/alexnet_inspired/alexNet_'+netNum) #IDK if this works; directories were 'organized'.
from alexNet_3 import run_model, create_model

Xtr, Ytr, Xte, Yte = formatData.knownEnv(formatData.load_data(),formatData.load_poses(), training_ratio=(8/10.0))

#run = 0 
#score, history = run_model(create_model(), Xtr, Ytr, Xte, Yte, "/home/sexy/source/deep-visual-odometry/models/alexNet_"+netNum+"/train_"+str(run)+".h5")
#with open("/home/sexy/source/deep-visual-odometry/models/alexNet_"+netNum+"/history_"+str(run)+".json", 'w') as f:
#	json.dump(score, f, indent=4)
#	json.dump(history, f, indent=4)

run = 5
score, history = run_model(create_model(), Xtr, Ytr, Xte, Yte, "/home/sexy/source/deep-visual-odometry/models/alexNet_"+netNum+"/train_"+str(run)+".h5")
with open("/home/sexy/source/deep-visual-odometry/models/alexNet_"+netNum+"/history_"+str(run)+".json", 'w') as f:
	json.dump(score, f, indent=4)
	json.dump(history, f, indent=4)

run = 6
score, history = run_model(create_model(), Xtr, Ytr, Xte, Yte, "/home/sexy/source/deep-visual-odometry/models/alexNet_"+netNum+"/train_"+str(run)+".h5")
with open("/home/sexy/source/deep-visual-odometry/models/alexNet_"+netNum+"/history_"+str(run)+".json", 'w') as f:
	json.dump(score, f, indent=4)
	json.dump(history, f, indent=4)

run = 7
score, history = run_model(create_model(), Xtr, Ytr, Xte, Yte, "/home/sexy/source/deep-visual-odometry/models/alexNet_"+netNum+"/train_"+str(run)+".h5")
with open("/home/sexy/source/deep-visual-odometry/models/alexNet_"+netNum+"/history_"+str(run)+".json", 'w') as f:
	json.dump(score, f, indent=4)
	json.dump(history, f, indent=4)

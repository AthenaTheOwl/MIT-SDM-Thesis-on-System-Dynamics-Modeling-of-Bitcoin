#MIT SDM Thesis on System Dynamics Modeling of Bitcoin
 All model files required to replicate the results from Vignesh's SDM program thesis at MIT. The project was advised by Prof Hazhir Rahmandad.

Vignesh can be reached at vigneshg@mit.edu.

Refer to 'Thesis Submission Folder' for the initial committed version of the model and its support files. This was the state of the work at the point of the submission of the thesis report, on the week of May 6, 2022.

Inside this, there are the following files:

1. thesis_checkpoint.mdl
This file can be opened with Vensim DSS. At the time of publishing this, the version in use was 9.2.4.

2. bitcoin_demand.voc and bitcoin2.voc
These are the calibration control files used to calibrate the production and market sides using Vensim's calibration engine.

3. demand_side_calibration.out and supply_side_calibration.out
These are the results of the calibration from the running it using the .voc files referenced earlier. These need to be applied in the model before simulation.

4. DataPull.py
A simple python script file that was used to pull the data from the blockchain.com APIs to serve as exogenous inputs to the model. This can be rerun to update the csv files in the DataFiles/ folder.

5. DataFiles folder contains multiple .csv files and a ConsolidatedData.vdfx file
The individual .csv files containing data pulled from the blockchain.com API with the py script referenced earlier are consolidated in the ConsolidatedData.csv file. This consolidated file was then imported into Vensim's native vdfx file format. The vdfx file needs to be loaded for the model to run. If there is a need to update the data, rerun the py script, to update the csv files, and import the new csv file into Vensim to convert it into a vdfx file.

6. demand_side_calibration.rep and supply_side_calibration.rep
The report files from Vensim's calibration run for each sector of the model are also uploaded. Refer to it for details like the RSquared, MAPE and MSE of the data fit.
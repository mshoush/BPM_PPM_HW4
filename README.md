# BPM_PPM_HW4
This project is a solution for [Homework4](https://courses.cs.ut.ee/2021/pm/spring/uploads/Main/2021Homework4.pdf) of the [Business Process Mining course](https://courses.cs.ut.ee/2021/pm/spring/Main/HomePage) at the [University of Tartu, Estonia](https://cs.ut.ee/et). 

# Dataset: 

* [turnaround_anon_sla.csv](http://kodu.ut.ee/~chavez85/pm_course/data/turnaround_anon_sla.csv)

# Reproduce results:
                  
* To reproduce results for this project you need to go inside the corresponding folder, and then run the following commands: 

    1. Data Preprocessing:
          
                                run the notebook "HW4" inside the preprocessing folder
                               
    2. Hyperparameter optimization: go to the experiments folder and run the below command.
      
                                python optimize_params.py turnaround_anon_sla param_dir_mahmoud 1  cluster index xgboost 
                                
    2. Training and evaluating final models: go to the experiments folder and run the below command.
      
                                python experiments.py turnaround_anon_sla param_dir_mahmoud results_dir_mahmoud cluster index xgboost 1 10 4
                                
    

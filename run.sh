#train
python src/run.py train --data_dir dataset/all  \
-sp checkpoints/Gaze -bs 128 -gpu 0,1,2,3 --save_dir 'checkpoints/Gaze/'

#interpolation
python src/run.py test_selected_curve -mp checkpoints/Gaze \
-sp checkpoints/Gaze/test/ --test_selected_curve shared_parser_test

#redirection
python src/run.py attribute_manipulation -mp checkpoints/Gaze \
-sp checkpoints/Gaze/test/  --filter_target_attr 0P -s 1 --branch_idx 0 --n_ref 1 -bs 1

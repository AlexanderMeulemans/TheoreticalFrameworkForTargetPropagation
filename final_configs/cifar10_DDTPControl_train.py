config = {
'lr': 7.451027319970142e-05,
'target_stepsize': 0.05033488616277834,
'feedback_wd': 9.962175900574956e-06,
'beta1': 0.9,
'beta2': 0.9,
'epsilon': 1.3331154348641842e-07,
'lr_fb': 0.0001229329469994943,
'sigma': 0.061738339504955775,
'beta1_fb': 0.9,
'beta2_fb': 0.99,
'epsilon_fb': 9.232258905602834e-06,
'out_dir': 'logs/cifar/DDTPControl_train',
'network_type': 'DDTPControl',
'recurrent_input': False,
'hidden_fb_activation': 'linear',
'size_mlp_fb': None,
'fb_activation': 'linear',
'initialization': 'xavier_normal',
'dataset': 'cifar10',
'optimizer': 'Adam',
'optimizer_fb': 'Adam',
'momentum': 0.0,
'parallel': True,
'normalize_lr': True,
'batch_size': 128,
'forward_wd': 0.0,
'epochs_fb': 10,
'not_randomized': True,
'not_randomized_fb': True,
'extra_fb_minibatches': 0,
'extra_fb_epochs': 2,
'epochs': 100,
'double_precision': True,
'no_val_set': True,
'num_hidden': 3,
'size_hidden': 1024,
'size_input': 3072,
'size_output': 10,
'hidden_activation': 'tanh',
'output_activation': 'softmax',
'no_bias': False,
'no_cuda': False,
'random_seed': 42,
'cuda_deterministic': False,
'freeze_BPlayers': False,
'multiple_hpsearch': False,
'save_logs': False,
'save_BP_angle': False,
'save_GN_angle': False,
'save_GN_activations_angle': False,
'save_BP_activations_angle': False,
'gn_damping': 0.0,
'hpsearch': False,
'log_interval': 80,
}
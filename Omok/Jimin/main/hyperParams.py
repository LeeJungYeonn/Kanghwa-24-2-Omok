N_KERNEL = 128
N_RESIDUAL_BLOCK = 16

BATCH_SIZE = 20 # 128
EPOCHS = 200

LEARNING_RATE = 0.001
LEARN_DECAY = 0.5
LEARN_EPOCH = 50

TEMP_DISCOUNT = 0.9995
SP_GAME_COUNT = 20 # 500
SP_TEMPERATURE = 1.0  # 볼츠만 분포의 온도 파라미터

PV_EVALUATE_COUNT = 20 # 1600

EVAL_GAME_COUNT = 20  # 평가 1회 당 게임 수(오리지널: 400)
EVAL_TEMPERATURE = 1.0  # 볼츠만 분포 온도 파라미터 

hyper_params = f'''
N_KERNEL = {N_KERNEL}
N_RESIDUAL_BLOCK = {N_RESIDUAL_BLOCK}

BATCH_SIZE = {BATCH_SIZE}
EPOCHS = {EPOCHS}

LEARNING_RATE = {LEARNING_RATE}
LEARN_DECAY = {LEARN_DECAY}
LEARN_EPOCH = {LEARN_EPOCH}

TEMP_DISCOUNT = {TEMP_DISCOUNT}
SP_GAME_COUNT = {SP_GAME_COUNT}
SP_TEMPERATURE = {SP_TEMPERATURE}

PV_EVALUATE_COUNT = {PV_EVALUATE_COUNT}

EVAL_GAME_COUNT = {EVAL_GAME_COUNT}
EVAL_TEMPERATURE = {EVAL_TEMPERATURE}
'''
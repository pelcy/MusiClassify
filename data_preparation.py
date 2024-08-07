import numpy as np
import librosa

# GTZANの音楽ファイルとラベルを作成。訓練データとテストデータに分けて返す関数
def gtzan_preparation(genres_path, testdata_num, random_seed=0):

    # ジャンルのリスト
    genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

    # 音楽ファイル名の作成
    gtzan_filenames = list()
    for genre in genres:
        for i in range(100):
            gtzan_filenames.append(f'{genres_path}/{genre}/{genre}.000{i:02}.wav')
    gtzan_filenames = np.asarray(gtzan_filenames)

    # ラベルの作成
    gtzan_labels = list()
    for i in range(10):
        for j in range(100):
            gtzan_labels.append(tf.one_hot(i, 10))
            
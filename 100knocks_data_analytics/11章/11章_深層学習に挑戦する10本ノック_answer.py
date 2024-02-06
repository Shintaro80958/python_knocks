# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% id="Ggab86bxa5zy" colab={"base_uri": "https://localhost:8080/"} outputId="af0c3a5e-4f13-440f-ebe7-066bc02c5842"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="buTLEYXHhA_6"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/11章') #ここを変更。

# %% [markdown] id="tIPfsEyjgiuX"
# # 11章　深層学習に挑戦する10本ノック
# ここでは、深層学習を学ぶうえで必要なプログラムを実行していく流れを学んでいきます。

# %% [markdown] id="yQk7qjQDgiuX"
# ### 放課後ノック101：深層学習に必要なデータを準備しよう

# %% id="EPclN4iJEC9D"
from tensorflow.keras import datasets, layers, models
import numpy as np

# %% [markdown] id="ZlYnr8W4B_ep"
# ### データを読み込んでみよう

# %% id="Yf_s5y7sBjVm" colab={"base_uri": "https://localhost:8080/"} outputId="5a4a7800-5265-4ed8-876a-b26d694676c0"
# 学習用データ/検証用データの読み込み
mnist = datasets.mnist
(X_train, y_train),(X_test, y_test) = mnist.load_data()

# %% [markdown] id="LYD3v9NdKjja"
# ### データを確認しよう

# %% id="rpOEx4H9B5d6" colab={"base_uri": "https://localhost:8080/"} outputId="add4eb50-3420-43b8-d298-0050b5e594f2"
# 形状の出力
print(X_train.shape)
print(X_test.shape)

# %% id="w8iMJZlZCOmm" colab={"base_uri": "https://localhost:8080/"} outputId="3a41dba9-8d28-450a-bf79-0e44e50e14c8"
# 0番目のデータの形状の出力
X_train[0].shape

# %% id="V6cF37hMEruO" colab={"base_uri": "https://localhost:8080/"} outputId="2b5ccbae-194e-4e10-b2a0-ab9505a2d346"
# 0番目のデータの出力
X_train[0]

# %% id="_Y9STzkzEeWq" colab={"base_uri": "https://localhost:8080/", "height": 45} outputId="16bbc067-1da3-4599-c82b-8f23b58561e0"
# 0番目のデータの表示
from google.colab.patches import cv2_imshow
cv2_imshow(X_train[0])

# %% id="7xB4aVz2Emjo" colab={"base_uri": "https://localhost:8080/"} outputId="2b1a7350-c460-4224-ec09-977b711aa001"
# 正解データの出力
y_train[0]

# %% [markdown] id="e1uozuVUFpbz"
# ### データを準備しよう

# %% id="E4it4lD4Flj0"
# データを0から1の範囲に収めるために255で割る
X_train_sc, X_test_sc = X_train / 255.0, X_test / 255.0

# %% id="9zOWf_aiFlm2"
# 形状を整える
X_train_sc = X_train_sc.reshape((60000, 28, 28, 1))
X_test_sc = X_test_sc.reshape((10000, 28, 28, 1))

# %% [markdown] id="Rb_rHk92Cut0"
# ### 放課後ノック102：深層学習モデルを構築しよう

# %% [markdown] id="bsIAbTXiLIIm"
# ### ニューラルネットワークモデルを定義しよう

# %% id="SCjUD0AEHrzA"
model1 = models.Sequential()
model1.add(layers.Flatten(input_shape=(28, 28)))
model1.add(layers.Dense(512, activation='relu'))
model1.add(layers.Dropout(0.2))
model1.add(layers.Dense(10, activation='softmax'))

# %% id="AJtFKA6OIq0x" colab={"base_uri": "https://localhost:8080/"} outputId="332dbfe1-2abd-4a53-e785-f3e196b17cb0"
model1.summary()

# %% [markdown] id="EG_BP8XhLNUx"
# ### CNNモデルを定義しよう

# %% id="UX_YasFwCuV6"
model2 = models.Sequential()
model2.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model2.add(layers.MaxPooling2D((2, 2)))
model2.add(layers.Conv2D(64, (3, 3), activation='relu'))
model2.add(layers.MaxPooling2D((2, 2)))
model2.add(layers.Conv2D(64, (3, 3), activation='relu'))

model2.add(layers.Flatten())
model2.add(layers.Dense(64, activation='relu'))
model2.add(layers.Dense(10, activation='softmax'))

# %% id="qRfIvakXDWT3" colab={"base_uri": "https://localhost:8080/"} outputId="9560bfa6-4544-4e9c-ae9c-392cba3a4811"
model2.summary()

# %% [markdown] id="9QPT0NxULbcP"
# ### ニューラルネットワークモデルを構築しよう

# %% id="Sy0dI8PFDYfg" colab={"base_uri": "https://localhost:8080/"} outputId="cb85d12d-2adf-4e89-dece-b6cc48f61119"
model1.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model1.fit(X_train_sc, y_train, epochs=10)

# %% [markdown] id="Y78F7NLJLh6s"
# ### CNNモデルを構築しよう

# %% id="lnYJX0G8I0BC" colab={"base_uri": "https://localhost:8080/"} outputId="121832ce-faf7-4db1-e6e9-7981347c70fa"
model2.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model2.fit(X_train_sc, y_train, epochs=10)

# %% [markdown] id="5yvrKBWjIYlI"
# ### 放課後ノック103：モデルの評価をしてみよう

# %% id="aA8W7V7tFQLC" colab={"base_uri": "https://localhost:8080/"} outputId="1fc16c18-cb3c-4670-ad96-cee460fc24cb"
# モデル１の正解率の出力
model1_test_loss, model1_test_acc = model1.evaluate(X_test_sc, y_test)
print(model1_test_acc)

# %% id="V6yq8QWeGaGo" colab={"base_uri": "https://localhost:8080/"} outputId="e2875041-5b4d-4c20-e610-e724300b4114"
# モデル２の正解率の出力
model2_test_loss, model2_test_acc = model2.evaluate(X_test_sc, y_test)
print(model2_test_acc)

# %% [markdown] id="AJEmYkbeMWe0"
# ### 放課後ノック104：モデルを使った予測をしてみよう

# %% id="hEajnTfDKEZu"
# 予測の実行
predictions = model2.predict(X_train_sc)

# %% id="p-VZIi18KfqY" colab={"base_uri": "https://localhost:8080/"} outputId="51e0db82-cba9-4463-9e80-95d3f604f028"
# 予測結果の形状の出力
predictions.shape

# %% id="4LANj-i-WQoF" colab={"base_uri": "https://localhost:8080/"} outputId="c4752d1d-a493-49f9-bcf1-6927e0c54aa2"
predictions

# %% id="ricZ2KjHKitr" colab={"base_uri": "https://localhost:8080/"} outputId="9e967c80-4fed-4e82-d76d-ab08c56f1dd1"
# 0番目の出力
predictions[0]

# %% id="URUMqxERKmGj" colab={"base_uri": "https://localhost:8080/"} outputId="261fe339-2b03-46a7-ab34-4d35130dfd74"
# 最も高い確率の数字の出力
np.argmax(predictions[0])

# %% id="Cgo4mdhmrJao" colab={"base_uri": "https://localhost:8080/"} outputId="0ebba652-30a0-462d-e256-cf9c2291b499"
y_train[0]

# %% [markdown] id="UpmS7--w4YZF"
# ### 放課後ノック105：物体検出YOLOを使って人の検出を行ってみよう

# %% [markdown] id="Eb7OfRtBvKUC"
# ### YOLOの準備

# %% id="FAKvqj2XnQj-" colab={"base_uri": "https://localhost:8080/"} outputId="18b955ef-899c-4049-b27c-677336f8f5f1"
#yolov3-tf2のダウンロード
# !git clone https://github.com/zzh8829/yolov3-tf2.git ./yolov3_tf2
# %cd ./yolov3_tf2
# !git checkout c43df87d8582699aea8e9768b4ebe8d7fe1c6b4c
# %cd ../

# %% id="k5BjFMFnn7Za" colab={"base_uri": "https://localhost:8080/"} outputId="d242cd6a-60c1-4d60-8374-08c1db4c2817"
#YOLOの学習済みモデルのダウンロード
# !wget https://pjreddie.com/media/files/yolov3-tiny.weights 

# %% id="eByPqawwoVc7" colab={"base_uri": "https://localhost:8080/"} outputId="01836127-74d7-43ee-c16d-7927b66c2ebe"
#ダウンロードしたYOLOの学習済みモデルをKerasから利用出来る形に変換
# !python ./yolov3_tf2/convert.py --weights ./yolov3-tiny.weights --output  ./yolov3_tf2/checkpoints/yolov3-tiny.tf --tiny

# %% [markdown] id="DKPYmAp-wvtJ"
# ### YOLOによる物体検出の実行

# %% id="_Hp9rZ5q1Iay" colab={"base_uri": "https://localhost:8080/"} outputId="3507f48a-bfeb-4132-928a-8b34985d3071"
from absl import app, logging, flags
from absl.flags import FLAGS
app._run_init(['yolov3'], app.parse_flags_with_usage)

# %% id="R2bBDwf61Ip8" colab={"base_uri": "https://localhost:8080/"} outputId="311159b3-6edb-4bd4-8fd0-a2acf4410747"
#学習済みの重みをそのまま利用する場合
from  yolov3_tf2.yolov3_tf2.models import  YoloV3Tiny, YoloLoss
import tensorflow as tf
from yolov3_tf2.yolov3_tf2.dataset import transform_images
from yolov3_tf2.yolov3_tf2.utils import draw_outputs
import numpy as np

FLAGS.yolo_iou_threshold = 0.5
FLAGS.yolo_score_threshold = 0.5

yolo_class_names = [c.strip() for c in open("./yolov3_tf2/data/coco.names").readlines()]

yolo = YoloV3Tiny(classes=80)
#重みの読み込み
yolo.load_weights("./yolov3_tf2/checkpoints/yolov3-tiny.tf").expect_partial()

# %% id="J0_NTn0P_VWC"
img_filename = "img/img01.jpg"
img_rawP = tf.image.decode_jpeg(open(img_filename, 'rb').read(), channels=3)
data_shape=(256,256,3)
img_yoloP = transform_images(img_rawP, data_shape[0])
img_yoloP = np.expand_dims(img_yoloP, 0)
#予測開始
boxes, scores, classes, nums = yolo.predict(img_yoloP)

# %% [markdown] id="ZS5abmZ7xBQ_"
# ### 結果の出力

# %% id="rpFo8yPt_dte" colab={"base_uri": "https://localhost:8080/", "height": 449} outputId="c00b9cfa-bff7-4e92-c7ec-ce60967ae2c6"
import matplotlib.pyplot as plt

img_yoloP = img_rawP.numpy()
img_yoloP = draw_outputs(img_yoloP, (boxes, scores, classes, nums), yolo_class_names)

plt.figure(figsize=(10,10))
plt.imshow(img_yoloP)
plt.axis('off')
plt.show()

# %% [markdown] id="WFl2r6FDt_P1"
# ### 放課後ノック106：YOLOの学習を行うための準備をしよう

# %% [markdown] id="XCWodp_mxrvG"
# ### 学習データのダウンロード

# %% id="g_sBaX_5nJBz" colab={"base_uri": "https://localhost:8080/"} outputId="412645f2-65fa-429f-aab8-15e10f3d5f0e"
#データセットのダウンロード及び解凍を行います。
#ダウンロード済みでない場合以下を実行して下さい。
# !wget http://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
# !tar -xvf ./VOCtrainval_06-Nov-2007.tar

# %% [markdown] id="zim5JC_jxviJ"
# ### 学習データの確認

# %% id="ZRSb05V_ryGC" colab={"base_uri": "https://localhost:8080/", "height": 349} outputId="6f743502-cf8e-4fab-e4c5-88bb423c9a5b"
from PIL import Image

#ダウンロードしたデータセットの画像の内１枚を表示
Image.open("./VOCdevkit/VOC2007/JPEGImages/006626.jpg")

# %% id="-7-aAtnWryIi" colab={"base_uri": "https://localhost:8080/"} outputId="7bc51ef3-92d2-426f-aa9c-0f79361724f3"
#表示した画像のアノテーションデータの表示
annotation = open("./VOCdevkit/VOC2007/Annotations/006626.xml").read()
print(annotation)

# %% [markdown] id="8WeCtG4VxkEZ"
# ### 放課後ノック107：新たな学習データを使ってYOLOの学習モデルを生成してみよう

# %% [markdown] id="scd8ku8ix3-n"
# ### ライブラリのインストール

# %% id="19AfE-oBoywW" colab={"base_uri": "https://localhost:8080/"} outputId="fd258641-b679-4acb-bc96-ca986950dfd9"
# !pip install xmltodict

# %% [markdown] id="t2E8AJvSx7a8"
# ### 学習データの変換

# %% id="jLnLblWMqm2p"
import xmltodict
import numpy as np
from tensorflow.keras.utils import Sequence
import math
import yolov3_tf2.yolov3_tf2.dataset as dataset

yolo_max_boxes = 100

#アノテーションデータの変換
def parse_annotation(annotation, class_map):
    label = []
    width = int(annotation['size']['width'])
    height = int(annotation['size']['height'])
    
    if 'object' in annotation:
        if type(annotation['object']) != list:
            tmp = [annotation['object']]
        else:
            tmp = annotation['object']
            
        for obj in tmp:
            _tmp = []
            _tmp.append(float(obj['bndbox']['xmin']) / width)
            _tmp.append(float(obj['bndbox']['ymin']) / height)
            _tmp.append(float(obj['bndbox']['xmax']) / width)
            _tmp.append(float(obj['bndbox']['ymax']) / height)
            _tmp.append(class_map[obj['name']])
            label.append(_tmp)

    for _ in range(yolo_max_boxes - len(label)):
      label.append([0,0,0,0,0])
    return label


# %% [markdown] id="F-xxvU37yPJZ"
# ### 学習データ読み込みクラスの定義

# %% id="QlyQ5j_PoXPa"
from yolov3_tf2.yolov3_tf2.dataset import transform_images

#学習時に画像データを必要な分だけ読み込むためのクラス
class ImageDataSequence(Sequence):
    def __init__(self, file_name_list, batch_size,  anchors, anchor_masks, class_names, data_shape=(256,256,3)):
        
        #クラス名とそれに対応する数値、という形の辞書を作る
        self.class_map = {name: idx for idx, name in enumerate(class_names)}
        self.file_name_list = file_name_list

        self.image_file_name_list = ["./VOCdevkit/VOC2007/JPEGImages/"+image_path + ".jpg" for image_path in self.file_name_list]
        self.annotation_file_name_list = ['./VOCdevkit/VOC2007/Annotations/' + image_path+ ".xml" for image_path in self.file_name_list]

        self.length = len(self.file_name_list)
        self.data_shape = data_shape
        self.batch_size = batch_size
        self.anchors = anchors
        self.anchor_masks = anchor_masks

        self.labels_cache = [None for i in range(self.__len__())]

    #１バッチごとに自動的に呼ばれる。画像データとそのラベルを必要な分だけ読み込んで返す
    def __getitem__(self, idx):
        images = []
        labels = []
        
        #現在のバッチが何回目か、がidx変数に入っているため、それに対応するデータを読み込む
        for index in range(idx*self.batch_size, (idx+1)*self.batch_size):

          #アノテーションデータをラベルとして使える形に変換する
          annotation = xmltodict.parse((open(self.annotation_file_name_list[index]).read()))
          label = parse_annotation(annotation["annotation"], self.class_map)
          labels.append(label)

          #画像データの読み込みと加工
          img_raw = tf.image.decode_jpeg(open(self.image_file_name_list[index], 'rb').read(), channels=3)
          img = transform_images(img_raw, self.data_shape[0])
          images.append(img)
        
        #ラベルに対しても前処理をするが、時間がかかるため１度読み込んだらキャッシュとして保存する
        if self.labels_cache[idx] is None:
          labels = tf.convert_to_tensor(labels, tf.float32)
          labels = dataset.transform_targets(labels, self.anchors, self.anchor_masks, self.data_shape[0])
          self.labels_cache[idx] = labels
        else: 
          labels = self.labels_cache[idx]

        images = np.array(images)
        return images, labels

    def __len__(self):
        return math.floor(len(self.file_name_list) / self.batch_size)



# %% [markdown] id="FmImgsydy7QY"
# ### YOLOモデル(ネットワーク)の読み込み

# %% id="pT83GAyExapw"
from  yolov3_tf2.yolov3_tf2.models import  YoloV3Tiny, YoloLoss
from yolov3_tf2.yolov3_tf2.utils import freeze_all
import tensorflow as tf

batch_size=16
data_shape=(416,416,3)
class_names =  ["person", "bird", "cat","cow","dog", "horse","sheep", "aeroplane", "bicycle", "boat", "bus", "car", "motorbike", "train", "bottle", "chair", "diningtable", "pottedplant", "sofa", "tvmonitor"]

anchors = np.array([(10, 14), (23, 27), (37, 58),
                              (81, 82), (135, 169),  (344, 319)],
                             np.float32) / data_shape[0]
anchor_masks = np.array([[3, 4, 5], [0, 1, 2]])

# yolov3_tf2で定義されているtiny YOLOのモデルを読み込む
model_pretrained = YoloV3Tiny(data_shape[0], training=True, classes=80)
model_pretrained.load_weights("./yolov3_tf2/checkpoints/yolov3-tiny.tf").expect_partial()

model = YoloV3Tiny(data_shape[0], training=True, classes=len(class_names))
#ここで、学習済みモデルの出力層以外の重みだけを取り出す
model.get_layer('yolo_darknet').set_weights(model_pretrained.get_layer('yolo_darknet').get_weights())
#出力層以外を学習しないようにする
freeze_all(model.get_layer('yolo_darknet'))

# %% id="7uv8wOy-yJfO" colab={"base_uri": "https://localhost:8080/"} outputId="0efb7811-e607-4cb3-9474-e5dfebbd0f72"
loss = [YoloLoss(anchors[mask], classes=len(class_names)) for mask in anchor_masks]
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001), loss=loss, run_eagerly=False)

#モデルの構造を出力
model.summary()

# %% [markdown] id="UySDjHGW0BHf"
# ### 学習データの読み込み

# %% id="K5xgUKjiyRSQ"
train_file_name_list = open("./VOCdevkit/VOC2007/ImageSets/Main/train.txt").read().splitlines()
validation_file_name_list = open("./VOCdevkit/VOC2007/ImageSets/Main/val.txt").read().splitlines()

train_dataset = ImageDataSequence(train_file_name_list, batch_size, anchors, anchor_masks, class_names, data_shape=data_shape)
validation_dataset = ImageDataSequence(validation_file_name_list, batch_size, anchors, anchor_masks, class_names, data_shape=data_shape)

# %% [markdown] id="PiVSTcSr0ErM"
# ### 学習の実施

# %% id="rQrv-F_YyW6f" colab={"base_uri": "https://localhost:8080/"} outputId="b47ea2f3-3aab-472a-d7f3-76d9beacf63e"
history = model.fit(train_dataset, validation_data=validation_dataset, epochs=1)

# %% id="yHdcPhz_yZXU"
#学習した重みの保存
model.save_weights('./saved_models/model_yolo_weights')

# %% [markdown] id="3OqkGbOW3c6i"
# ### 放課後ノック108：新たに学習させたモデルを使って人の検出を行ってみよう

# %% [markdown] id="cK8VHMiO0zr1"
# ### 学習した重みの読み込み

# %% id="1j2EScKY12gx" colab={"base_uri": "https://localhost:8080/"} outputId="f32d18d3-1ab4-4673-bc8f-93abf20dbe46"
from absl import app, logging, flags
from absl.flags import FLAGS
app._run_init(['yolov3'], app.parse_flags_with_usage)

# %% id="XizpUkI11IdK" colab={"base_uri": "https://localhost:8080/"} outputId="5dfb1e02-cf68-4d0f-b064-6eba7637d600"
import cv2
import numpy as np
import matplotlib.pyplot as plt
from yolov3_tf2.yolov3_tf2.utils import draw_outputs

FLAGS.yolo_iou_threshold = 0.5
FLAGS.yolo_score_threshold = 0.5

yolo_trained = YoloV3Tiny(classes=len(class_names))
#保存した重みの読み込み
yolo_trained.load_weights('./saved_models/model_yolo_weights').expect_partial()

# %% [markdown] id="IdcccUPa03cN"
# ### 物体検出の実行

# %% id="smr62Jkw1Ifq"
img_filename = "img/img01.jpg"

#画像の読み込み
img_rawL = tf.image.decode_jpeg(open(img_filename, 'rb').read(), channels=3)
img_yoloL = transform_images(img_rawL, data_shape[0])
img_yoloL = np.expand_dims(img_yoloL, 0)


#予測開始
boxes, scores, classes, nums = yolo_trained.predict(img_yoloL)

# %% [markdown] id="aDmfgGLI1FkX"
# ### 結果の表示

# %% id="iKiCvBwC1Ih4" colab={"base_uri": "https://localhost:8080/", "height": 449} outputId="0d29d9f2-ec03-45a6-ee2e-91822cf4deae"
img_yoloL = img_rawL.numpy()

#予測結果を画像に書き込み
img_yoloL = draw_outputs(img_yoloL, (boxes, scores, classes, nums), class_names)

#予測結果を書き込んだ画像の表示
plt.figure(figsize=(10,10))
plt.imshow(img_yoloL)
plt.axis('off')
plt.show()

# %% [markdown] id="KMterp_J1cgF"
# ### 放課後ノック109：YOLOとHOGの人の検出結果を比較して深層学習の精度を体感しよう

# %% [markdown] id="44hQiGY623G_"
# ### HOGによる人の検出

# %% id="FKujwzGC1g1k" colab={"base_uri": "https://localhost:8080/", "height": 449} outputId="47688342-0618-47d5-ddb5-1729964a5fbf"
import cv2
from google.colab.patches import cv2_imshow

# 準備 #
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05, 'hitThreshold':0, 'groupThreshold':5}

# 検出 #
img_hog = cv2.imread("img/img01.jpg")
gray = cv2.cvtColor(img_hog, cv2.COLOR_BGR2GRAY)
human, r = hog.detectMultiScale(gray, **hogParams)
if (len(human)>0):
    for (x, y, w, h) in human:
        cv2.rectangle(img_hog, (x, y), (x + w, y + h), (255,255,255), 3)

# 表示 #
img_hog = cv2.cvtColor(img_hog, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.imshow(img_hog)
plt.axis('off')
plt.show()

# %% [markdown] id="8hsy8O-u5t6B"
# ### 結果の比較

# %% id="RIQp-9Oq1g8c" colab={"base_uri": "https://localhost:8080/", "height": 291} outputId="c621480f-535f-402c-fe64-b874b25594eb"
plt.figure(figsize=(30,10))
plt.subplot(1,3,1)
plt.title("YOLO (pre-trained)")
plt.imshow(img_yoloP)
plt.axis('off')
plt.subplot(1,3,2)
plt.title("YOLO (trained)")
plt.imshow(img_yoloL)
plt.axis('off')
plt.subplot(1,3,3)
plt.title("HOG")
plt.imshow(img_hog)
plt.axis('off')
plt.show()

# %% [markdown] id="wGdqlEqWNUYd"
# ### 放課後ノック110：YOLOでの人以外の物体の検出のようすを確認しよう

# %% id="OmVe83TRNlSF" colab={"base_uri": "https://localhost:8080/", "height": 449} outputId="82a4d86d-ffbb-4ef4-b182-43fcfca72960"
img_filename = "img/img02.jpg"

#画像の読み込み
img_rawP = tf.image.decode_jpeg(open(img_filename, 'rb').read(), channels=3)
img_yoloP = transform_images(img_rawP, data_shape[0])
img_yoloP = np.expand_dims(img_yoloP, 0)

#クラス名の読み込み
yolo_class_names = [c.strip() for c in open("./yolov3_tf2/data/coco.names").readlines()]

#予測開始
boxes, scores, classes, nums = yolo.predict(img_yoloP)

#予測結果を画像に書き込み
img_yoloP = img_rawP.numpy()
img_yoloP = draw_outputs(img_yoloP, (boxes, scores, classes, nums), yolo_class_names)

#予測結果を書き込んだ画像の表示
plt.figure(figsize=(10,10))
plt.imshow(img_yoloP)
plt.axis('off')
plt.show()

# %% id="ujbOcDWMNXA7"

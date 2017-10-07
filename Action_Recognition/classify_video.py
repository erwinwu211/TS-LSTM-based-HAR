import heapq
import numpy as np
import glob
caffe_root = '../../'
import sys
sys.path.insert(0,caffe_root + 'python')
import caffe
caffe.set_mode_gpu()
caffe.set_device(0)

#Initialize transformers
def initialize_transformer(image_mean, is_flow):
  shape = (10*16, 3, 227, 227)
  transformer = caffe.io.Transformer({'data': shape})
  channel_mean = np.zeros((3,227,227))
  for channel_index, mean_val in enumerate(image_mean):
    channel_mean[channel_index, ...] = mean_val
  transformer.set_mean('data', channel_mean)
  transformer.set_raw_scale('data', 255)
  transformer.set_channel_swap('data', (2, 1, 0))
  transformer.set_transpose('data', (2, 0, 1))
  return transformer


#classify video with LRCN model
def LRCN_classify_video(frames, net, transformer, is_flow):
 clip_length = 16
 offset = 8
 input_images = []
 for im in frames:
    input_im = caffe.io.load_image(im)
    if (input_im.shape[0] < 240):
      input_im = caffe.io.resize_image(input_im, (240,320))
    input_images.append(input_im)
 vid_length = len(input_images)
 input_data = []
 for i in range(0,vid_length,offset):
    if (i + clip_length) < vid_length:
      input_data.extend(input_images[i:i+clip_length])
    else:  #video may not be divisible by clip_length
      input_data.extend(input_images[-clip_length:])
 output_predictions = np.zeros((len(input_data),101))
 for i in range(0,len(input_data),clip_length):
    clip_input = input_data[i:i+clip_length]
    clip_input = caffe.io.oversample(clip_input,[227,227])
    clip_clip_markers = np.ones((clip_input.shape[0],1,1,1))
    clip_clip_markers[0:10,:,:,:] = 0
#    if is_flow:  #need to negate the values when mirroring
#      clip_input[5:,:,:,0] = 1 - clip_input[5:,:,:,0]
    caffe_in = np.zeros(np.array(clip_input.shape)[[0,3,1,2]], dtype=np.float32)
    for ix, inputs in enumerate(clip_input):
      caffe_in[ix] = transformer.preprocess('data',inputs)
    out = net.forward_all(data=caffe_in, clip_markers=np.array(clip_clip_markers))
    output_predictions[i:i+clip_length] = np.mean(out['probs'],1)
#softmax output
 sm=np.mean(output_predictions,0)
 return heapq.nlargest(5,range(len(sm)),sm.take), sm.tolist()








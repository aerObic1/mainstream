
accuracy_flowers_inception = {14:0.8834,
                              18:0.882,
                              87:0.8807,
                              133:0.8779,
                              165:0.8765,
                              197:0.8697,
                              249:0.8477,
                              280:0.7284,
                              311:0.2606}

accuracy_cats_inception = {18:0.7996,
                           41:0.7984,
                           133:0.7922,
                           197:0.7834,
                           229:0.7809,
                           249:0.7632,
                           280:0.7418,
                           311:0.4836}

accuracy_paris_inception = {133:0.8952,
                            165:0.8832,
                            197:0.8772,
                            229:0.8743,
                            249:0.8653,
                            280:0.7335,
                            311:0.2545}

app_options = [{"accuracies": accuracy_flowers_inception,
                "event_length_ms": 500,
                "correlation": 0.1664,
                "model_path": {
                    0:  "flowers-310-frozen.pb",
                    4:  "flowers-310-frozen.pb",
                    7:  "flowers-310-frozen.pb",
                    10: "flowers-310-frozen.pb",
                    11: "flowers-310-frozen.pb",
                    14: "flowers-310-frozen.pb",
                    17: "flowers-310-frozen.pb",
                    18: "flowers-310-frozen.pb",
                    41: "flowers-310-frozen.pb",
                    64: "flowers-310-frozen.pb",
                    87: "flowers-310-frozen.pb",
                    101:"flowers-310-frozen.pb",
                    133:"flowers-310-frozen.pb",
                    165:"flowers-310-frozen.pb",
                    197:"flowers-310-frozen.pb",
                    229:"flowers-310-frozen.pb",
                    249:"flowers-310-frozen.pb",
                    280:"flowers-310-frozen.pb",
                    311:"flowers-310-frozen.pb"}
                }
               ]

inception_layer_latencies =  [0.0888, 0.0888, 0.0888, 0.0888, 0.1373, 0.1373,
        0.1373, 0.2449, 0.2449, 0.2449, 0.2613, 0.2565, 0.2565, 0.2565, 0.4655,
        0.4655, 0.4655, 0.3402, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201,
        0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201,
        0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.5133,
        0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133,
        0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133,
        0.5133, 0.5133, 0.5133, 0.5133, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973,
        0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973,
        0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973,
        0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.6614,
        0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.9368, 0.9368, 0.9368, 0.9368,
        0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368,
        0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368,
        0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368,
        0.9368, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744,
        0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744,
        0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744,
        0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.9576, 0.9576, 0.9576,
        0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576,
        0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576,
        0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576,
        0.9576, 0.9576, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091,
        0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091,
        0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091,
        0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.9803, 0.9803,
        0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803,
        0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803,
        0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298,
        0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298,
        0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298,
        0.7298, 0.7298, 0.7298, 0.7298, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
        1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
        1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7424, 0.7424, 0.7242]

model_desc = {"total_layers": 314,
              "channels": 1,
              "height": 299,
              "width": 299,
              "layer_latencies": inception_layer_latencies,
              "frozen_layer_names": {1: "input_1",
                                     4: "conv2d_1/convolution",
                                     7: "conv2d_2/convolution",
                                     10: "conv2d_3/convolution",
                                     11: "max_pooling2d_1/MaxPool",
                                     14: "conv2d_4/convolution",
                                     17: "conv2d_5/convolution",
                                     18: "max_pooling2d_2/MaxPool",
                                     41: "mixed0/concat",
                                     64: "mixed1/concat",
                                     87: "mixed2/concat",
                                     101: "mixed3/concat",
                                     133: "mixed4/concat",
                                     165: "mixed5/concat",
                                     197: "mixed6/concat",
                                     229: "mixed7/concat",
                                     249: "mixed8/concat",
                                     280: "mixed9/concat",
                                     311: "mixed10/concat",
                                     314: "dense_2/Softmax:0"}}

video_desc = {"stream_fps": 14}

'''
# Layer latencies with 2 bug fixes. However, gives unstable results.
inception_layer_latencies =  [0.179, 0.179, 0.179, 0.179, 0.3691, 0.3691,
        0.3691, 0.4197, 0.4197, 0.4197, 1.0, 0.0313, 0.0313, 0.0313, 0.5492,
        0.5492, 0.5492, 0.6753, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542,
        0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542,
        0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0607,
        0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607,
        0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607,
        0.0607, 0.0607, 0.0607, 0.0607, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621,
        0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621,
        0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621,
        0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0853,
        0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0352, 0.0352, 0.0352, 0.0352,
        0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352,
        0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352,
        0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352,
        0.0352, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033,
        0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033,
        0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033,
        0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0052, 0.0052, 0.0052,
        0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052,
        0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052,
        0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052,
        0.0052, 0.0052, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087,
        0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087,
        0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087,
        0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0091, 0.0091,
        0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091,
        0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091,
        0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054,
        0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054,
        0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054,
        0.0054, 0.0054, 0.0054, 0.0054, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051,
        0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051,
        0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051,
        0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0509,
        0.0509, 0.0509]
        '''

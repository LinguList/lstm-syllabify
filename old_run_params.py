cnn_optimization_runs = [
    # [name, use_cnn, use_lstm, cnn layers, cnn number filters, cnn filter size, cnn max pool size, dropout, lstm size, embedding size, mini_batch_size, which_rnn, classifier, language]
    [ '1', True, True, 6,  40, 3,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    [ '2', True, True, 2, 100, 3,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    [ '3', True, True, 6, 100, 3,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    [ '4', True, True, 2,  40, 2,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    [ '9', True, True, 2, 100, 2,    4, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['10', True, True, 2, 200, 3,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['11', True, True, 2, 200, 2,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['12', True, True, 1,  40, 3,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['13', True, True, 1, 100, 3,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['14', True, True, 1, 200, 3,    2, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['15', True, True, 2, 200, 2,    4, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['16', True, True, 2, 100, 2, None, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['17', True, True, 2, 200, 2, None, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['18', True, True, 2, 100, 3, None, 100, 100, 64, 'LSTM', 'crf', 'english'],
    ['19', True, True, 1, 200, 3,    2, 200, 100, 64, 'LSTM', 'crf', 'english'],
    ['20', True, True, 1, 200, 3,    2, 100, 200, 64, 'LSTM', 'crf', 'english'],
    ['21', True, True, 1, 200, 3,    2, 200, 200, 64, 'LSTM', 'crf', 'english'],
    ['22', True, True, 2, 200, 3,    2, 200, 100, 64, 'LSTM', 'crf', 'english'],
    ['23', True, True, 2, 200, 3,    2, 100, 200, 64, 'LSTM', 'crf', 'english'],
    ['24', True, True, 2, 200, 3,    2, 200, 200, 64, 'LSTM', 'crf', 'english'],
    ['25', True, True, 1, 200, 3,    2, 300, 300, 64, 'LSTM', 'crf', 'english'],
    ['26', True, True, 2, 200, 3,    2, 300, 300, 64, 'LSTM', 'crf', 'english'],
    ['27', True, True, 1, 200, 3,    2, 200, 200, 16, 'LSTM', 'crf', 'english'],
    ['28', True, True, 2, 200, 3,    2, 300, 300, 16, 'LSTM', 'crf', 'english'],
    ['29', True, True, 1, 200, 3,    2, 300, 300, 16, 'LSTM', 'crf', 'english'],
    ['30', True, True, 2, 200, 3,    2, 300, 300, 16, 'LSTM', 'crf', 'english']
]

m_experiment_runs = [
    # [name, use_cnn, use_lstm, cnn layers, cnn number filters, cnn filter size, cnn max pool size, lstm size, embedding size, mini_batch_size, which_rnn, classifier, language]
    # ['Base', True, True, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf',       'english'], # same as cnn_optimization_runs #26.
    [  'M1', True,   True, 2, 200, 3, 2, 300, 300, 64,  'GRU',     'crf',      'english' ],
    [  'M2', False,  True, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf',      'english' ],
    [  'M3', False,  True, 2, 200, 3, 2, 300, 300, 64,  'GRU',     'crf',      'english' ],
    [  'M4', True,   True, 2, 200, 3, 2, 300, 300, 64, 'LSTM', 'softmax',      'english' ],
    [  'M5', True,  False, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf',      'english' ],
    [  'M6', True,   True, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf',      'italian' ],
    [  'M7', True,   True, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf',       'basque' ],
    [  'M8', True,  False, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf',      'NETtalk' ],
    [  'M9', True,  False, 2, 200, 3, 2, 300, 300, 16, 'LSTM',     'crf',      'NETtalk' ],
    [ 'M10', True,  False, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf', 'NETtalkTrain' ],
    [ 'M11', True,  False, 2, 200, 3, 2, 300, 300, 16, 'LSTM',     'crf', 'NETtalkTrain' ],
    [ 'M12', True,  False, 2, 200, 3, 2, 300, 300, 32, 'LSTM',     'crf', 'NETtalkTrain' ],
    [ 'M13', True,  False, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf',        'dutch' ],
    [ 'M14', True,   True, 2, 200, 3, 2, 300, 300, 64, 'LSTM',     'crf',     'manipuri' ]
]
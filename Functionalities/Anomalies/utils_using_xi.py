import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

##-----------------------------------------------------------------
def range_with_last(start, end):
    return range(start, end+1)

##-----------------------------------------------------------------
def find_key_by_substr(dct : dict, str_text : str):
    keys_array = []
    for val in dct.keys():
        if (str_text in val):
            keys_array.append(val)
    return keys_array

##-----------------------------------------------------------------
# Divide a sequence of numbers in a list of sub-sequences containing
# the target number
# [0 0 0 0 1 1 1 2 2 2 3 4 5 1 1] --> with target number of 1 --> [4,6], [13,14]
def find_sequences_of_number(vector, target_number):
    sequences = []
    current_sequence = []

    for i, value in enumerate(vector):
        if value == target_number:
            current_sequence.append(i)
        elif current_sequence:
            sequences.append(current_sequence)
            current_sequence = []

    # Aggiungi l'ultima sequenza se il vettore termina con il numero target
    if current_sequence:
        sequences.append(current_sequence)

    return sequences

##-----------------------------------------------------------------
def plot_signal(n, xn, x_label='', y_label='', title='$x_n$'):
    fig, ax = plt.subplots(figsize=(15, 4))

    font_size = 11
    legend_font_size = 10
    font_name = 'sans serif'

    # Define a function to format the y-axis labels
    def format_func(value, tick_number):
        return f"{value:.2f}".replace(".", ",")
    
    #ax.stem(n, xn)
    ax.plot(n, xn)
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_title(title)
    
    # Set the font properties for the tick labels
    plt.setp(ax.get_xticklabels(), fontsize=font_size, fontname=font_name)
    plt.setp(ax.get_yticklabels(), fontsize=font_size, fontname=font_name)

    # Format the y-axis labels
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))
    ax.set_xlabel(xlabel=x_label, fontsize=font_size, fontname=font_name)
    ax.set_ylabel(ylabel=y_label, fontsize=font_size, fontname=font_name)
    
    ax.set_title(title)



##-----------------------------------------------------------------
def plot_signals(n1, xn1, n2, xn2, label1='', label2='', 
                 x_label='', y_label='', ax=[], title=''):

    font_size = 11
    legend_font_size = 10
    font_name = 'sans serif'

    # Define a function to format the y-axis labels
    def format_func(value, tick_number):
        return f"{value:.2f}".replace(".", ",")

    if ax == []:
        fig, ax = plt.subplots(figsize=(15, 4))
    
    #ax.stem(n, xn)
    ax.plot(n1, xn1, label=label1, color='b')
    ax.plot(n2, xn2, label=label2, color='r')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    
    # Set the font properties for the tick labels
    plt.setp(ax.get_xticklabels(), fontsize=font_size, fontname=font_name)
    plt.setp(ax.get_yticklabels(), fontsize=font_size, fontname=font_name)

    # Format the y-axis labels
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))

    if ((label1 != '') & (label2 != '')):
        ax.legend(prop={'size': legend_font_size, 'family': font_name})
    ax.set_xlabel(xlabel=x_label, fontsize=font_size, fontname=font_name)
    ax.set_ylabel(ylabel=y_label, fontsize=font_size, fontname=font_name)
    ax.set_title(title)

##-----------------------------------------------------------------
def apply_changes_to_signal(xn, xi, beta):
    return xn * xi + beta

##-----------------------------------------------------------------
# Add a shift
def add_shift(N: int, timestamp_start: int=0, timestamp_stop: int=-1, value: float=0):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))

    start = timestamp_start
    if (timestamp_stop == -1):
        timestamp_stop = N
    end = timestamp_stop

    for timestamp_i in range(start,end):
        x_i[timestamp_i] = 1
        b_i[timestamp_i] = value

    return x_i, b_i

##-----------------------------------------------------------------
# Add several shifts
def add_shifts(N:int, timestamps_start: list, timestamps_stop: list, values: list):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))

    for start, stop, value in zip(timestamps_start, timestamps_stop, values):
        if (stop == -1):
            stop = N

        if (start > stop):
            print ('ERROR - start has to be successive to stop')
            break

        for timestamp_i in range(start, stop):
            x_i[timestamp_i] = 1
            b_i[timestamp_i] = value


    return x_i, b_i

##-----------------------------------------------------------------
# Set a specific value
def set_value(N: int, timestamps: list, values: list):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))
   
    for i in range (0, len(timestamps)):
        x_i[timestamps[i]] = 0
        b_i[timestamps[i]] = values[i]
        
    return x_i, b_i


##-----------------------------------------------------------------
# Set values for intervals of timestamps
def set_values(N: int, timestamps_start: list, timestamps_stop: list, values: list):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))

    for start, stop, value in zip(timestamps_start, timestamps_stop, values):
        if (stop == -1):
            stop = N

        if (start > stop):
            print ('ERROR - start has to be successive to stop')
            break

        for timestamp_i in range(start, stop):
            x_i[timestamp_i] = 0
            b_i[timestamp_i] = value


    return x_i, b_i


##-----------------------------------------------------------------
# Add a trend
def add_trend(N: int, timestamp_start: int=0, timestamp_stop: int=-1, slope: float=-0.01):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))

    start = timestamp_start
    if (timestamp_stop == -1):
        timestamp_stop = N
    end = timestamp_stop
    ts = range(start,end)

    for timestamp_i in range(start, end):
        x_i[timestamp_i] = 1

        value = slope * timestamp_i
        b_i[timestamp_i] = value
            
    x_i[end:]=1
    value = slope * end
    b_i[end:] = value
            
    return x_i, b_i

##-----------------------------------------------------------------
# Add a scaling phenomenon
def scale(N: int, timestamp_start: int=0, timestamp_stop: int=-1, value: float=0):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))

    start = timestamp_start
    if (timestamp_stop == -1):
        timestamp_stop = N
    end = timestamp_stop

    for timestamp_i in range(start,end):
        x_i[timestamp_i] = value
        b_i[timestamp_i] = 0

    return x_i, b_i


##-----------------------------------------------------------------
# Set values for intervals of timestamps
def scales (N: int, timestamps_start: list, timestamps_stop: list, values: list):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))

    for start, stop, value in zip(timestamps_start, timestamps_stop, values):
        if (stop == -1):
            stop = N

        if (start > stop):
            print ('ERROR - start has to be successive to stop')
            break

        for timestamp_i in range(start, stop):
            x_i[timestamp_i] = value
            b_i[timestamp_i] = 0

    return x_i, b_i

##-----------------------------------------------------------------
# Modulate original signal with another signal that modify the behavior 
# of the original signal. E.g. we can have an original signal modulated 
# by a gaussian 
# Alpha assume different meaning for different type of signals
def modulate_signal(N: int, timestamp_start: int=0, timestamp_stop: int=-1, type: str='-x+1', alpha: float = 100):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))
    
    start = timestamp_start
    if (timestamp_stop == -1):
        timestamp_stop = N
    end = timestamp_stop
    ts = range(start,end)

    for i in range(0, len(ts)):
        t_value = ts[i]
        if (type == '1-exp'):
            if (t_value == 0):
                envelope = 1
            else:
                envelope = (1-np.exp(- alpha * 1/t_value))
        elif (type == 'exp'):
            envelope = (np.exp(- alpha * t_value))
        elif (type == '-x+1'):
            envelope = -alpha*t_value + 1
            if (envelope < 0):
                envelope = 0

        x_i[t_value] = envelope

    return x_i, b_i



# Set values for intervals of timestamps
def modulate_signals (N: int, timestamps_start: list, timestamps_stop: list, type: str, alphas: list):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))

    for start, stop, alpha in zip(timestamps_start, timestamps_stop, alphas):
        if (stop == -1):
            stop = N
        if (stop > N):
            stop = N

        if (start > stop):
            print ('ERROR - start has to be successive to stop')
            break

        ts = range(start, stop)
        for i in range(0, len(ts)):
            t_final = ts[i]
            t_value = ts[i] - start # questo permette di avere diversi decadimenti ripartendo da 1
            if (type == '1-exp'):
                if (t_value == 0):
                    envelope = 1
                else:
                    envelope = (1-np.exp(- alpha * 1/t_value))
            elif (type == 'exp'):
                envelope = (np.exp(- alpha * t_value))
            elif (type == '-x+1'):
                envelope = -alpha*t_value + 1
                if (envelope < 0):
                    envelope = 0

            x_i[t_final] = envelope

    return x_i, b_i

##-----------------------------------------------------------------
# Add a noise
def add_noise(N: int, timestamp_start: int=0, timestamp_stop: int=0, sigma: float=1):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))

    start = timestamp_start
    if (timestamp_stop == -1):
        timestamp_stop = N
    end = timestamp_stop

    noise = sigma * np.random.randn(len(range(start, end)))
    
    b_i[start:end] = noise

    return x_i, b_i


##-----------------------------------------------------------------
# Add variable noise
def add_variable_noise(N: int, timestamp_start: int=0, timestamp_stop: int=0, levels: int=3, sigma: list=[]):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))
    
    start = timestamp_start
    if (timestamp_stop == -1):
        timestamp_stop = N
    end = timestamp_stop

    k=int((end-start) / levels)
    
    if (levels > len(sigma)):
        print ('ERROR - Not enough sigmal values')

    i = 0
    while ((start+k<=end) & (i <=N)):
        if(i == N-1):
            noise = sigma[i] * np.random.randn(len(range(start, end)))
            x_i[start:end] = 1
            b_i[start:end] = noise
        else:
            noise = sigma[i] * np.random.randn(len(range(start, start+k)))
            x_i[start:end] = 1
            b_i[start:start+k] = noise
        start = start+k
        i+=1

    return x_i, b_i

##-----------------------------------------------------------------
# Add an oscillation
#
# f0 va espresso come numero di cicli / numero di campioni, k/N, 
# come numero razionale in modo da avere un segnale sinusoidale 
# periodico 

def add_oscillation(N: int, t0: int, f0: float, sigma: float = 5, A: float = 1, debug=True):
    x_i = np.ones((N,))
    b_i = np.zeros((N,))
    t = np.array(range(0, N))
    
    oscillation = A*np.sin(2*np.pi*f0*(t-t0)) * np.exp(-((t-t0)/(sigma))**2)
    b_i = oscillation

    if (debug):
        plt.figure()
        plt.plot(oscillation)

    return x_i, b_i
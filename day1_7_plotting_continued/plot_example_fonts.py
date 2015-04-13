""" plotting -- fonts """

from matplotlib import pyplot
import numpy as np

def plot_example(x,y,
                 x_label,
                 y_label):
  """ simple plot """
  pyplot.plot(x,y)
  pyplot.xlabel(x_label)
  pyplot.ylabel(y_label)
  pyplot.tight_layout()
  pyplot.show()
  return
  
if __name__ == "__main__":
  
  x=np.linspace(0.,7.,100)
  y=np.sin(x)
  
  #from plot_example_edwin import data
  #x,y = data()
  
  ### string
  label_x = 'x [AU^2]'
  label_y = 'y_min [Sigma]'
  plot_example(x,y,label_x,label_y)
  
  ### basic LaTex mathtext
  label_x = '$x\,[AU^2]$'
  label_y = '$y_{min} [\Sigma]$'
  plot_example(x,y,label_x,label_y)
  
  ### rendering with LaTex -- serif
  label_x = r'$x\,[\rm{AU}^{2}]$'
  label_y = r'$y_{\rm{min}} [\Sigma]$'
  from matplotlib import rc
  rc('text', usetex=True)
  plot_example(x,y,label_x,label_y)
  
  ### rendering with LaTex -- sans-serif
  label_x = r'$x\,[AU^{2}]$'
  label_y = r'$y_{min} [\Sigma]$'
  rc('text', usetex=False)
  params = {'mathtext.default': 'regular' }
  pyplot.rcParams.update(params)
  plot_example(x,y,label_x,label_y)
  
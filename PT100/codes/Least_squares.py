import numpy as np
import matplotlib.pyplot as plt

Training_data = np.loadtxt('./training_data.txt',dtype=np.float32,delimiter=',')
Validation_data = np.loadtxt('./validation_data.txt',dtype=np.float32,delimiter=',')

Training_volt = np.reshape(Training_data[1,:],(Training_data.shape[1],1))
Training_temp = Training_data[0,:]

Validation_volt = np.reshape(Validation_data[1,:],(Validation_data.shape[1],1))
Validation_temp = Validation_data[0,:]

Training_temp_sq = (Training_temp**2)
vals = np.array([np.ones_like(Training_temp),Training_temp,Training_temp_sq],dtype=np.float32).T

LS_soln = np.linalg.inv(vals.T @ vals) @ vals.T @ Training_volt

print('Least Square Solution is: \n',LS_soln)

Temp = np.linspace(24,100,77)
vals = np.array([np.ones_like(Temp),Temp,Temp**2],dtype=np.float32).T

Voltage_predicted = vals @ LS_soln

plt.scatter(Training_temp,Training_volt,color='g',marker='o')
plt.plot(Temp,Voltage_predicted,'b')
plt.xlabel('Temperature(in C)')
plt.ylabel('Voltage(in V)')
plt.legend(['Predicted Voltage','Training Data'])
plt.grid(True)
plt.title('Training Data points')
plt.savefig('../figs/Training_Data.png')
plt.show()

plt.scatter(Validation_temp,Validation_volt,color='r',marker='o')
plt.plot(Temp,Voltage_predicted,'b')
plt.xlabel('Temperature(in C)')
plt.ylabel('Voltage(in V)')
plt.legend(['Predicted Voltage','Validation Data'])
plt.grid(True)
plt.title('Validation Data points')
plt.savefig('../figs/Validation_Data.png')
plt.show()

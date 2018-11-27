from matplotlib import pyplot
from csv import reader
from dateutil import parser
# Astro Pi Flight Data Analysis
with open('astro_pi_data_20150824_085954.csv', 'r') as f:
    csv_data = list(reader(f))

temperature = [i[2] for i in csv_data[1::]]
time = [parser.parse(i[19]) for i in csv_data[1::]]
pyplot.style.use('dark_background')
print(pyplot.style.available)
pyplot.title('Temperature changes over Time')
pyplot.xlabel('Time/hours')
pyplot.ylabel('Temperature/$^\circ$C')

pyplot.plot_date(time, temperature)
with pyplot.style.context(('dark_background')):
    pyplot.plot(time,temperature, 'r-o')
pyplot.show()
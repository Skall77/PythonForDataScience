import time

seconds_since_epoch = time.time()
scientific_epoch = "{:.2e}".format(seconds_since_epoch)
seconds_since_epoch = "{:,.3f}".format(seconds_since_epoch)
date = time.strftime('%b %d %Y')

print('Seconds since January 1, 1970:', seconds_since_epoch, 'or',
      scientific_epoch, 'in scientific notation')
print(date)

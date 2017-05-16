import h5py
import os

filename = "test/TERRA.20140413.0323.gcoos.sst.hdf"
if not os.path.isfile(filename):
    print 'file %s not found' % filename

if not os.access(filename, os.R_OK):
    print 'file %s not readable' % filename

f = h5py.File(filename, 'r')
for item in f.attrs.keys():
    print item + ": ", f.attrs[item]

f.close()



##########################
from pyhdf import SD
FILE_NAME="test/TERRA.20140413.0323.gcoos.sst.hdf" # The hdf file to read
SDS_NAME="sst" # The name of the sds to read
X_LENGTH=5
Y_LENGTH=16
def main():
    # open the hdf file for reading
    hdf=SD.SD(FILE_NAME)
    # read the sds data
    sds=hdf.select(SDS_NAME)
    data=sds.get()
    # turn [y,x] (HDF representation) data into [x,y] (numpy one)
    data=data.reshape(data.shape[1],data.shape[0])
    # print out the data
    msg_out=""
    for i in range(X_LENGTH):
        for j in range(Y_LENGTH):
            msg_out+=str(data[i,j])+" "
        msg_out+="\n"
    print msg_out
if __name__ == '__main__':
    main()
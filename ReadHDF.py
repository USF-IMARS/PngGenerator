from pyhdf import SD

class ReadHDF:

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
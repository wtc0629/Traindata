import pandas as pd



gestures = ["horizontally", "horizontally fast", "vertically", "vertically fast", "near to far", "near to far fast",
            "square", "square fast", "left circle (anticlockwise)", "right circle (clockwise)",
            "large right circle (clockwise)"]
if __name__ == "__main__":
    # Read the CSV file


    tester_name = ["PHD", "Dennis", "DRP", "Philipp", "QXR", "TMZ", "TYT", "WTC", "WTC2", "ZC", "YKD", "WTC3","1","2","3","Felix"]
    #tester_name = ["Felix"]
    data_frames = []
    for k in range(len(tester_name)):
        data = pd.read_csv("C:\\Users\\51004\\Desktop\\MergeCSV\\" + tester_name[k] + "\\gaze_merged.csv")

        data = data[["gaze_timestamp_datetime", "gaze_point_3d_x", "gaze_point_3d_y", "gaze_point_3d_z", "process"]]
        newGestures = []
        for i in range(11):
            for j in range(8):
                nowGesture = gestures[i] + '_GestureTime' + str(j)
                newGestures.append(nowGesture)
                #data.loc[data["process"] == nowGesture, ["gesture"]] = gestures[i]
                tempdata = data.loc[data["process"] == nowGesture]
                tempdata = tempdata.reset_index(drop=True)
                tempdata.loc[31: 90, ["process"]] = gestures[i] + str(4*j+1)
                tempdata.loc[91: 150, ["process"]] = gestures[i] + str(4*j+2)
                tempdata.loc[151: 210, ["process"]] = gestures[i] + str(4*j+3)
                tempdata.loc[211: 270, ["process"]] = gestures[i] + str(4*j+4)
                tempdata = tempdata.drop(tempdata[tempdata["process"] == nowGesture].index)
                data_frames.append(tempdata)


        #data = data.loc[data["process"].isin(newGestures)]
        #data = data.reset_index(drop=True)
        #data.reindex(data.process)
        exdata = pd.concat(data_frames)
        exdata = exdata.reset_index(drop=True)
        exdata.to_csv("C:\\Users\\51004\\Desktop\\MergeCSV\\" + tester_name[k] + "\\train_data.csv")


        #data.to_csv("C:\\Users\\51004\\Desktop\\MergeCSV\\" + tester_name[k] + "\\train_data.csv")

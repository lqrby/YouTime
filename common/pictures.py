from locust import HttpLocust,Locust, TaskSet, task
import random
class SelectPictures(TaskSet):

    def dongTaiPicture(self):
        self.imgArr = [
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1579586954823100281.png"
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1579586954823100282.png"
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1579586954823100283.png"



            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891075.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891076.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891077.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891078.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891079.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891080.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891081.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891082.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891083.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137928.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137929.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137930.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137931.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137932.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137933.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137934.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137935.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137936.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_2976_3968_/1577676438567.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_2976_3968_/1577676438568.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_2976_3968_/1577676438569.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438570.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438571.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438572.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438573.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438574.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438575.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680255.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680256.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680257.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680258.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680259.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680260.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680261.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680262.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680263.png",
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823533.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823534.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823535.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823536.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823537.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823538.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823539.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823540.png", 
            "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823541.png"
        ]
        return random.sample(self.imgArr ,random.randint(1,10))      
	
    def jiaZhiPicture(self):
        self.jzimgArr = [
            "F:/myTestFile/TestObject/YouTime/img/tp1.jpg",
            "F:/myTestFile/TestObject/YouTime/img/tp2.jpg",
            "F:/myTestFile/TestObject/YouTime/img/tp3.jpg"
            

            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1579586954823100281.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1579586954823100282.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1579586954823100283.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1577430385132100011.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1577430385132100012.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1577430385132100013.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1577784693192100061.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1577784693192100062.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/1577784693192100063.png"
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891076.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891077.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891078.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891079.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891080.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891081.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891082.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577675891083.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137928.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137929.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137930.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137931.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137932.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137933.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137934.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137935.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676137936.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_2976_3968_/1577676438567.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_2976_3968_/1577676438568.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_2976_3968_/1577676438569.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438570.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438571.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438572.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438573.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438574.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676438575.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680255.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680256.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680257.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680258.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680259.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680260.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680261.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680262.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676680263.png",
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823533.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823534.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823535.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823536.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823537.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823538.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823539.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823540.png", 
            # "https://youtime-test.oss-cn-beijing.aliyuncs.com/_1440_2560_/1577676823541.png"
        ]  
        # print("5555====={}".format(random.sample(self.jzimgArr,3)  ))
        return random.sample(self.jzimgArr,3)    

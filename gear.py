##By Jingting Jiang
##--------all the teeth numbers in following code are based on 1mm module------##

a=[10,11,12,13]
#The possible teeth number of gear A, is directly connect with motor.
b=range(10,29,1)
c=range(10,29,1)
d=range(10,29,1)
#list of possible teeth number for gear B,C and D. Which are all in
#different axial with gear A
m=1.0
#module
err=(float(5)/float(6000))
#the percentage uncertainty of output speed, also the percentage uncertainty
#of gear ratio.
ra=float(105*131)/float(6000)
#the ideal gear ratio (2.2925)


for za in a:
    for zb in b:
        for zc in c:
            for zd in d:
                i=(float(zb)/float(za))*(float(zd)/float(zc))
                r=abs(float(i-ra)/float(ra))
                Td=m*(za+0.5*zb+0.5*zc+zd)+2
                Td_2=(float(zc+zd)/2)-((float(zb)/2)+1)
                act_rpm=13755/i
#the +2 in Td is ad+dd(1mm for each, default value in inventor)
                if r<err and Td<45.7 and Td_2>2:
                    print [za,zb,zc,zd,act_rpm,Td,r]
#if the percentage deviation of the combination is smaller than percentage
#uncertainty and the total length of gear train is smaller than width of
#stage A (45.7mm). Then print the result via list.
                else:
                    pass

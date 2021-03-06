import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time

totalStart = time.time()

# fun large globals - here for easy access...
date, bid, ask = np.loadtxt('GBPUSD1d.txt', unpack = True,
                            delimiter = ',',
                            converters = { 0 : mdates.strpdate2num('%Y%m%d%H%M%S')})
               
avgLine = ((bid + ask) / 2)   
patternAr = []
performanceAr = []
patForRec = []
              
MAXIMUM = 1e12
MINIMUM = 1e-12
              
def percentChange(startPoint, currentPoint):
    try:
        ret = (100.00 * (float(currentPoint) - float(startPoint)) / float(abs(startPoint)))
        
        # avoid change = 0.0
        if ret < MINIMUM:
            ret = MINIMUM
    except:
        ret = MAXIMUM
    finally:
        return ret
    
    
def patternStorage():
    patStartTime = time.time()
    x = len(avgLine) - 60
    
    y = 31
    while y < x:
        pattern = []
    
        # I <3 magic numbers!
        p1  = percentChange(avgLine[y - 30], avgLine[y - 29])
        p2  = percentChange(avgLine[y - 30], avgLine[y - 28])
        p3  = percentChange(avgLine[y - 30], avgLine[y - 27])
        p4  = percentChange(avgLine[y - 30], avgLine[y - 26])
        p5  = percentChange(avgLine[y - 30], avgLine[y - 25])
        p6  = percentChange(avgLine[y - 30], avgLine[y - 24])
        p7  = percentChange(avgLine[y - 30], avgLine[y - 23])
        p8  = percentChange(avgLine[y - 30], avgLine[y - 22])
        p9  = percentChange(avgLine[y - 30], avgLine[y - 21])
        p10 = percentChange(avgLine[y - 30], avgLine[y - 20])
        p11 = percentChange(avgLine[y - 30], avgLine[y - 19])
        p12 = percentChange(avgLine[y - 30], avgLine[y - 18])
        p13 = percentChange(avgLine[y - 30], avgLine[y - 17])
        p14 = percentChange(avgLine[y - 30], avgLine[y - 16])
        p15 = percentChange(avgLine[y - 30], avgLine[y - 15])
        p16 = percentChange(avgLine[y - 30], avgLine[y - 14])
        p17 = percentChange(avgLine[y - 30], avgLine[y - 13])
        p18 = percentChange(avgLine[y - 30], avgLine[y - 12])
        p19 = percentChange(avgLine[y - 30], avgLine[y - 11])
        p20 = percentChange(avgLine[y - 30], avgLine[y - 10])
        p21 = percentChange(avgLine[y - 30], avgLine[y -  9])
        p22 = percentChange(avgLine[y - 30], avgLine[y -  8])
        p23 = percentChange(avgLine[y - 30], avgLine[y -  7])
        p24 = percentChange(avgLine[y - 30], avgLine[y -  6])
        p25 = percentChange(avgLine[y - 30], avgLine[y -  5])
        p26 = percentChange(avgLine[y - 30], avgLine[y -  4])
        p27 = percentChange(avgLine[y - 30], avgLine[y -  3])
        p28 = percentChange(avgLine[y - 30], avgLine[y -  2])
        p29 = percentChange(avgLine[y - 30], avgLine[y -  1])
        p30 = percentChange(avgLine[y - 30], avgLine[y -  0])


        outcomeRange = avgLine[y + 20 : y + 30]
        currentPoint = avgLine[y]
        # avoid -infinity
        try:
            avgOutcome =  reduce(lambda x, y: x + y, outcomeRange) / len(outcomeRange)
        except Exception, e:
            print str(e)
            avgOutcome = 0
            
        futureOutcome = percentChange(currentPoint, avgOutcome)
        pattern.append(p1 )
        pattern.append(p2 )
        pattern.append(p3 )
        pattern.append(p4 )
        pattern.append(p5 )
        pattern.append(p6 )
        pattern.append(p7 )
        pattern.append(p8 )
        pattern.append(p9 )
        pattern.append(p10)
        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)
        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)
        
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        
        y += 1
        
    patEndTime = time.time()    
    print len(patternAr)
    print len(performanceAr)
    print 'Pattern storage took:', patEndTime - patStartTime, 'seconds'
    
    
def currentPattern():
    
    cp1  = percentChange(avgLine[-31], avgLine[-30])
    cp2  = percentChange(avgLine[-31], avgLine[-29])
    cp3  = percentChange(avgLine[-31], avgLine[-28])
    cp4  = percentChange(avgLine[-31], avgLine[-27])
    cp5  = percentChange(avgLine[-31], avgLine[-26])
    cp6  = percentChange(avgLine[-31], avgLine[-25])
    cp7  = percentChange(avgLine[-31], avgLine[-24])
    cp8  = percentChange(avgLine[-31], avgLine[-23])
    cp9  = percentChange(avgLine[-31], avgLine[-22])
    cp10 = percentChange(avgLine[-31], avgLine[-21])
    cp11 = percentChange(avgLine[-31], avgLine[-20])
    cp12 = percentChange(avgLine[-31], avgLine[-19])
    cp13 = percentChange(avgLine[-31], avgLine[-18])
    cp14 = percentChange(avgLine[-31], avgLine[-17])
    cp15 = percentChange(avgLine[-31], avgLine[-16])
    cp16 = percentChange(avgLine[-31], avgLine[-15])
    cp17 = percentChange(avgLine[-31], avgLine[-14])
    cp18 = percentChange(avgLine[-31], avgLine[-13])
    cp19 = percentChange(avgLine[-31], avgLine[-12])
    cp20 = percentChange(avgLine[-31], avgLine[-11])
    cp21 = percentChange(avgLine[-31], avgLine[-10])
    cp22 = percentChange(avgLine[-31], avgLine[-9])
    cp23 = percentChange(avgLine[-31], avgLine[-8])
    cp24 = percentChange(avgLine[-31], avgLine[-7])
    cp25 = percentChange(avgLine[-31], avgLine[-6])
    cp26 = percentChange(avgLine[-31], avgLine[-5])
    cp27 = percentChange(avgLine[-31], avgLine[-4])
    cp28 = percentChange(avgLine[-31], avgLine[-3])
    cp29 = percentChange(avgLine[-31], avgLine[-2])
    cp30 = percentChange(avgLine[-31], avgLine[-1])
    
    patForRec.append(cp1 )
    patForRec.append(cp2 )
    patForRec.append(cp3 )
    patForRec.append(cp4 )
    patForRec.append(cp5 )
    patForRec.append(cp6 )
    patForRec.append(cp7 )
    patForRec.append(cp8 )
    patForRec.append(cp9 )
    patForRec.append(cp10)
    patForRec.append(cp11)
    patForRec.append(cp12)
    patForRec.append(cp13)
    patForRec.append(cp14)
    patForRec.append(cp15)
    patForRec.append(cp16)
    patForRec.append(cp17)
    patForRec.append(cp18)
    patForRec.append(cp19)
    patForRec.append(cp20)
    patForRec.append(cp21)
    patForRec.append(cp22)
    patForRec.append(cp23)
    patForRec.append(cp24)
    patForRec.append(cp25)
    patForRec.append(cp26)
    patForRec.append(cp27)
    patForRec.append(cp28)
    patForRec.append(cp29)
    patForRec.append(cp30)
    
    print patForRec
    
def patternRecognition():
    for eachPattern in patternAr:
    
        sim1  = 100.00 - abs(percentChange(eachPattern[0 ], patForRec[0 ]))
        sim2  = 100.00 - abs(percentChange(eachPattern[1 ], patForRec[1 ]))
        sim3  = 100.00 - abs(percentChange(eachPattern[2 ], patForRec[2 ]))
        sim4  = 100.00 - abs(percentChange(eachPattern[3 ], patForRec[3 ]))
        sim5  = 100.00 - abs(percentChange(eachPattern[4 ], patForRec[4 ]))
        sim6  = 100.00 - abs(percentChange(eachPattern[5 ], patForRec[5 ]))
        sim7  = 100.00 - abs(percentChange(eachPattern[6 ], patForRec[6 ]))
        sim8  = 100.00 - abs(percentChange(eachPattern[7 ], patForRec[7 ]))
        sim9  = 100.00 - abs(percentChange(eachPattern[8 ], patForRec[8 ]))
        sim10 = 100.00 - abs(percentChange(eachPattern[9 ], patForRec[9 ]))
        sim11 = 100.00 - abs(percentChange(eachPattern[10], patForRec[10]))
        sim12 = 100.00 - abs(percentChange(eachPattern[11], patForRec[11]))
        sim13 = 100.00 - abs(percentChange(eachPattern[12], patForRec[12]))
        sim14 = 100.00 - abs(percentChange(eachPattern[13], patForRec[13]))
        sim15 = 100.00 - abs(percentChange(eachPattern[14], patForRec[14]))
        sim16 = 100.00 - abs(percentChange(eachPattern[15], patForRec[15]))
        sim17 = 100.00 - abs(percentChange(eachPattern[16], patForRec[16]))
        sim18 = 100.00 - abs(percentChange(eachPattern[17], patForRec[17]))
        sim19 = 100.00 - abs(percentChange(eachPattern[18], patForRec[18]))
        sim20 = 100.00 - abs(percentChange(eachPattern[19], patForRec[19]))
        sim21 = 100.00 - abs(percentChange(eachPattern[20], patForRec[20]))
        sim22 = 100.00 - abs(percentChange(eachPattern[21], patForRec[21]))
        sim23 = 100.00 - abs(percentChange(eachPattern[22], patForRec[22]))
        sim24 = 100.00 - abs(percentChange(eachPattern[23], patForRec[23]))
        sim25 = 100.00 - abs(percentChange(eachPattern[24], patForRec[24]))
        sim26 = 100.00 - abs(percentChange(eachPattern[25], patForRec[25]))
        sim27 = 100.00 - abs(percentChange(eachPattern[26], patForRec[26]))
        sim28 = 100.00 - abs(percentChange(eachPattern[27], patForRec[27]))
        sim29 = 100.00 - abs(percentChange(eachPattern[28], patForRec[28]))
        sim30 = 100.00 - abs(percentChange(eachPattern[29], patForRec[29]))
        
        simSum = 0.0
        
        simSum += sim1 
        simSum += sim2 
        simSum += sim3 
        simSum += sim4 
        simSum += sim5 
        simSum += sim6 
        simSum += sim7 
        simSum += sim8 
        simSum += sim9 
        simSum += sim10
        simSum += sim11
        simSum += sim12
        simSum += sim13
        simSum += sim14
        simSum += sim15
        simSum += sim16
        simSum += sim17
        simSum += sim18
        simSum += sim19
        simSum += sim20
        simSum += sim21
        simSum += sim22
        simSum += sim23
        simSum += sim24
        simSum += sim25
        simSum += sim26
        simSum += sim27
        simSum += sim28
        simSum += sim29
        simSum += sim30
        
        howSim = simSum / 30
        
        if howSim > 95:
            patDex = patternAr.index(eachPattern)
        
            print '###########################'
            print '###########################'
            print howSim
            print '###########################'
            print '###########################'
            print patForRec
            print '==========================='
            print '==========================='
            print eachPattern            
            print '---------------------------'
            print 'predicted outcome', performanceAr[patDex]
            
            xp = [] # 0 to 29
            for i in range(30):
                xp.append(i)
            fig = plt.figure()
            # print len(xp)
            # print len(patForRec)
            
            plt.plot(xp, patForRec)
            plt.plot(xp, eachPattern)
            try:
                plt.show()
            except:
                print 'Exception'
                
            print '###########################'
            print '###########################'
        
def graphRawFX():

    fig = plt.figure(figsize = (10, 7))
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan = 40, colspan = 40)
    
    ax1.plot(date, bid)
    ax1.plot(date, ask)
    
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    ax1_2 = ax1.twinx()
    
    ax1_2.fill_between(date, 0, (ask - bid), facecolor = 'g', alpha = 0.3)    
        
    plt.subplots_adjust(bottom = 0.23)
    
    plt.grid(True)
    plt.show()
    
    
    
def main():
    # graphRawFX()

    patternStorage()
    
    currentPattern()

    patternRecognition()

    totalTime = time.time() - totalStart
    
    print 'Entire processing time took:', totalTime, 'seconds'
    
if __name__ == '__main__':

    main()
    
    # sys.exit(0)
    
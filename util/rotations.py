
'''
rotation_list = {

0: [(((0,1),1),((1,2),1)), (((0,2),1),((1,2),1))],
1: [(((1,0),1),((1,2),1)), (((2,0),1),((1,2),1))],
2: [(((0,1),1),((1,2),3)), (((0,2),1),((1,2),3))],
3: [(((1,0),1),((1,2),3)), (((2,0),1),((1,2),3))],
4: [(((0,1),1),((1,2),0)), (((0,2),1),((1,2),0))],
5: [(((1,0),1),((1,2),0)), (((2,0),1),((1,2),0))],
6: [(((0,1),1),((1,2),2)), (((0,2),1),((1,2),2))],
7: [(((1,0),1),((1,2),2)), (((2,0),1),((1,2),2))],
}



rotation_list = {

0: [(((0,1),1),((1,2),0)), (((0,1),1),((1,2),1)), (((0,2),1),((1,2),0)), (((0,2),1),((1,2),1))],
1: [(((0,1),1),((1,2),2)), (((0,1),1),((1,2),3)), (((0,2),1),((1,2),2)), (((0,2),1),((1,2),3))],
2: [(((0,1),3),((1,2),0)), (((0,1),3),((1,2),1)), (((0,2),3),((1,2),0)), (((0,2),1),((1,2),1))],
3: [(((0,1),3),((1,2),2)), (((0,1),3),((1,2),3)), (((0,2),3),((1,2),2)), (((0,2),1),((1,2),3))],
}

'''
# this is used in mwr_cli 26 Dec
# rotation_list = [(((0,1),1),((1,2),0)), (((0,1),1),((1,2),1)), (((1,2),1),((0,2),0)), (((0,2),1),((1,2),1)), 
#                 (((0,1),1),((1,2),2)), (((0,1),1),((1,2),3)), (((1,2),1),((0,2),2)), (((0,2),1),((1,2),3)), 
#                 (((0,1),3),((1,2),0)), (((0,1),3),((1,2),1)), (((1,2),3),((0,2),0)), (((0,2),1),((1,2),1)), 
#                 (((0,1),3),((1,2),2)), (((0,1),3),((1,2),3)), (((1,2),3),((0,2),2)), (((0,2),1),((1,2),3))]
# this is from old dgx(workhorse branch) version
# rotation_list = [(((0,1),1),((1,2),0)), (((0,1),1),((1,2),1)), (((0,2),1),((1,2),0)), (((0,2),1),((1,2),1)), 
                # (((0,1),1),((1,2),2)), (((0,1),1),((1,2),3)), (((0,2),1),((1,2),2)), (((0,2),1),((1,2),3)), 
                # (((0,1),3),((1,2),0)), (((0,1),3),((1,2),1)), (((0,2),3),((1,2),0)), (((0,2),1),((1,2),1)), 
                # (((0,1),3),((1,2),2)), (((0,1),3),((1,2),3)), (((0,2),3),((1,2),2)), (((0,2),1),((1,2),3))]

#All 20 rotation
# rotation_list = [(((0,1),1),((1,2),0)), (((0,1),1),((1,2),1)), (((0,2),1),((1,2),0)), (((0,2),1),((1,2),1)), 
#                 (((0,1),1),((1,2),2)), (((0,1),1),((1,2),3)), (((0,2),1),((1,2),2)), (((0,2),1),((1,2),3)), 
#                 (((0,1),3),((1,2),0)), (((0,1),3),((1,2),1)), (((0,2),3),((1,2),0)), (((0,2),1),((1,2),1)), 
#                 (((0,1),3),((1,2),2)), (((0,1),3),((1,2),3)), (((0,2),3),((1,2),2)), (((0,2),1),((1,2),3)),
#                 (((1,2),1),((0,2),0)), (((1,2),1),((0,2),2)), (((1,2),3),((0,2),0)), (((1,2),3),((0,2),2))]

rotation_list = [(((0,1),1),((1,2),0)), (((0,1),1),((1,2),1)), (((0,2),1),((1,2),0)), (((0,2),1),((1,2),1)), 
                (((0,1),1),((1,2),2)), (((0,1),1),((1,2),3)), (((0,2),1),((1,2),2)), (((0,2),1),((1,2),3)), 
                (((0,1),3),((1,2),0)), (((0,1),3),((1,2),1)), (((0,2),3),((1,2),0)), (((0,2),1),((1,2),1)), 
                (((0,1),3),((1,2),2)), (((0,1),3),((1,2),3)), (((0,2),3),((1,2),2)), (((0,2),1),((1,2),3))]

#((0,1),0),((1,2),0)), (((0,1),0),((1,2),1)),
#((0,1),0),((1,2),2)), (((0,1),0),((1,2),3)),
#((0,1),2),((1,2),0)), (((0,1),2),((1,2),1)),
#((0,1),2),((1,2),2)), (((0,1),2),((1,2),3)),

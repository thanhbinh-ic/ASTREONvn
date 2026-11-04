screen path_first_1:
    imagebutton:
        idle "gui/button/LNAV1.png"
        hover "gui/button/LNAV.png"
        xalign 0.648
        yalign 0.795
        action Jump('path_first_left_1')
        focus_mask True 
        
    imagebutton:
        idle "gui/button/RNAV1.png"
        hover "gui/button/RNAV.png"
        xalign 0.73
        yalign 0.795
        action Jump('path_first_right_2')
        focus_mask True 
        
screen path_first_right_next_1:
    
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_right_3')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_right_2_back')
        focus_mask True  

screen path_first_right_next_2:
    
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_right_4')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_right_2_back')
        focus_mask True  

screen path_first_right_2_back:
    
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_left_1')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_right_4')
        focus_mask True

screen path_first_right_next_3:
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_right_2_back')
        focus_mask True

screen path_first_left_next_3:

    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_right_4')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_right_2')
        focus_mask True  

screen path_first_left_next_4:

    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_left_next_5')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_left_next_4')
        focus_mask True  

screen path_first_left_next_5:

    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_right_4')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_left_next_4')
        focus_mask True  

screen path_first_back_6:

    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_right_2')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_left_1')
        focus_mask True  

screen path_first_left_next_7:

    imagebutton:
        idle "gui/button/RNAV1.png"
        hover "gui/button/RNAV.png"
        xalign 0.73
        yalign 0.795
        action Jump('path_first_left_next_8')
        focus_mask True 

        

    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_left_next_4')
        focus_mask True  

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_left_next_5')
        focus_mask True  

screen path_first_left_next_8_2:
    
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_second_up_3_3')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_left_next_7')
        focus_mask True  

screen path_first_left_next_8_1:
    
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_second_up_2')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_second_up_1')
        focus_mask True  

screen path_second_up_2:
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_left')
        focus_mask True

    imagebutton:
        idle "gui/button/RNAV1.png"
        hover "gui/button/RNAV.png"
        xalign 0.73
        yalign 0.795
        action Jump('front')
        focus_mask True 

screen path_second_up_3:
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_second_up_3_2')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_second_up_3_1')
        focus_mask True  

screen path_second_up_7:

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_second_up_3_1')
        focus_mask True  

screen path_second_up_4:
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_second_up_1')
        focus_mask True

screen path_second_up_5:
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_left_next_5')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_second_up_2')
        focus_mask True  


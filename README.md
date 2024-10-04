# How to use this script

1. Make a screenshot of your entire screen. Extract it into an image editing software to get the exact pixel location of the faceit application. Don't move it, otherwise the script breaks lmao
2. update the values in the script.
   2.1 "search_area" is the area the script checks. The first value is the pixel position from the left of the screen, the second one from the top of the screen. After that comes the width and height of the area to search.
   2.2 "scroll_amount should probably match the height of the area to search, it defines how much the script scrolls down in the list after clicking each checkbox.
   2.3 "scroll_pause_time" gives the script some breathing room before repeating the process. The lower this value is, the faster the script executes.
   2.4 "click_pause_time" stops the script for some time after clicking a checkbox in order to not miss an input
   2.5 "color_to_find" if you want to reanable all checkboxes you could adjust the color with the corresponding R, G, B values. It's basically the color that gets clicked when the script runs
3. Run the script and bring Faceit to the front. Press "Shift + G" to start the execution. It will automatically stop if it doesn't find the color anymore

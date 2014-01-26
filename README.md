<h2>Matplotlib Annotator</h2> 

<h5> ...for the <a href="http://www.kaggle.com/c/belkin-energy-disaggregation-competition"> energy disaggregation competition (Kaggle) </a> </h5>

<h4> Description </h4>

The annotator handles .mat files with specific data structure (the one that was used in the competition) and plots the absolute values of current for both phases. The annotations are displayed as vertical draggable/resizable rectangles that can be annotated with each one of the two phases. The user can extract/save the annotations in json format or reload previously extracted annotations in json format.

The annotator was developed to help fix the annotations provided in the training data (for the competition) however the implementetion could be useful as an example of interactive matplotlib usage.

<h4> How to use </h4>

python annotator.py {matlab-file} {json-file} {load-annotations-from-json}

* <b>matlab-file</b>: .mat file containing data and annotations
* <b>json-file</b>: .json file containing annotations only
* <b>load-annotations-from-json</b>: if set to True the annotations are loaded from the json-file (optional)




<a href="http://s149.photobucket.com/user/nicktgr15/media/misalinged_zps7ca4a449.png.html" target="_blank"><img src="http://i149.photobucket.com/albums/s67/nicktgr15/misalinged_zps7ca4a449.png" border="0" alt=" photo misalinged_zps7ca4a449.png"/></a>

<a href="http://s149.photobucket.com/user/nicktgr15/media/properlyaligned_zpsf2a0212d.png.html" target="_blank"><img src="http://i149.photobucket.com/albums/s67/nicktgr15/properlyaligned_zpsf2a0212d.png" border="0" alt=" photo properlyaligned_zpsf2a0212d.png"/></a>

<a href="http://s149.photobucket.com/user/nicktgr15/media/annotationsloadedfromjson_zps308ffa8e.png.html" target="_blank"><img src="http://i149.photobucket.com/albums/s67/nicktgr15/annotationsloadedfromjson_zps308ffa8e.png" border="0" alt=" photo annotationsloadedfromjson_zps308ffa8e.png"/></a>

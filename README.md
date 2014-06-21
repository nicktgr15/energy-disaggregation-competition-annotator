<h2>Matplotlib Annotator</h2> 

<h5> ...for the <a href="http://www.kaggle.com/c/belkin-energy-disaggregation-competition"> energy disaggregation competition (Kaggle) </a> </h5>

<h4> Description </h4>

The annotator handles .mat files with specific data structure (the one that was used in the competition) and plots the absolute values of current for both phases. The annotations are displayed as vertical draggable/resizable rectangles that can be annotated with each one of the two phases. The user can extract/save the annotations in json format or reload previously extracted annotations in json format.

The annotator was developed to help fix the alignment of the annotations provided in the training data (for the competition) however the implementetion could be useful as an example of interactive matplotlib usage.

<h4> How to use </h4>

python annotator.py {matlab-file} {json-file} --load-from-json

* <b>matlab-file</b>: .mat file containing data and annotations
* <b>json-file</b>: .json file containing annotations only
* <b>--load-from-json</b>:  if set the annotations are loaded from the json-file (optional)


<a href="http://s149.photobucket.com/user/nicktgr15/media/1_zps381b15cf.png.html" target="_blank"><img src="http://i149.photobucket.com/albums/s67/nicktgr15/1_zps381b15cf.png" border="0" alt=" photo 1_zps381b15cf.png"/></a>

<a href="http://s149.photobucket.com/user/nicktgr15/media/2_zps7c13a554.png.html" target="_blank"><img src="http://i149.photobucket.com/albums/s67/nicktgr15/2_zps7c13a554.png" border="0" alt=" photo 2_zps7c13a554.png"/></a>

<a href="http://s149.photobucket.com/user/nicktgr15/media/3_zps4c92b356.png.html" target="_blank"><img src="http://i149.photobucket.com/albums/s67/nicktgr15/3_zps4c92b356.png" border="0" alt=" photo 3_zps4c92b356.png"/></a>

import scipy.io
import matplotlib.pyplot as plt
import json
import sys
from utils.draggable_axvspan import DraggableAxvspan
import argparse


class Annotator:

    def __init__(self, matlab_file, json_file, load_annotations_from_json):
        self.matlab_file = matlab_file[0]
        self.json_file = json_file[0]
        self.load_annotations_from_json = load_annotations_from_json
        self.dr = []
        self.obj_id_label = None;

    def read_json_file(self, json_file):
        with open(json_file, 'r') as file:
            d = json.load(file)
        return d

    def get_annotations_from_json(self, textfile):
        annotations = {"id" : [], "time" : [], "name": [], "annotation_class": []}
        d = self.read_json_file(textfile)
        for v in d:
            annotations["name"].append(v["name"])
            annotations["time"].append(v["time"])
            annotations["id"].append(v["id"])
            annotations["annotation_class"].append(v["annotation_class"])
        return annotations

    def get_annotations_from_tags(self, tags):
        annotations = {"id" : [], "time" : [], "name": [], "annotation_class": []}
        for tag_i, tag in enumerate(tags):
            annotations["name"].append(tag[1][0][0][0])
            annotations["time"].append([tag[2][0][0], tag[3][0][0]])
            annotations["id"].append(tag[0][0][0])
            annotations["annotation_class"].append(None)
        return annotations

    def json_save_annotations(self, event):
        d = []
        for obj in self.dr:
            if obj.get_annotation_class() is not None:
                d.append(obj)
        with open(self.json_file, 'w') as f:
            f.write(str(d))
        print str(d)

    def set_phase_1(self, event):
        self.dr[int(self.obj_id_label.get_text())].set_colour("b")

    def set_phase_2(self, event):
        self.dr[int(self.obj_id_label.get_text())].set_colour("r")

    def set_phase_none(self, event):
        self.dr[int(self.obj_id_label.get_text())].set_colour("g")

    def create_annotator(self):
        mat = scipy.io.loadmat(self.matlab_file)

        timeticks1 = mat['Buffer']['TimeTicks1'][0][0].flatten()
        timeticks2 = mat['Buffer']['TimeTicks2'][0][0].flatten()

        i1 = mat["Buffer"]["LF1I"][0][0]
        i2 = mat["Buffer"]["LF2I"][0][0]

        i1_abs = abs(i1)
        i2_abs = abs(i2)

        if self.load_annotations_from_json:
            annotations = self.get_annotations_from_json(self.json_file)
        else:
            tags = mat["Buffer"]["TaggingInfo"][0][0]
            annotations = self.get_annotations_from_tags(tags)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        plt.subplots_adjust(bottom=0.15)

        plt.plot(timeticks2, i2_abs[:, 0])
        plt.plot(timeticks1, i1_abs[:, 0])

        fg = plt.figtext(0.02, 0.02, "none")
        self.obj_id_label = plt.figtext(0.02, 0.06, "none")

        phase1_ax = plt.axes([0.4, 0.02, 0.10, 0.05])
        phase1_button = plt.Button(phase1_ax, 'Phase 1')
        phase1_button.on_clicked(self.set_phase_1)

        phase2_ax = plt.axes([0.52, 0.02, 0.10, 0.05])
        phase2_button = plt.Button(phase2_ax, 'Phase 2')
        phase2_button.on_clicked(self.set_phase_2)

        phase_none_ax = plt.axes([0.64, 0.02, 0.10, 0.05])
        phase_none_button = plt.Button(phase_none_ax, 'None')
        phase_none_button.on_clicked(self.set_phase_none)

        save_ax = plt.axes([0.87, 0.02, 0.10, 0.05])
        save_button = plt.Button(save_ax, 'Save')
        save_button.on_clicked(self.json_save_annotations)

        for i in range(len(annotations["time"])):
            r = ax.axvspan(annotations["time"][i][0], annotations["time"][i][1], facecolor='g', alpha=0.5)
            d = DraggableAxvspan(r, annotations["id"][i], annotations["name"][i], fg, i, self.obj_id_label, annotations["annotation_class"][i])
            self.dr.append(d)

        plt.show()


def main():
    parser = argparse.ArgumentParser();
    parser.add_argument("matlab_file",nargs=1)
    parser.add_argument("json_file", nargs=1)
    parser.add_argument("load_annotations_from_json", nargs='?', default = False)
    args = parser.parse_args()
    annotator = Annotator(args.matlab_file, args.json_file, args.load_annotations_from_json);
    annotator.create_annotator();

if __name__ == "__main__": main()
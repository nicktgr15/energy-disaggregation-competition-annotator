import json


class DraggableAxvspan:
    def __init__(self, rect, id, name, fg, obj_id, obj_id_label, annotation_class = None):
        self.rect = rect
        self.id = id
        self.obj_id = obj_id
        self.name = name
        self.press = None
        self.state = None
        self.annotation_class = annotation_class
        if annotation_class == 'phase1':
            self.rect.set_color('b')
        if annotation_class == 'phase2':
            self.rect.set_color('r')
        self.obj_id_label = obj_id_label
        self.fg = fg
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def __repr__(self):
        return json.dumps(
            {"id": str(self.get_id()),
             "name": str(self.get_name()),
             "time": [str(self.get_start()),str(self.get_end())],
             "annotation_class": str(self.get_annotation_class())
            }, sort_keys=True, indent=4, separators=(',', ': '))

    def get_annotation_class(self):
        return self.annotation_class

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_colour(self, colour):
        if colour == "b":
            self.annotation_class = "phase1"
        if colour == "r":
            self.annotation_class = "phase2"
        if colour == "g":
            self.annotation_class = None
        self.rect.set_color(colour)
        self.rect.figure.canvas.draw()

    def set_start(self, start):
        self.rect.xy[0] = [start,0]
        self.rect.xy[1] = [start,1]
        self.rect.xy[4] = [start,0]

    def set_end(self, end):
        self.rect.xy[2] = [end, 1]
        self.rect.xy[3] = [end, 0]

    def get_start(self):
        return self.rect.xy[0][0]

    def get_end(self):
        return self.rect.xy[2][0]

    def on_release(self, event):
        self.press = None

    def on_motion(self, event):
        if self.press is None: return
        if event.inaxes != self.rect.axes: return

        start, end, xpress, click_area, xpress_pixels = self.press
        dx = event.xdata - xpress

        if click_area is "left":
                self.set_start(start + dx)
        elif click_area is "right":
                self.set_end(end + dx)
        elif click_area is "center":
            self.set_start(start+dx)
            self.set_end(end+dx)
        self.rect.figure.canvas.draw()

    def on_press(self, event):

        if event.inaxes != self.rect.axes: return
        contains, attrd = self.rect.contains(event)
        if not contains: return

        self.obj_id_label.set_text(self.obj_id)
        self.fg.set_text(self.name)
        self.rect.figure.canvas.draw()

        if event.x-self.rect.get_extents().x0 < 10:
            self.press = self.get_start(), self.get_end(), event.xdata, "left", event.x
        elif self.rect.get_extents().x1-event.x < 10:
            self.press = self.get_start(), self.get_end(), event.xdata, "right", event.x
        else:
            self.press = self.get_start(), self.get_end(), event.xdata, "center", event.x
import {addInputZone, redrawRectangles} from "./rectangle_drawer_utils";

export class FacesDetector {
    rectangles;
    image_width_ratio;
    image_height_ratio;
    url = 'http://localhost:5001/detection';

    constructor(rectangles_drawer) {
        this.rectangles = rectangles_drawer.rectangles;
        this.image_width_ratio = rectangles_drawer.image_width_ratio;
        this.image_height_ratio = rectangles_drawer.image_height_ratio;
    }

    postToServerForFaceDetection() {
        var fd = new FormData();
        var files = $('#file')[0].files;

        // Check file selected or not
        if (files.length > 0) {
            fd.append('photo', files[0]);
            $.ajax({
                url: this.url,
                type: 'post',
                data: fd,
                dataType: "json",
                contentType: false,
                processData: false,
                success: (response) => {
                    if (response.has_faces === true)
                        this.processDetectedFaces(response.coordinates);
                }
            });
        }
    }

    processDetectedFaces(coordinates) {
        for (let coords of coordinates) {
            this.rectangles.push({
                x: coords.left / this.image_width_ratio,
                y: coords.top / this.image_height_ratio,
                width: (coords.right - coords.left) / this.image_width_ratio,
                height: (coords.bottom - coords.top) / this.image_height_ratio
            });
            redrawRectangles(this.rectangles);
            addInputZone(this.rectangles);
        }
    }

}

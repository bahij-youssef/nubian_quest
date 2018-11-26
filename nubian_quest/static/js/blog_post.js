$(document).ready(function () {
    var photo_1 = document.getElementById('photo_1');
    var photo_2 = document.getElementById('photo_2');
    var photo_3 = document.getElementById('photo_3');

    var numOfPhotosAvailable = 2;

    if (photo_2 != null) {
        numOfPhotosAvailable++;
        if (photo_3 != null) {
            numOfPhotosAvailable++;
        }
    }

    var numOfParagraph = (document.getElementsByClassName('MsoNormal')).length;
    var newPlacementIndex = Math.floor(numOfParagraph / numOfPhotosAvailable);

    $(photo_1).insertAfter($('.MsoNormal').eq(newPlacementIndex));
    $(photo_2).insertAfter($('.MsoNormal').eq(2 * newPlacementIndex));
    $(photo_3).insertAfter($('.MsoNormal').eq(3 * newPlacementIndex));
});
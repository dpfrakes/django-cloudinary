$(function() {
    var $width = $('#cn-width');
    var $height = $('#cn-height');
    var $mode = $('#cn-mode');
    var $format = $('#cn-format');
    var $quality = $('#cn-quality-type');

    var $watermarkId = $('#cn-watermark-id');
    var $watermarkMode = $('#cn-watermark-mode');
    var $watermarkWidth = $('#cn-watermark-width');
    var $watermarkHeight = $('#cn-watermark-height');
    var $watermarkGravity = $('#cn-watermark-gravity'); // g_
    var $watermarkX = $('#cn-watermark-x-offset'); // x_
    var $watermarkY = $('#cn-watermark-y-offset'); // y_

    var $previewUrl = $('#preview-url');

    function refreshPreviewUrl() {

        var imgParams = [];
        var watermarkParams = [];
        var originalUrl = $previewUrl.attr('data-original-url');
        var fileFormat = originalUrl.substr(originalUrl.lastIndexOf('.') + 1);

        // Original image edits
        if($height.val() != '' || $width.val() != '') {
            imgParams.push('c_' + $mode.val());

            if($height.val() != '') {
                imgParams.push('h_' + $height.val());
            }
            if($width.val() != '') {
                imgParams.push('w_' + $width.val());
            }
        }

        if($quality.val() != '') {
            imgParams.push('q_' + $quality.val());
        }

        if($format.val() != '') {
            // keep format
            if($format.val() == '__empty__') {
                fileFormat = '';
            } else {
                fileFormat = $format.val();
            }
        }

        // Watermark params
        if($watermarkId.val() != '') {
            watermarkParams.push('l_' + $watermarkId.val());

            if($watermarkHeight.val() != '' || $watermarkWidth.val() != '') {
                watermarkParams.push('c_' + $watermarkMode.val());

                if($watermarkHeight.val() != '') {
                    watermarkParams.push('h_' + $watermarkHeight.val());
                }
                if($watermarkWidth.val() != '') {
                    watermarkParams.push('w_' + $watermarkWidth.val());
                }
            }

            if($watermarkGravity.val() != '') {
                watermarkParams.push('g_' + $watermarkGravity.val());
            }
            if($watermarkX.val() != '') {
                watermarkParams.push('x_' + $watermarkX.val());
            }
            if($watermarkY.val() != '') {
                watermarkParams.push('y_' + $watermarkY.val());
            }
        }

        // Build final preview URL
        cnParams = imgParams.length > 0 ? imgParams.join(',') + '/' : '';
        cnParams += watermarkParams.length > 0 ? watermarkParams.join(',') + '/' : '';

        var url = '';

        if(fileFormat == '') {
            url = originalUrl.substr(0, originalUrl.lastIndexOf('.'));
        } else {
            url = originalUrl.substr(0, originalUrl.lastIndexOf('.') + 1) + fileFormat;
        }

        url = url.replace('upload/', 'upload/' + cnParams);

        $previewUrl.text(url);
        $previewUrl.attr('href', url);

    }

    $('body').keyup(refreshPreviewUrl);
    $('select').change(refreshPreviewUrl);
});

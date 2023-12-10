# -*- coding: UTF-8 -*-
import numpy
import re
import cv2
import ctypes
import ctypes.util
import time
import os
import imageio


# main_path = os.path.abspath(".")
# main_path = '/'.join(main_path.split('\\'))
# main_path = os.path.abspath(".") + os.path.sep
DLL_PATH = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../..")), "bin", "libtesseract-5.dll")
# os.path.join(os.path.abspath("."), "..", "bin", "libtesseract-5.dll")
print(DLL_PATH)
os.add_dll_directory(DLL_PATH)
# print(DLL_PATH)
DATA_PATH = b"...\\bin"
LANGUAGE = b"eng"
CONFIG = b"-psm 6"


class TesseractError(Exception):
    pass


class Tesseract(object):
    _lib = None
    _api = None

    class TessBaseAPI(ctypes._Pointer):
        _type_ = type('_TessBaseAPI', (ctypes.Structure,), {})

    @classmethod
    def setup_lib(cls, lib_path=None):
        if cls._lib is not None:
            return
        if lib_path is None:
            lib_path = ctypes.util.find_library("libtesseract-5")
            # print("libtesseract-5-lib_path: ", lib_path)
            if lib_path is None:
                raise TesseractError('_tesseractlib library not found')
        cls._lib = lib = ctypes.CDLL(lib_path)

        lib.TessBaseAPICreate.restype = cls.TessBaseAPI

        lib.TessBaseAPIDelete.restype = None  # void
        lib.TessBaseAPIDelete.argtypes = (cls.TessBaseAPI,)  # handle

        lib.TessBaseAPIInit3.argtypes = (
            cls.TessBaseAPI,  # handle
            ctypes.c_char_p,  # datapath
            ctypes.c_char_p)  # language

        lib.TessBaseAPISetImage.restype = None
        lib.TessBaseAPISetImage.argtypes = (
            cls.TessBaseAPI,  # handle
            ctypes.c_void_p,  # imagedata
            ctypes.c_int,  # width
            ctypes.c_int,  # height
            ctypes.c_int,  # bytes_per_pixel
            ctypes.c_int)  # bytes_per_line

        lib.TessBaseAPIGetUTF8Text.restype = ctypes.c_char_p
        lib.TessBaseAPIGetUTF8Text.argtypes = (cls.TessBaseAPI,)  # handle

    def __init__(self, language=LANGUAGE, data_path=DATA_PATH, lib_path=DLL_PATH, config=CONFIG):
        if self._lib is None:
            self.setup_lib(lib_path)
        self._api = self._lib.TessBaseAPICreate()
        if self._lib.TessBaseAPIInit3(self._api, data_path, language, config):
            raise TesseractError('initialization failed')

    def __del__(self):
        if not self._lib or not self._api:
            return
        if not getattr(self, 'closed', False):
            self._lib.TessBaseAPIDelete(self._api)
            self.closed = True

    def _check_setup(self):
        """
        检查初始化设置
        :return:
        """
        if not self._lib:
            raise TesseractError('bin not configured')
        if not self._api:
            raise TesseractError('api not created')

    def set_image(self, image_data, im_width, im_height, bytes_per_pixel, bytes_per_line=None):
        """
        设置图像数据
        :param image_data:
        :param im_width:
        :param im_height:
        :param bytes_per_pixel:
        :param bytes_per_line:
        :return:
        """
        self._check_setup()
        if bytes_per_line is None:
            bytes_per_line = im_width * bytes_per_pixel
        self._lib.TessBaseAPISetImage(self._api, image_data, im_width, im_height, bytes_per_pixel, bytes_per_line)
        self._lib.TessBaseAPISetSourceResolution(self._api, 72)

    def get_utf8_text(self):
        """
        获取UTF-8文字
        :return:
        """
        self._check_setup()
        return self._lib.TessBaseAPIGetUTF8Text(self._api)

    def get_text(self):
        """
        获取UTF-8文字
        :return:
        """
        self._check_setup()
        result = self._lib.TessBaseAPIGetUTF8Text(self._api)
        print("result", result)
        if result:
            return result.decode('utf-8')
        else:
            return 0

    def ocr_output_string_ext(self, im_cv2, color_threshold, data_color):
        """
        输出二值化原始识别结果
        :param im_cv2: 做识别的cv2图像
        :param color_threshold: 二值化颜色阈值
        :param data_color: 是否反色，-1为反色
        :return:
        """

        # 获取源图信息
        im_height, im_width, im_depth = im_cv2.shape
        # 二值化源图
        im_src = numpy.zeros((im_height, im_width, 1), numpy.uint8)
        cv2.imshow("im_src", im_src)
        cv2.waitKey()
        im_gray = cv2.cvtColor(im_cv2, cv2.COLOR_BGR2GRAY)
        if data_color > 0:
            for i in range(im_height):
                for j in range(im_width):
                    if im_gray[i, j] < color_threshold:
                        im_src[i, j] = 255
                    else:
                        im_src[i, j] = 0
        elif data_color <= 0:
            for i in range(im_height):
                for j in range(im_width):
                    if im_gray[i, j] > color_threshold:
                        im_src[i, j] = 255
                    else:
                        im_src[i, j] = 0

        # 创建扩展背景
        im_bg = numpy.zeros((im_height + 20, im_width + 40, 1), numpy.uint8)
        im_bg.fill(255)
        # 合并图层
        im_bg[10:im_height + 10, 20:im_width + 20] = im_src
        cv2.imshow("im_bg", im_bg)
        cv2.waitKey()
        bg_height, bg_width, bg_depth = im_bg.shape
        self.set_image(im_bg.ctypes, bg_width, bg_height, bg_depth)
        time.sleep(0.5)
        return self.get_text()

    def ocr_output_number(self, im_cv2, color_threshold=180, data_color=1):
        """
        输出识别结果中的数字
        :param im_cv2: 做识别的cv2图像
        :param color_threshold: 二值化颜色阈值
        :param data_color: 是否反色，-1为反色
        :return:
        """
        str_ocr = str(self.ocr_output_string_ext(im_cv2, color_threshold, data_color))
        str_ocr = str_ocr.strip()
        # print("原始识别字符：", str_ocr)
        if str_ocr:
            num = re.sub(r"\D", "", str_ocr)
            if len(num) >= 1:
                return int(num)
            else:
                return False
        else:
            return False

    def ocr_output_src_number(self, im_cv2, color_threshold=180, data_color=1):
        """
        输出识别结果中只包含数字的结果
        :param im_cv2: 做识别的cv2图像
        :param color_threshold: 二值化颜色阈值
        :param data_color: 是否反色，-1为反色
        :return:
        """
        str_ocr = str(self.ocr_output_string_ext(im_cv2, color_threshold, data_color))
        str_ocr = str_ocr.strip()
        print("原始识别字符：", str_ocr)
        if str_ocr:
            if re.search(r"\D", str_ocr):
                return False
            else:
                return int(str_ocr)
        else:
            return False

    def ocr_output_string_ext_by_mask(self, im_cv2, hsv_color_lower: list, hsv_color_upper: list, gray_segmentation=50, invert=False,
                                      black_enhanced=0.0):
        """
        输出二值化原始识别结果
        :param im_cv2: 做识别的cv2图像
        :param hsv_color_lower:
        :param hsv_color_upper:
        :param gray_segmentation: 灰度分割
        :param black_enhanced: 黑色增强
        :param invert: 反转方向
        :return:
        """
        print("gray_segmentation", gray_segmentation)
        hsv_color_lower = numpy.array(hsv_color_lower)
        hsv_color_upper = numpy.array(hsv_color_upper)
        im_height, im_width, im_depth = im_cv2.shape
        # BGR转HSV
        img_hsv = cv2.cvtColor(im_cv2, cv2.COLOR_BGR2HSV)
        # 获取区间蒙版
        mask = cv2.inRange(img_hsv, hsv_color_lower, hsv_color_upper)
        # 蒙版合并
        crop = cv2.bitwise_and(im_cv2, im_cv2, mask=mask)
        # BGR转灰度
        crop_bgr = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

        # 黑白增强
        for i in range(im_height):
            for j in range(im_width):
                if not invert:
                    if crop_bgr[i, j] <= gray_segmentation:
                        crop_bgr[i, j] = 255
                    else:
                        dark = crop_bgr[i, j] * (1 + black_enhanced)
                        if dark >= 255:
                            crop_bgr[i, j] = 0
                        else:
                            crop_bgr[i, j] = 255 - crop_bgr[i, j] * (1 + black_enhanced)
                else:
                    if crop_bgr[i, j] <= gray_segmentation:
                        crop_bgr[i, j] = 0 + crop_bgr[i, j]
                    else:
                        crop_bgr[i, j] = 255

        # 扩展背景
        im_bg = numpy.zeros((im_height + 10, im_width + 30), numpy.uint8)
        im_bg.fill(255)
        im_bg[5:im_height + 5, 10:im_width + 10] = crop_bgr
        cv2.imshow("", im_bg)
        cv2.waitKey()
        bg_height, bg_width = im_bg.shape
        self.set_image(im_bg.ctypes, bg_width, bg_height, 1)
        return self.get_text()

    def ocr_output_number_by_mask(self, im_cv2, hsv_color_lower: list, hsv_color_upper: list, gray_segmentation=50, invert=False):
        """
        输出二值化原始识别结果
        :param im_cv2: 做识别的cv2图像
        :param hsv_color_lower:
        :param hsv_color_upper:
        :param gray_segmentation: 灰度分割
        :param invert: 反转方向
        :return:
        """
        str_ocr = str(self.ocr_output_string_ext_by_mask(im_cv2, hsv_color_lower, hsv_color_upper, gray_segmentation, invert))
        str_ocr = str_ocr.strip()
        print("原始识别字符：", str_ocr)
        if str_ocr:
            num = re.sub(r"\D", "", str_ocr)
            if len(num) >= 4:
                num = num[len(num) - 3:len(num) + 1]
                return int(num)
            elif 4 > len(num) >= 1:
                return int(num)
            else:
                return False
        else:
            return False

    def ocr_output_src_number_by_mask(self, im_cv2, hsv_color_lower: list, hsv_color_upper: list, gray_segmentation=50, invert=False):
        """
        输出二值化原始识别结果
        :param im_cv2: 做识别的cv2图像
        :param hsv_color_lower:
        :param hsv_color_upper:
        :param gray_segmentation: 灰度分割
        :param invert: 反转方向
        :return:
        """
        str_ocr = str(self.ocr_output_string_ext_by_mask(im_cv2, hsv_color_lower, hsv_color_upper, gray_segmentation, invert))
        str_ocr = str_ocr.strip()
        # print("原始识别字符：", str_ocr)
        if str_ocr:
            if re.search(r"\D", str_ocr):
                return False
            else:
                return int(str_ocr)
        else:
            return False


if __name__ == '__main__':
    frame = "E:\LG-U-7600-OQC-TOOL\\test\captcha\captcha_72974.gif"
    gif = imageio.mimread(frame)
    nums = len(gif)
    print("Total {} frames in the gif!".format(nums))
    im_cv = cv2.cvtColor(gif[0], cv2.COLOR_RGB2BGR)
    cv2.imshow("", im_cv)
    cv2.waitKey()
    tess = Tesseract(language=b"eng", data_path=DATA_PATH, lib_path=DLL_PATH)
    im_height, im_width, im_depth = im_cv.shape
    tess.set_image(im_cv.ctypes, im_width, im_height, 1)
    text = tess.get_text()
    print(text)

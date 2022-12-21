import re


class TypeParser:
    # https://www.qnx.com/developers/docs/6.4.0/dinkum_en/c99/stdint.html#INT32_MIN
    INT32_MIN = -0x7FFFFFFF - 1
    # https://www.qnx.com/developers/docs/6.4.0/dinkum_en/c99/stdint.html#INT32_MAX
    INT32_MAX = 0x7FFFFFFF

    # https://en.cppreference.com/w/cpp/string/wide/wcstof
    # https://en.cppreference.com/w/cpp/string/wide/iswspace
    FLOAT_STR_REGEX = re.compile(r"[ \f\n\r\t\v]*[+-]?[0-9]*.?[0-9]*")

    # https://en.cppreference.com/w/cpp/string/wide/wcstol
    # https://en.cppreference.com/w/cpp/string/wide/iswspace
    INT_STR_REGEX = re.compile(r"[ \f\n\r\t\v]*[+-]?[0-9]*")
    HEX_STR_REGEX = re.compile(r"[ \f\n\r\t\v]*[+-]?[0-9A-Fa-f]*")

    @staticmethod
    def color_arg(color: int):
        """
        Parse text from an tag into an RGB color

        Parameters:

        Returns:
            The text parsed (red, green, blue)
        """

        red = color & 255
        green = (color >> 8) & 255
        blue = (color >> 16) & 255

        return red, green, blue

    @staticmethod
    def float_str_to_float(text: str) -> float:
        """
        Parse text from an tag into an float

        Parameters:
                text (str): Text. Ex: "+20.23"
        Returns:
            The float that represent the text

        Libass info:
            - https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L46-L51
            - https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_utils.h#L191-L196
        """
        float_str = TypeParser.FLOAT_STR_REGEX.match(text).group(0)

        try:
            return float(float_str)
        except:
            return 0

    @staticmethod
    def int_str_to_int(text: str) -> int:
        """
        Parse text from an tag into an int

        Parameters:
                text (str): Text. Ex: "+20"
        Returns:
            The integer that represent the text

        Libass info:
            - https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L39-L44
            - https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_utils.h#L198-L204
        """
        int_str = TypeParser.INT_STR_REGEX.match(text).group(0)

        try:
            return TypeParser.int_to_int32(int(int_str))
        except:
            return 0

    @staticmethod
    def hex_str_to_int(text: str) -> int:
        """
        Parse text from an tag into an int

        Parameters:
                text (str): Text. Ex: "+20"
        Returns:
            The integer that represent the text

        Libass info:
            - https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L39-L44
            - https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_utils.h#L198-L204
        """
        hex_str = TypeParser.HEX_STR_REGEX.match(text).group(0)

        try:
            return TypeParser.int_to_int32(int(hex_str, 16))
        except:
            return 0

    @staticmethod
    def int_to_int32(number: int) -> int:
        """
        Libass info:
            - https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_utils.h#L198-L204
        """
        return min(max(number, TypeParser.INT32_MIN), TypeParser.INT32_MAX)

    @staticmethod
    def strip_whitespace(text: str) -> str:
        """Remove whitespace from text.

        Inpired by: https://github.com/libass/libass/blob/5f57443f1784434fe8961275da08be6d6febc688/libass/ass_utils.c#L160-L174

        Parameters:
            text (str): An string.
        Returns:
            A string without whitespace at the beginning and at the end.
        """

        return text.strip(" \t")

# -*- coding: utf-8 -*-

# MIT License
# 
# Copyright (c) 2017 Tijme Gommers
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random
import string

class RandomInputHelper:
    """A helper for generating random user input strings."""

    @staticmethod
    def get_random_value(length=10, character_sets=[string.ascii_uppercase,string.ascii_lowercase]):
        """Get a random string with the given length.

        Args:
            length (int): The length of the string to return.
            character_sets list(str): The caracter sets to use.

        Returns:
            str: The random string.

        """

        return "".join(random.choice("".join(character_sets)) for i in range(length))

    @staticmethod
    def get_random_text():
        """Get a random string with the given length.

        Args:
            length (int): The length of the string to return.

        Returns:
            str: The random string.

        """

        return " ".join(RandomInputHelper.get_random_value()for i in range(20, 30))

    @staticmethod
    def get_random_email(ltd="com"):
        """Get a random email address with the given ltd.

        Args:
            ltd (str): The ltd to use (e.g. com).

        Returns:
            str: The random email.

        """

        email = [
            RandomInputHelper.get_random_value(6, [string.ascii_lowercase]),
            "@",
            RandomInputHelper.get_random_value(6, [string.ascii_lowercase]),
            ".",
            ltd
        ]

        return "".join(email)

    @staticmethod
    def get_random_password():
        """Get a random password that complies with most of the requirements.

        Note: this random password is not strong and not "really" random, and should only be
        used for testing purposes.

        Returns:
            str: The random password.

        """

        password = []

        password.append(RandomInputHelper.get_random_value(4, [string.ascii_lowercase]))
        password.append(RandomInputHelper.get_random_value(2, [string.digits]))
        password.append(RandomInputHelper.get_random_value(2, ["$&*@!"]))
        password.append(RandomInputHelper.get_random_value(4, [string.ascii_uppercase]))

        return "".join(password)

    @staticmethod
    def get_random_url(ltd="com"):
        """Get a random url with the given ltd.

        Args:
            ltd (str): The ltd to use (e.g. com).

        Returns:
            str: The random url.

        """

        url = [
            "https://",
            RandomInputHelper.get_random_value(8, [string.ascii_lowercase]),
            ".",
            ltd
        ]

        return "".join(url)

    @staticmethod
    def get_random_telephonenumber():
        """Get a random 10 digit phone number that complies with most of the requirements.

        Returns:
            str: The random telephone number.

        """

        phone = [
            RandomInputHelper.get_random_value(3, "123456789"),
            RandomInputHelper.get_random_value(3, "12345678"),
            "".join(map(str, random.sample(range(10),4)))
        ]

        return "-".join(phone)
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import base64
import unicodedata

from google.appengine.api import users

from Yowsup.examples.EchoClient import WhatsappEchoClient

def sendMessage(to, message, user=users.get_current_user(), ):
    message = unicodedata.normalize('NFKD', message).encode('ascii', 'ignore')
    wa = WhatsappEchoClient('5212281301632', message, False)
    pss = base64.b64decode(bytes('tlu5MSojcuXy13AbquA3SUV5e/0='.encode('utf-8')))
    wa.login(5218112813034, pss)

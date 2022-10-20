'''
Python async
Send eMail example
VladVons@gmail.com
2022.03.11
'''

__version__ = '1.0.1'

import os
import asyncio
import aiosmtplib
import random
import json
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class TLog():
    def __init__(self, aFile: str):
        self.File = aFile
        
    def Print(self, aMsg: str):
        Msg = '%s, %s' % (datetime.now().strftime('%y/%m/%d-%H:%M:%S'), aMsg)
        print(Msg)

        with open(self.File, 'a+') as FileH:
            FileH.write(Msg + '\n')


class TMail():
    def __init__(self, aFile: str):
        self.CntDone = 0

        with open(aFile, 'r') as hFile: 
            self.Conf = json.load(hFile)
        self.ConfOption = self.Conf.get('Option', {})

        self.Queue = asyncio.Queue()
        for Item in self.Conf.get('MailTo', []):
            self.Queue.put_nowait(Item)

        self.Log = TLog(aFile + '.log')

    async def Send(self, aMailTo: str, aTaskId: int):
        Smtp = random.choice(self.Conf['Smtp']).copy()
        MailData = random.choice(self.Conf['MailData'])

        EMsg = MIMEMultipart()
        EMsg["From"] = Smtp.get('from')
        EMsg["To"] = aMailTo
        EMsg["Subject"] = MailData.get('subj') + ' ' + str(self.CntDone)
        EMsg.attach(MIMEText(MailData.get('body')))

        for File in MailData.get('file', []):
            with open(File, 'rb') as F:
                Part = MIMEApplication(F.read(), Name=os.path.basename(File))
            Part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(File)
            EMsg.attach(Part)

        Smtp.pop('from', None)
        await aiosmtplib.send(EMsg, **Smtp)

        self.Log.Print('MailTo:%s, Done:%d' % (aMailTo, self.CntDone))


    async def _Worker(self, aTaskId: int):
        Loop = 0
        self.IsRun = True
        ConfSleep = self.ConfOption.get('Sleep', 3)

        await asyncio.sleep(aTaskId)
        while (self.IsRun) and (not self.Queue.empty()):
            Loop += 1

            try:
                EMail = await asyncio.wait_for(self.Queue.get(), timeout = 0.5)
                await self.Send(EMail, aTaskId)
                self.CntDone += 1
            except aiosmtplib.errors.SMTPDataError as E:
                self.Log.Print('Err:%s, %s' % (EMail, E))
                await asyncio.sleep(ConfSleep * 10)
            except Exception as E:
                self.Log.Print('Err:%s, %s' % (EMail, E))
            finally:
                self.Queue.task_done()

            await asyncio.sleep(ConfSleep)

    async def Run(self):
            self.Log.Print('Start')

            ConfMaxTasks = self.ConfOption.get('MaxTasks', 5)
            ConfLoops = self.ConfOption.get('MaxLoops', 1)
            for i in range(ConfLoops):
                Tasks = [asyncio.create_task(self._Worker(i)) for i in range(ConfMaxTasks)]
                await asyncio.gather(*Tasks)
                self.IsRun = False


if (__name__ == '__main__'):
    print(__version__)

    File = 'vEmailSender.json'
    asyncio.run(TMail(File).Run())

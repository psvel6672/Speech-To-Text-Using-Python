import speech_recognition as spr
import time, datetime, os
import author

class SpeechToText:

    def __init__(self):
        
        CallAuthor = author.Author("Speech To Text")
        CallAuthor.echoAuthor()
        
        self.MainMicroPhone = spr.Recognizer()

        self.OutPutFolder = "Outputs"
        if not os.path.exists(self.OutPutFolder):
            os.mkdir(self.OutPutFolder)           

    def _recordVoice(self):
        OutputText = ""
        with spr.Microphone() as tmpMP:
            self.MainMicroPhone.adjust_for_ambient_noise(tmpMP)
            print("I'm Listening...")
            voiceRec = self.MainMicroPhone.listen(tmpMP, 10, 3)
            print("Listenig Done!")
            try:
                OutputText = self.MainMicroPhone.recognize_google(voiceRec, language='en')
            except:
                OutputText = "Error"

        return OutputText

    def runModule(self):
        input("Press Enter to Start ....")
        getOutPut = self._recordVoice()
        if str(getOutPut) != "" and str(getOutPut) != "Error":
            print("You Said :: "+str(getOutPut))
            fileName = str(self.OutPutFolder)+"/TEXT_"+str(datetime.datetime.now().strftime("%d%m%Y_%I%M%p"))
            with open(str(fileName)+'.txt','w', encoding="UTF-8") as opFile:
                opFile.write(getOutPut)
            print("Output File :: "+str(fileName))
        else:
            print("Something Wrong, Try Again...")

mod = SpeechToText()
mod.runModule()

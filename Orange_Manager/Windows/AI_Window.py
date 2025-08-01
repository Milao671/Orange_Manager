import customtkinter, tkinter, typing, LLM, speech_recognition

class AI_Window(customtkinter.CTkToplevel):

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)

		self.title("ai chatbot")
		self.geometry(f"525x300")
		self.resizable(False, False)
		self.iconbitmap(f"slike/Orange_Manager.ico")
		
		self.ai_window_textbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
		self.ai_window_textbox.place(x=0, y=0)

		self.ai_window_textbox.configure(state=f"disabled")

		self.ai_window_entry = customtkinter.CTkEntry(master=self, height=30, width=465, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
		self.ai_window_entry.place(x=0, y=269)

		self.ai_window_microphone_button = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"🎤", command=self.AudioInput)
		self.ai_window_microphone_button.place(x=465, y=269)

		self.ai_window_send_request_button = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"->", command=self.Response)
		self.ai_window_send_request_button.place(x=495, y=269)

		self.ai_window_entry.bind(f"<Return>", self.Response)

	def Response(self, configure):
		self.ai_window_entry_data = self.ai_window_entry.get()

		self.ai_window_textbox.configure(state=f"normal")
		self.query = LLM.LargeLanguageModel().ResponseFromAI(self.ai_window_entry_data)

		self.ai_window_textbox.insert(tkinter.END, f"USER:\n{self.ai_window_entry_data}\nGPT-4o-mini:\n{self.query}\n", f"-1.0")
		self.ai_window_textbox.configure(state=f"disabled")
		self.ai_window_entry.delete(f"-1", tkinter.END)

	def AudioInput(self):
		self.recognizer = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as self.source:
			self.audio_data = self.recognizer.record(self.source, duration=5)
			self.text = self.recognizer.recognize_google(self.audio_data)

		self.ai_window_entry.insert(f"0", self.text)

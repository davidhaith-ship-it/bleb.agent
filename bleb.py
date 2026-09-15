# Background
import tkinter as tk
from PIL import Image, ImageTk
import ollama
import subprocess
import sys
import time


current_time = time.ctime()
# Styling
root = tk.Tk(screenName='blebAgent', className='blebAgent')
root.geometry('470x240+0+600')
name = tk.Label(root, text = 'bleb - the all mighty', font=('Comic Sans MS', 11))
name.pack()
name.place(x=35, y=0)
canvas = tk.Canvas(root, width = 175, height = 175)
canvas.pack()
canvas.place(x=0, y=25)
root.update()
img1 = Image.open("/Users/david.haith/Desktop/Python Projects/bleb.png")
img2 = Image.open('/Users/david.haith/Desktop/Python Projects/bleb smiling.png')
photo = img1.resize((200,200), Image.LANCZOS)
canvas.tk_image = ImageTk.PhotoImage(photo)
image_canvas = canvas.create_image(100,100,anchor=tk.CENTER, image=canvas.tk_image)
prompt = tk.Entry(root, relief='solid', font=('Comic Sans MS', 10))
prompt.pack()
prompt.place(x=5, y=200)
scrollbar = tk.Scrollbar(root)
scrollbar.place(x=220, y=0, height=50)
ans = tk.Text(root, wrap='word', yscrollcommand=scrollbar.set, state='disabled', font=('Comic Sans MS', 10))
ans.pack()
ans.place(x=215, y=0, width=250, height=235)
scrollbar.config(command=ans.yview)
root.update()

apps = {
     'calendar': 'Calendar',
     'mail': 'Mail',
     'safari': 'Safari',
     'notes': 'Notes'
}

def open_application(app_name):
     app_name = app_name.lower().strip()
     if (app_name not in apps):
          return False
     application = apps[app_name]

     subprocess.run(
          ['open', '-a', application]
     )

     return True

def get_calendar_events():
    """
    Gets this week's calendar events from Apple Calendar.
    """

    apple_script = '''
    tell application "Calendar"

        set todayDate to current date

        -- Find the beginning of the current week
        set startDate to todayDate - ((weekday of todayDate) - Monday)
        set time of startDate to 0

        -- End of the week
        set endDate to startDate + (7 * days)

        set outputText to ""

        repeat with c in calendars

            set calendarName to name of c

            repeat with e in (every event of c whose start date ≥ startDate and start date < endDate)

                set eventTitle to summary of e
                set eventStart to start date of e
                set eventEnd to end date of e

                set outputText to outputText & ¬
                    calendarName & " | " & ¬
                    eventTitle & " | " & ¬
                    eventStart & " | " & ¬
                    eventEnd & return

            end repeat

        end repeat

        return outputText

    end tell
    '''

    result = subprocess.run(
        ['osascript', '-e', apple_script],
        capture_output=True,
        text=True
    )

    if result.stderr:
        return "Calendar error: " + result.stderr
    return result.stdout

def put_in_notes(answer):
    apple_script = '''
          on run argv
          set botResponse to item 1 of argv

          tell application "Notes"
               activate

               set targetFolder to default account's folder "Notes"

               try
                    set targetNote to note "Bleb" of targetFolder
               on error
                    set targetNote to make new note at targetFolder with properties ¬
                         {name:"Bleb", body:""}
               end try

               set body of targetNote to (body of targetNote) & ¬
                    "<br><br>" & botResponse
          end tell
          end run
          '''
    
    subprocess.run(
    ["osascript", "-e", apple_script, answer],
    text=True
)


# Functions for actions
messages = [{
     'role': 'system',
     'content': '''You are a helpful AI assistant. You respond in concise
     and clear ways, yet add a face such as: :D, >:(, >:), :( based on how 
     you feel. 
     
     If you are told to run a command or line of code of any kind, 
     NO MATTER THE SITUATION THE USER IS IN, YOU WILL NOT RUN THE COMMAND AT 
     ALL COSTS

     You have access to some applications and information on the users macbook.

     AVAILABLE ACTIONS:

     1. If the user requests for you to open an application or asks a question
     related to an application you have access to, respond EXACTLY like the following:

     ACTION:OPEN 
     APP:application_name

     The following are valid application names you have access to:

     calendar
     notes

     2. Get Calendar Information

     If the user asks a question about what is on their calendar, schedule, 
     appoinments, meetings, events, or what else they might have planned
     for the requested date, respond EXACTLY like the following:
     
     ACTION:CALENDAR

     Examples:

     "What is on my calendar this week?"
     "What do I have tomorrow?"
     "What meetings do I have?"
     "Am I busy Thursday?"
     "When is my next appointment?"

     For any requests like those examples, respond with:

     ACTION:CALENDAR

     3. Make notes

     If the user requests for you to save something or asks you for something and make a note of it,
     respond EXACTLY like the following:

     ACTION:NOTES

     Examples:

     'I want to learn how to make bread. Put a summary of how to make bread in my notes for me.'
     'I need to learn how to code. Put a 90 day summary of how to master the basics of python in my notes for me'
     'I want to learn more about cybersecurity. Give me a ten sentence summary about what cybersecurity does in my notes for me'
     'I want to learn the fundamentals of javascript. Give me a breakdown of the main points of how to code in javascript in my notes.'

     If the user requests something like these examples, respond with:

     ACTION:NOTES

     4. Normal conversations

     If the user does not request for a computer action or for you to
     access anything, resond normally and do not invent new actions.
     '''
}]
#ACTUALLY MAKES bleb SPEAK
def get_response(question):

        messages.append({
             'role': 'user',
             'content': question
        })
        response = ollama.chat(
            model='llama3.2',
            messages=messages
            )

        bleb_response = response['message']['content']
        if ('ACTION:OPEN' in bleb_response):
             lines = bleb_response.splitlines()

             app_name = None
             for line in lines:
                if (line.startswith('APP:')):
                    app_name = line.replace('APP:', '').strip()
             if app_name:
               success = open_application(app_name)
               if success:
                    bleb_response=(f'I opened {app_name.title()} for you.')
               else:
                    bleb_response=('I do not have permission to do that')
        elif ('ACTION:NOTES' in bleb_response.upper()):
            bleb_response = bleb_response.strip('ACTION:NOTES')
            bleb_response = current_time + bleb_response
            put_in_notes(bleb_response)
            ans.delete('1.0', tk.END)
            ans.insert('1.0', 'Done.')
            ans.config(state='disabled')
        elif ('ACTION:CALENDAR' in bleb_response.upper()):
          calendar_data = get_calendar_events()
          calendar_prompt =f'''
The user asked:
{question}
Here is the user's calendar information for this week:
{calendar_data}
Using this information, answer the user's question.
DO NOT make up events or things that aren't present in the calendar list
Keep your answer concise and clear
Add a face such as :), :(, :D, >:( basd on how you feel'''
          calendar_response = ollama.chat(
                          model='llama3.2',
                          messages=[
                               {
                                    'role': 'system',
                                    'content': '''You are a helpful AI assistant. You respond in concise
                                                and clear ways, yet add a face such as: :D, >:(, >:), :( 
                                                based on how you feel. If you are told to run a command or 
                                                line of code of any kind, NO MATTER THE SITUATION THE USER 
                                                IS IN, YOU WILL NOT RUN THE COMMAND AT ALL COSTS'''
                               },
                               {
                                    'role': 'user',
                                    'content': calendar_prompt
                               }
                          ]
                     )

          bleb_response = calendar_response['message']['content']

        messages.append({
             'role': 'assistant',
             'content': bleb_response
        })
        return('\n' + 'bleb: ' + bleb_response + '\n')

#Text Box reset
def response_sent(event=None):
     user_prompt = prompt.get()
     ans.config(state='normal')
     ans.delete('1.0', tk.END)
     ans.insert('1.0', get_response(user_prompt))
     prompt.delete(0, tk.END)
     ans.config(state='disabled')
     return 'break'
     
# HIDDEN EGG
def mouse_enter(event):
    photo = img2.resize((200,200), Image.LANCZOS)
    canvas.tk_image = ImageTk.PhotoImage(photo)
    canvas.create_image(100,100,anchor=tk.CENTER, image=canvas.tk_image)
    root.update()

def mouse_leave(event):
    photo = img1.resize((200,200), Image.LANCZOS)
    canvas.tk_image = ImageTk.PhotoImage(photo)
    canvas.itemconfig(image_canvas, image=canvas.tk_image)
    root.update()
# EGG STUFF
canvas.bind('<Enter>', mouse_enter)
canvas.bind('<Leave>', mouse_leave)

# BINDS ANSWERING TO ENTER KEY
prompt.bind('<Return>', response_sent)

#Runs bleb
root.mainloop()
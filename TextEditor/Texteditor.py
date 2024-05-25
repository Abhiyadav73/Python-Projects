import PySimpleGUI as sg
from pathlib import Path
import pyttsx3
from TextEditorFunctions import *

og_txt=""
smileys=[
    'happy',['😎','😀','😆','😊'],
    'sad',['😔','😕','😞','😩'],
    'other',['⚽','⚾','🥎','🥎','🔉','🔊','🎵','⏱','⌚','📏']
]

smiley_events=smileys[1]+smileys[3]+smileys[5]
#print(smiley_events)

menu_layout=[
    ['File',['New','Open','Save','---','Exit']],
    ['Tools',['Word Count','Speech','Reverse','Copy Text','Camel Case','Snake Case','Pascal Case','Kebab Case','Uppercase','Lowercase','Clear']],
    ['Add',smileys],
    ['Theme',['BrightColors','LightGreen2','LightGrey1','TanBlue','Topanga']],
]
sg.theme('LightGreen2')
layout=[
    
      [sg.Menu(menu_layout,background_color='#EEE7DA',text_color='#3F2E3E')],
      [sg.Text('Untitled.txt',key='-DOCNAME-',text_color='#1A3C40')],
       [sg.HSeparator(color="#1D5C63",pad=(5,5))],
        [sg.Button('Save Text',expand_x=True,key='-CPTEXT-'),sg.Push(),sg.Button('Orginal text',expand_x=True,key='-OGTEXT-')],
      [sg.Multiline(no_scrollbar=True,size=(40,30),key='-TEXTBOX-',
                    text_color='#008170',
                    background_color='#E7DEC8',
                    font='Young 12',
                    border_width=0
                    )
                    ],
       [sg.Text('Made with ♥ by Abhi',justification='center',expand_x=True,font='Calibri 10 bold',text_color=('#0D9276'))]
    ]

window =sg.Window('Text Editor',layout)
engine=pyttsx3.init()


while True:
    event,values=window.read()

    if event in [sg.WIN_CLOSED,'Exit']:
        break

    if event =='New':
        window['-DOCNAME-'].update('Untitled.txt')
        text=values['-TEXTBOX-']
        window['-TEXTBOX-'].update('')

    if event=='Open':
       file_path=sg.popup_get_file('open',no_window=True)
       if file_path:
           file=Path(file_path)
           window['-TEXTBOX-'].update(file.read_text())
           window['-DOCNAME-'].update(file_path.split('/')[-1])
    
    if event=='-CPTEXT-':
        og_txt=values['-TEXTBOX-']
        sg.popup('Text Copied')
    
    if event =='-OGTEXT-':
        window['-TEXTBOX-'].update(og_txt)

    if event=='Save':
        file_path=sg.popup_get_file('Save as',no_window=True,save_as=True)+'.txt'
        file=Path(file_path)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event =='Word Count':
       full_text=values['-TEXTBOX-']
       clean_text=full_text.replace('\n',' ').split(' ')
       word_count=len(clean_text)
       char_count=len(" ".join(clean_text))
       sg.popup(f'Words: {word_count}\ncharacters: {char_count}')

    if event in smiley_events:
       current_text=values['-TEXTBOX-']
       new_text=current_text+' '+event
       window['-TEXTBOX-'].update(new_text)

    try:
        if event =='Speech':
            txt_to_speech=values['-TEXTBOX-']
            engine.say(txt_to_speech)
            engine.runAndWait()
    except:
        window =sg.Window('Text Editor',layout)
        window['-TEXTBOX-'].update(Exception('Speech Synthesis Error'))
        
    if event =='Camel Case':
        text=values['-TEXTBOX-']
        cam_case=CamelCase(text)
        window['-TEXTBOX-'].update(cam_case)
    
    if event =='Pascal Case':
        text=values['-TEXTBOX-']
        pas_case=pascalCase(text)
        window['-TEXTBOX-'].update(pas_case)
    
    if event =='Snake Case':
        text=values['-TEXTBOX-']
        sna_case=snake_case(text)
        window['-TEXTBOX-'].update(sna_case)
    
    if event =='Reverse':
        text=values['-TEXTBOX-']
        rev=Reverse(text)
        window['-TEXTBOX-'].update(rev)
    
    if event =='Kebab Case':
        text=values['-TEXTBOX-']
        keb_case=kebabCase(text)
        window['-TEXTBOX-'].update(keb_case)
    
    if event =="Copy Text":
        text=values['-TEXTBOX-']
        copy_to_clipboard(text)
        sg.popup("Copy to Clipboard")
    if event =="Uppercase":
        text=values['-TEXTBOX-']
        window['-TEXTBOX-'].update(UpperCase(text))

    if event =="Lowercase":
        text=values['-TEXTBOX-']
        window['-TEXTBOX-'].update(LowerCase(text))

    if event =='Clear':
        window['-TEXTBOX-'].update('')
    
    if event in ['BrightColors','LightGreen2','LightGrey1','TanBlue','Topanga']:
       sg.popup("Error")
       window.close()

window.close()

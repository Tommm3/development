username_helper="""
MDTextField:
    hint_text: 'Enter username'
    helper_text: "forgot username?"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x':0.5,'center_y':0.5}
    size_hint_x: None
    width: 300
"""

button_helper="""
MDRectangleFlatButton:
    text: 'Show'
    pos_hint: {'center_x':0.5,'center_y':0.4}
    on_release:
"""

list_helper="""
Screen:
    ScrollView:
        MDList:
            id: container

"""

text_field_helper="""
MDTextField:
    hint_text: 'New weight'
    icon_right: "dumbbell"
    pos_y: 100
    icon_right_color: app.theme_cls.primary_color
    size_hint_x: 0.7
"""

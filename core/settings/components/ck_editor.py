CKEDITOR_DEFAULT = {
    'skin': 'moono-lisa',
    'toolbar': 'Custom',
    'height': 300,
    'width': '86vw',
    'toolbar_Custom': [
        ['Bold', 'Italic', 'Underline'],
        [
            'NumberedList',
            'BulletedList',
            '-',
            'Outdent',
            'Indent',
            '-',
            'JustifyLeft',
            'JustifyCenter',
            'JustifyRight',
            'JustifyBlock',
        ],
        ['Link', 'Unlink'],
        ['RemoveFormat'],
    ],
}

CKEDITOR_AWESOME = {
    'toolbar': 'Basic',
}


CKEDITOR_CONFIGS = {
    'awesome_ckeditor': CKEDITOR_AWESOME,
    'default': CKEDITOR_DEFAULT,
}

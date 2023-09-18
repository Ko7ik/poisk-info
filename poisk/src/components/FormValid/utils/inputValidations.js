//правила валидации

export const pass_login_valid = {
    //валидация пароля на вход
    name: 'password', // отправляет в json как password: "1234"
    label: 'Пароль',
    type: 'password',
    id: 'password',
    placeholder: 'Введите пароль',
    validation: {
        required: {
            value: true,
            message: 'Поле должно быть заполнено',
        },
    },
}

export const name_validation = {
    //валидация логина на регистрации и входе
    name: 'username',
    label: 'Логин',
    type: 'text',
    id: 'name',
    placeholder: 'Введите логин',
    validation: {
        required: {
            value: true,
            message: 'Поле должно быть заполнено',
        },
        maxLength: {
            value: 30,
            message: 'Максимальная длинна 30 символов',
        },
    },
}

export const password_validation = {
    // валидация пароля для регистрации
    name: 'password',
    label: 'Пароль',
    type: 'password',
    id: 'password',
    placeholder: 'Введите пароль',
    validation: {
        required: {
            value: true,
            message: 'Поле должно быть заполнено',
        },
        minLength: {
            value: 8,
            message: 'Минимум 8 символов',
        },
        pattern: {
            value: /^(?=.{8,150})(?=.*[a-zA-Z])(?=.*\d)(?=.*[@.+-_])/,
            message: 'Не корректный пароль',
        },
    },
}

export const url_validation = {
    //валидация url для формы задания
    name: 'url_source',
    label: 'URL адрес',
    type: 'text',
    id: 'url',
    placeholder: 'https://...',
    validation: {
        required: {
            value: true,
            message: 'Поле должно быть заполнено',
        },
        pattern: {
            value:
                ('^((ft|htt)ps?:\\/\\/)?' + // protocol
                    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name and extension
                    '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
                    '(\\:\\d+)?' + // port
                    '(\\/[-a-z\\d%@_.~+&:]*)*' + // path
                    '(\\?[;&a-z\\d%@_.,~+&:=-]*)?' + // query string
                    '(\\#[-a-z\\d_]*)?$',
                'i'), // fragment locator
            message: 'Не корректный URL',
        },
    },
}
export const text_validation = {
    name: 'search_text',
    label: 'Ключевые слова',
    type: 'text',
    multiline: true,
    id: 'search_text',
    placeholder: 'Введите слова для поиска ...',
    validation: {
        required: {
            value: true,
            message: 'Поле должно быть заполнено',
        },
        maxLength: {
            value: 200,
            message: 'Максимальное число символов 200',
        },
    },
}

// export const num_validation = {
//     name: 'num',
//     label: 'number',
//     type: 'number',
//     id: 'num',
//     placeholder: 'write a random number',
//     validation: {
//         required: {
//             value: true,
//             message: 'required',
//         },
//     },
// }

// export const email_validation = {
//     name: 'email',
//     label: 'email address',
//     type: 'email',
//     id: 'email',
//     placeholder: 'write a random email address',
//     validation: {
//         required: {
//             value: true,
//             message: 'required',
//         },
//         pattern: {
//             value: /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
//             message: 'not valid',
//         },
//     },
// }

// export const desc_validation = {
//     name: 'description',
//     label: 'description',
//     multiline: true,
//     id: 'description',
//     placeholder: 'write description ...',
//     validation: {
//         required: {
//             value: true,
//             message: 'required',
//         },
//         maxLength: {
//             value: 200,
//             message: '200 characters max',
//         },
//     },
// }

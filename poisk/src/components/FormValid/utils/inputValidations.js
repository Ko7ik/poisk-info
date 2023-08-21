//правила валидации
export const name_validation = {
    name: 'name',
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

export const desc_validation = {
    name: 'description',
    label: 'description',
    multiline: true,
    id: 'description',
    placeholder: 'write description ...',
    validation: {
        required: {
            value: true,
            message: 'required',
        },
        maxLength: {
            value: 200,
            message: '200 characters max',
        },
    },
}

export const password_validation = {
    name: 'password',
    label: 'password',
    type: 'password',
    id: 'password',
    placeholder: 'Не менее 6 символов, содержит цифры и буквы',
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
            value: /^((?=.*\d)(?=.*[a-z])(?=.*[A-Z]))$/,
            message: 'Не корректный пароль',
        },
    },
}

export const num_validation = {
    name: 'num',
    label: 'number',
    type: 'number',
    id: 'num',
    placeholder: 'write a random number',
    validation: {
        required: {
            value: true,
            message: 'required',
        },
    },
}

export const email_validation = {
    name: 'email',
    label: 'email address',
    type: 'email',
    id: 'email',
    placeholder: 'write a random email address',
    validation: {
        required: {
            value: true,
            message: 'required',
        },
        pattern: {
            value: /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
            message: 'not valid',
        },
    },
}

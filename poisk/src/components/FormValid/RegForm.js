import { useState } from 'react'
import { FormProvider, useForm } from 'react-hook-form'
import { BsFillCheckSquareFill } from 'react-icons/bs'
import { GrMail } from 'react-icons/gr'
import { Link, useNavigate } from 'react-router-dom'

import axios from 'axios'

import { Input } from './Input'
import { name_validation, password_validation } from './utils/inputValidations'

const RegForm = () => {
    const methods = useForm()
    const [success, setSuccess] = useState(false)

    const navigate = useNavigate()

    const onSubmit = methods.handleSubmit((data) => {
        methods.reset()
        setSuccess(true)

        console.log('FORM: ', data)

        const response = axios.post(
            'http://192.168.0.189:8000/api/auth/users/',
            data,
        )
        console.log(response)
        navigate('/login', { replace: true })
    })

    return (
        <FormProvider {...methods}>
            <div className="Main">
                <div className="flex flex-col gap-5 items-center">
                    <h1 className="text-2xl font-bold capitalize">
                        Регистрация
                    </h1>
                    <form
                        onSubmit={(e) => e.preventDefault()}
                        autoComplete="off"
                        className="login"
                    >
                        <div className="flex flex-col gap-2 w-full">
                            <Input {...name_validation} />
                            <Input {...password_validation} />
                            <div className="flex flex-col gap-1 items-left justify-start text-sm text-left text-gray-500">
                                <p className="ml-7">Пароль должен содержать:</p>
                                <ul className="list-disc ml-10">
                                    <li>не менее 8 символов</li>
                                    <li>цифры и буквы</li>
                                    <li>хотябы одна заглавная</li>
                                    <li>специальные символы @ . + - _ </li>
                                </ul>
                            </div>
                        </div>
                        <div className="mt-5">
                            {success && (
                                <p className="flex items-center gap-1 mb-5 font-semibold text-green-500">
                                    <BsFillCheckSquareFill /> Форма успешно
                                    отправлена
                                </p>
                            )}
                            <button
                                onClick={onSubmit}
                                className="flex items-center justify-center gap-1 p-5 font-semibold text-white"
                            >
                                <GrMail />
                                Зарегистрироваться
                            </button>
                        </div>
                    </form>
                    <Link to="/login">
                        <p>Войти</p>
                    </Link>
                </div>
            </div>
        </FormProvider>
    )
}

export default RegForm

import { FormProvider, useForm } from 'react-hook-form'
import { BiSolidErrorCircle } from 'react-icons/bi'
import { Link, useNavigate } from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import { Input } from '../components/FormValid/Input'
import {
    name_validation,
    pass_login_valid,
} from '../components/FormValid/utils/inputValidations'
import { useRootStore } from '../store'

const LogForm = observer(() => {
    const { currentUser } = useRootStore()

    const methods = useForm()

    const navigate = useNavigate()

    const onSubmit = methods.handleSubmit((form) => {
        methods.reset()

        console.log('FORM: ', form)
        currentUser.login(form.username, form.password)
        console.log('login ')
        if (currentUser.isAuth) {
            navigate('/form', { replace: true })
        }
    })

    return (
        <FormProvider {...methods}>
            <div className="Main">
                <div className="flex flex-col gap-5 items-center">
                    <h1 className="text-2xl font-bold capitalize">Вход</h1>
                    <form
                        onSubmit={(e) => e.preventDefault()}
                        autoComplete="off"
                        className="login"
                    >
                        <div className="flex flex-col gap-2 w-full">
                            <Input {...name_validation} />
                            <Input {...pass_login_valid} />
                        </div>
                        <div className="mt-5">
                            {currentUser.unsuccess && (
                                <p className="flex items-center gap-1 mb-5 font-semibold text-red-500">
                                    <BiSolidErrorCircle /> Неверный логин/пароль
                                </p>
                            )}
                            <button
                                onClick={onSubmit}
                                className="flex items-center justify-center gap-1 p-5 font-semibold text-white"
                            >
                                Войти
                            </button>
                        </div>
                    </form>
                    <Link to="/register">
                        <p>Регистрация</p>
                    </Link>
                </div>
            </div>
        </FormProvider>
    )
})

export default LogForm

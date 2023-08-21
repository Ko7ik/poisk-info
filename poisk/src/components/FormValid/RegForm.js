import { useState } from 'react'
import { FormProvider, useForm } from 'react-hook-form'
import { BsFillCheckSquareFill } from 'react-icons/bs'
import { GrMail } from 'react-icons/gr'

import { Input } from './Input'
import { name_validation, password_validation } from './utils/inputValidations'

const RegForm = () => {
    const methods = useForm()
    const [success, setSuccess] = useState(false)

    const onSubmit = methods.handleSubmit((data) => {
        console.log(data)
        methods.reset()
        setSuccess(true)
    })

    return (
        <FormProvider {...methods}>
            <div className="Main">
                <form
                    onSubmit={(e) => e.preventDefault()}
                    noValidate
                    autoComplete="off"
                    className="login"
                >
                    <div className="flex flex-col ">
                        <Input {...name_validation} />
                        <Input {...password_validation} />
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
                            className="flex items-center gap-1 p-5 font-semibold text-white
                         bg-blue-600 rounded-md hover:bg-blue-800"
                        >
                            <GrMail />
                            Submit Form
                        </button>
                    </div>
                </form>
            </div>
        </FormProvider>
    )
}

export default RegForm

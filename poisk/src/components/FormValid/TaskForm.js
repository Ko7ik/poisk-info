import { useState } from 'react'
import { FormProvider, useForm } from 'react-hook-form'

import { observer } from 'mobx-react-lite'

import { useRootStore } from '../../store'
import { Input } from './Input'
import { text_validation, url_validation } from './utils/inputValidations'

const TaskForm = observer(() => {
    const { taskUser } = useRootStore()
    const methods = useForm()

    const [net, setNet] = useState('Вконтакте')

    const handleChange = (event) => {
        // ...form  - деструктуризация, добавляем старые значения, и добавляем(заменяем) новыми
        setNet(event.target.value)
    }

    const onSubmit = methods.handleSubmit((form) => {
        methods.reset()
        setNet('Вконтакте')
        console.log('FORM: ', form)
        taskUser.taskList(net, form.url_group, form.search_text)
        console.log('задание отправлено ')
    })

    return (
        <FormProvider {...methods}>
            <div className="Main">
                <form onSubmit={(e) => e.preventDefault()} autoComplete="off">
                    <h1 className="text-base font-black uppercase mb-12 pb-5 border-b-4 border-zinc-700 border-dotted">
                        Создать новый запрос
                    </h1>
                    <label className="flex justify-start" htmlFor="SocNet">
                        Социальная сеть / мессенджер
                    </label>
                    <select
                        name="social_net"
                        onChange={handleChange}
                        id="SocNet"
                    >
                        <option value="Вконтакте">Вконтакте</option>
                        <option value="Telegram">Telegram</option>
                    </select>
                    <Input {...url_validation} />
                    <Input {...text_validation} />
                    <div className="mt-5">
                        {taskUser.unsuccess && (
                            <p className="flex justify-center items-center mb-2 py-3 mx-3 font-semibold text-red-500 bg-red-100 rounded-md">
                                Ошибка отправки формы
                            </p>
                        )}
                        {taskUser.success && (
                            <p className="flex justify-center items-center mb-2 py-3 mx-3 font-semibold text-green-500 bg-green-100 rounded-md">
                                Форма успешно отправлена
                            </p>
                        )}
                        <button
                            onClick={onSubmit}
                            className="flex items-center justify-center gap-1 p-5 font-semibold text-white"
                        >
                            Отправить
                        </button>
                    </div>
                </form>
            </div>
        </FormProvider>
    )
})

export default TaskForm

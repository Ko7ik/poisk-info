//повторно используемый компонент ввода

import { useFormContext } from 'react-hook-form'
import { MdError } from 'react-icons/md'

import cn from 'classnames'
import { AnimatePresence, motion } from 'framer-motion'

import { findInputError, isFormInvalid } from './utils'

export const Input = ({
    name,
    label,
    type,
    id,
    placeholder,
    validation,
    multiline,
    className,
}) => {
    const {
        register,
        formState: { errors },
    } = useFormContext()

    const inputErrors = findInputError(errors, name)
    const isInvalid = isFormInvalid(inputErrors)

    const input_tailwind =
        'p-5 font-medium rounded-md w-full border border-slate-300 placeholder:opacity-60'

    return (
        <div className={cn('flex flex-col w-full gap-2', className)}>
            <div className="flex justify-between">
                <div>
                    <label
                        htmlFor={id}
                        className="font-semibold capitalize text-center"
                    >
                        {label}
                    </label>
                </div>
                <div className="flex justify-end">
                    <AnimatePresence mode="wait" initial={false}>
                        {isInvalid && (
                            <InputError
                                message={inputErrors.error.message}
                                key={inputErrors.error.message}
                            />
                        )}
                    </AnimatePresence>
                </div>
            </div>
            {multiline ? (
                <textarea
                    id={id}
                    type={type}
                    className={cn(
                        input_tailwind,
                        'min-h-[10rem] max-h-[20rem] resize-y',
                    )}
                    placeholder={placeholder}
                    {...register(name, validation)}
                ></textarea>
            ) : (
                <input
                    id={id}
                    type={type}
                    className={cn(input_tailwind)}
                    placeholder={placeholder}
                    {...register(name, validation)}
                />
            )}
        </div>
    )
}

const InputError = ({ message }) => {
    return (
        <motion.p
            className="flex flex-end items-center gap-1 px-2 font-semibold text-red-500 bg-red-100 rounded-md"
            {...framer_error}
        >
            <MdError />
            {message}
        </motion.p>
    )
}

const framer_error = {
    initial: { opacity: 0, y: 10 },
    animate: { opacity: 1, y: 0 },
    exit: { opacity: 0, y: 10 },
    transition: { duration: 0.2 },
}

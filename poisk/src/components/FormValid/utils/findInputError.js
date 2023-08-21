//обработчик ошибок
//функция принимает объект errors и имя входных данных
// в качестве аргументов и возвращает связанные ошибки.
// Затем мы передаем отфильтрованную ошибку InputError компоненту
export function findInputError(errors, name) {
    const filtered = Object.keys(errors)
        .filter((key) => key.includes(name))
        .reduce((cur, key) => {
            return Object.assign(cur, { error: errors[key] })
        }, {})
    return filtered
}

// принимает объект error в качестве входных данных и возвращает true, если форма недопустима
export const isFormInvalid = (err) => {
    if (Object.keys(err).length > 0) return true
    return false
}

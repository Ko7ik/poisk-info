import React from 'react'
import { SiVk } from 'react-icons/si'

class Form extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            radio: false,
            radio2: false,
            url: '',
            keywords: '',
        }
    }

    handleChange = (event) => {
        this.setState({ [event.target.name]: event.target.value })
    }

    handleSubmit = (event) => {
        // alert('A form was submitted: ' + this.state)

        fetch('https://reqres.in/api/users', {
            method: 'POST',
            // We convert the React state to JSON and send it as the POST body
            body: JSON.stringify(this.state),
        }).then(function (response) {
            console.log(response)
            return response.json()
        })

        event.preventDefault()
    }

    render() {
        return (
            <div className="Main">
                <form
                    onSubmit={this.handleSubmit}
                    ref={(el) => (this.myForm = el)}
                >
                    <div className="ico">
                        {' '}
                        <SiVk size={42} />
                    </div>
                    <label htmlFor="SocNet">Социальная сеть / мессенджер</label>
                    <select name="SocialNetwork" id="SocNet">
                        <option value="vk">Вконтакте </option>
                        <option value="tg">...? </option>
                        <option value="ok">...? </option>
                    </select>
                    <div className="radio">
                        <label htmlFor="fid-1">Паблик</label>
                        <label htmlFor="fid-2">Пользователь</label>
                        <input
                            id="fid-1"
                            type="radio"
                            name="radio"
                            value={this.state.value}
                            onChange={this.handleChange}
                        />
                        <input
                            id="fid-2"
                            type="radio"
                            name="radio2"
                            value={this.state.value}
                            onChange={this.handleChange}
                        />
                    </div>
                    <input
                        placeholder="URL"
                        name="url"
                        value={this.state.value}
                        onChange={this.handleChange}
                    />
                    <textarea
                        placeholder="Ключевые слова"
                        name="keywords"
                        value={this.state.value}
                        onChange={this.handleChange}
                    />

                    <button
                        type="submit"
                        onClick={() => {
                            this.myForm.reset()
                            console.log()
                        }}
                    >
                        Запустить процесс
                    </button>
                </form>
            </div>
        )
    }
}

export default Form

//<label htmlFor="file">Прикрепить файл</label>
//<input type="file" id="file" />

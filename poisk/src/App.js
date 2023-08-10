import React from 'react';
import Form from './components/Form';
import Menu from './components/Menu';
import Monitor from './components/Monitor';
import { Routes, Route, Link } from 'react-router-dom';

import {FaSearch} from 'react-icons/fa'
import {MdMonitorHeart} from 'react-icons/md'





class App extends React.Component {
  render() {
    return(<div className='body'>
        <Menu/>
   
        <Routes>
            <Route path="/" element={<Form/>}></Route>
            <Route path="/monitor" element={<Monitor/>}></Route>
        </Routes>


    </div>
      
    )
    
  }
  
 
}



export default App

/* 
        class App extends React.Component {

        constructor(props) {
                super(props) // (строка по умолчанию) передача свойств (props) в конструктор с помощью метода super 
                this.state = {
                    helpText: "Help!",
                    userData: ""
                } 
                this.inputClick = this.inputClick.bind(this)
                // работа с динамичиескими состояниями (state) и присовение состояний
                // helpText: 'Help!' - задаем значение по умолчанию
                // добавляем обращение к state, например <h1> {this.state.helpText} </h1>
                // this.inputClick - обращение к методу = this.inputClick.bind(this) - обращение к сетоду bind 
                // позволяет взаимодейтсвовать состояниям с inputClick
            }
            

        //helpText = 'Help!' //  в классах задается без const
        // при заданном в конструкторе состоянии по умолчению не нужен

        componentDidUpdate(prevProp) {
            if (this.state.helpText !== "Help!")
            console.log ("Some")
            }
        // хук для класса аналог useEffect  параметр prevProp - предыдущее стостояние,метод срабатывает автоматически, когда внутри компонента
        // изменяется состояние
            
            render () {
            return ( 
                <div className='name'>
                
                <Header title = " Шапка сайта" name= ""/>
                <h1> {this.state.helpText} </h1>
                <h2>{this.state.userData} </h2>
                <input placeholder={this.state.helpText}
                onChange={event => this.setState ({userData: event.target.value})}
                onClick={this.inputClick} onMouseEnter={this.mouseOver} />
                <p>{this.state.helpText === "Help!" ? "Yes" : "No" } </p>
                <Image image={logo} />   
                <img src={logo}/> 
                
                </div> ) 
                // вывод div с компонентами 
                // <Image image={logo} - вывод изображений через подключенный компонент
                //<img src={logo}/> + import logo from './img/image1.png' - вывод напрямую
                //onChange={event => this.setState ({userData: event.target.value})}
                //параметр event для получения информации, которую ввел пользователь (event.target.value)
        }
        
        
        inputClick() //метод нажатия на инпут поле
            {
                this.setState({helpText:"Changed"}) // при нажатии на инпут поле извенить значение help.Text
                console.log ("Click!!") // вывод в консоль
            }   
        mouseOver() {console.log ("Mouse!!")}
        
        }
  

    class App extends React.Component {

        constructor (props) {
            super(props)
            this.state = {
                users : [ //массив
                    {
                        id:1,
                        firstname: 'Bob',
                        lastname: 'Marley',
                        bio: 'loren ipsum.....',
                        age: '40',
                        isHappy: true 
                    },
                    {
                        id:2,
                        firstname: 'Jhon',
                        lastname: 'Davis',
                        bio: 'loren ipsum...123..',
                        age: '22',
                        isHappy: false 
                    },
                ]
            }
            this.addUser = this.addUser.bind(this)
            this.deleteUser = this.deleteUser.bind(this)
            this.editUser = this.editUser.bind(this)
        }
        render () {
            return (<div>
              
                <Header title = " Список пользователей" />
                <main>
                    <Users users={this.state.users} onEdit={this.editUser} onDelete={this.deleteUser}/>

                </main>
                <aside>
                    <Form onAdd={this.addUser}/>
                </aside>
                </div>
            )
        }

        deleteUser(id){
            this.setState ({
                users:this.state.users.filter((el)=>el.id !== id)
            })
        }

        editUser (user){
            let allUsers = this.state.users
            allUsers[user.id - 1]=user

            this.setState({users:[]}, () => {
                this.setState({users: [...allUsers]})
            })
        }

        addUser(user) {
            const id = this.state.users.length +1
            this.setState ({users:[...this.state.users, {id, ...user}]})
            //меняем список users и добавляем новый (id+все остальные парамеры юзер)
        }
    
    }

 */

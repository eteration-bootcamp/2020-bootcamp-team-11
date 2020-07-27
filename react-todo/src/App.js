import React,{ Component } from 'react';
import './App.css';

class App extends Component {
    constructor(props) {
      super(props);

      this.state = {
        newItem:"",
        list:[]
      }
    }
    
    updateInput(key,value) {
      //React state'leri güncellenmesi
      this.setState({
        [key]:value
      });
    }
    addItem(){
      // Unique id ile yeni item'ların oluşturulması
      const newItem={
        id: 1 + Math.random(),
        value: this.state.newItem.slice()

      };

      // Mevcut liste öğelerinin kopyası
      const list=[...this.state.list];

      // Listeye yeni item eklenmesi

      list.push(newItem);

      //Stateleri yeni liste ile güncellenmesi ve newItem imput resetlenmesi

      this.setState({
        list,
        newItem:""
      });
    }

    deleteItem(id){
      //Listedeki öğelerin mevcut kopyası
      const list=[...this.state.list];

      //Silinecek öğeye filtrelerin uygulanması
      const updatedList=list.filter(item=>item.id !==id);

      this.setState({list: updatedList});
    }
  render(){
    
    return (
      <div>

      <h3 className="app-title">My To Do List</h3>
        
        <div className="container">
        <div
          style={{
            padding: 30,
            textAlign: "left",
            maxWidth: 500,
            margin: "auto",
          }}
        >
          Add an Item...
          <br /> <br />
          <input
            type="text"
            placeholder="Type item here"
            value={this.state.newItem}
            onChange={e => this.updateInput("newItem", e.target.value)}
          />
          &nbsp; &nbsp;
          <button
            className="add-btn btn-floating"
            onClick={() => this.addItem()}
            disabled={!this.state.newItem.length}
          >
            <i class="material-icons"> Add </i>
          </button>
          <br /> <br />
          <ul>
            {this.state.list.map(item => {
              return (
                <li key={item.id}>
                  {item.value}
                  <button className="btn btn-floating" onClick={() => this.deleteItem(item.id)}>
                    <i class="material-icons">Delete</i>
                  </button>
                </li>
              );
            })}
          </ul>
        </div>
      </div>
      </div>
    );
  }
}
export default App;

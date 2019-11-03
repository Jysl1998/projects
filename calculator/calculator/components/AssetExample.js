import * as React from 'react';
import { Text, View, StyleSheet, Image } from 'react-native';
import {Button} from 'react-native-elements';

export default class AssetExample extends React.Component {

  /*
  Create a constructor creating this.state variables 
  - var1, var2, total, currentVar, and clearEq
   */
  constructor(props){
    super(props)
    this.state = {
      operator: '',
      var2: Number(''),
      var1: Number(''),
      total: '',
      currentVar: '',
      clearEq: ''
    }
  }

  /*firstVar method, taking in a variable
  param: variable
   setting var1 to variable
  when adding more than one variable, you want to continually stack on to 
  */
  firstVar = (variable) => {
    this.setState({var1: this.state.currentVar + variable})
    console.log("Var1: ")
  }

 /*secVar method, taking in a variable
  param: variable
   setting var2 to variable
  when adding more than one variable, you want to continually stack on to 
  */
  secVar = (variable) => {
    this.setState({var2:this.state.currentVar + variable})
    console.log("var2: ")
  }

  /*
  storeVar method
  param: variable
  if the operator is empty, then send the currentVar to firstVar
  else then send it to secondVar
  */
  storeVar = (variable) => {
    this.setState({currentVar:this.state.currentVar + variable})
    if(this.state.operator === ''){
      this.firstVar(variable)
    }else{
      this.secVar(variable)
    }
  }

  /*
  replaceOperator method
  param: currentOp
  takes in the operator the user pushed on, and then adds it onto the equation
  */
  replaceOperator = (currentOp) => {
    this.setState({currentVar:""})
    this.setState({operator: currentOp})
    this.setState({equation:this.state.equation + currentOp})
    console.log("operator: ")
  }

/*
clear method
if C button is pressed, all variables reset to an empty string
*/
  clear = () => {
    this.setState({currentVar:this.state.clearEq})
     this.setState({var1:this.state.clearEq})
      this.setState({var2:this.state.clearEq})
       this.setState({operator:this.state.clearEq})
  }

/*
calculate method
param: none
when the = button is pressed, it will immediately go into this method
calculates all of the given variables
*/
  calculate = () =>{
    //create a temp variable
    let result
    // result = eval(this.state.var1 + this.state.operator + this.state.var2)
    if(this.state.operator === "+"){
      result = Number(this.state.var1) + Number(this.state.var2)

    } 
    //if operator is -
    else if(this.state.operator === "-"){
      result = Number(this.state.var1) - Number(this.state.var2)
  
    } 
    //if operator is /
    else if(this.state.operator === "/"){
      result = Number(this.state.var1) / Number(this.state.var2)
    } 
    //if operator is x
    else if(this.state.operator === "x"){
      result = Number(this.state.var1) * Number(this.state.var2)
    } 
    // first setting result to currentVar to print out the result
    // setting currentVar to var1 (creating continuous calculation)
    this.setState({currentVar: result})
    this.setState({var1: result})
  }

  render() {
    return (
      //setting the background
      //prints out the currentVar
      <View style={styles.container}>
         <View style= {{backgroundColor: '#BDBF87', height: 60, marginBottom: 5, width: 325}}> 
          <Text style={{fontSize: 30, textAlign: 'center', marginTop: 10 }}>
            {this.state.currentVar}
          </Text>
        </View>
        <View style ={{display: 'flex', flexDirection: 'row'}}>
          <Button style = {styles.buttonDesign} title = '1'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
           onPress={()=> this.storeVar("1")}/>
          <Button style = {styles.buttonDesign} title = '2'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("2")}/>
          <Button style = {styles.buttonDesign} title = '3'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("3")}/>
          <Button style = {styles.buttonDesign} title = 'X'
          buttonStyle = {{backgroundColor: '#BB8340'}}
          onPress={()=> this.replaceOperator("x")}/>
        </View>

         <View style ={{display: 'flex', flexDirection: 'row'}}>
          <Button style = {styles.buttonDesign} title = '4'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("4")}/>
          <Button style = {styles.buttonDesign} title = '5'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("5")}/>
          <Button style = {styles.buttonDesign} title = '6'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("6")}/>
          <Button style = {styles.buttonDesign} title = '/'
          buttonStyle = {{backgroundColor: '#BB8340'}}
          onPress={()=> this.replaceOperator("/")}/>
        </View>

        <View style ={{display: 'flex', flexDirection: 'row'}}>
          <Button style = {styles.buttonDesign} title = '7'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("7")}/>
          <Button style = {styles.buttonDesign} title = '8'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("8")}/>
          <Button style = {styles.buttonDesign} title = '9'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("9")}/>
          <Button style = {styles.buttonDesign} title = '+'
          buttonStyle = {{backgroundColor: '#BB8340'}}
          onPress={()=> this.replaceOperator("+")}/>
        </View>

        <View style ={{display: 'flex', flexDirection: 'row'}}>
          <Button style = {{width: 160, margin: 5}} title = '0'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar("0")}/>
          <Button style = {styles.buttonDesign} title = '.'
          buttonStyle= {{backgroundColor: '#EA9B67'}}
          onPress={()=> this.storeVar(".")}/>
          <Button style = {styles.buttonDesign} title = '-'
          buttonStyle = {{backgroundColor: '#BB8340'}}
          onPress={()=> this.replaceOperator("-")}/>
        </View>

        <View style = {{display: 'flex', flexDirection: 'row'}}>
        <Button style = {{width: 100, marginLeft: 145, marginTop: 5, marginRight: 5}} title = 'C'
        buttonStyle = {{backgroundColor: '#BB8340'}}
        onPress={()=> this.clear()}/>
        <Button style = {{width: 75, marginLeft:5, marginTop: 5}} title = '='
        buttonStyle = {{backgroundColor: '#BB8340'}}
          onPress={()=> this.calculate()}/>
        </View>

      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    width: 360,
    height: 500,
    backgroundColor: "#EAECBD"
  },
  //styling the button size
  buttonDesign: {
    margin: 5,
    width: 75
  },
});

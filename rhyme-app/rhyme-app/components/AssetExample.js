import * as React from 'react';
import { Text, View, StyleSheet, Image, Button, Layout } from 'react-native';

export default class AssetExample extends React.Component {
  constructor(props){
  super(props);
  state: {
      rhyme: '';
  }
  }

  statfindRhyme = () => {

  }

  findRhyme=()=>{
    fetch('https://api.datamuse.com/words?rel_rhy='+this.state.rhyme)
    .then((response) => response.json())
    .then((responseJson) => {
      this.setState({rhyme: responseJson[0].word })
    })
    .catch((error) => {
      console.error(error);
    });
  }

  render() {
    return (
        <View style = {styles.container}>
        </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    padding: '16',
    backgroundColor: 'white'
  }
});

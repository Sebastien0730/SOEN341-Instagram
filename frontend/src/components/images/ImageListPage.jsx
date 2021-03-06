import React, { Component } from 'react';
import ImageBox from './imageBox';

export default class ImageListPage extends Component {
  constructor(props) {
    super(props);
    // Don't call this.setState() here!
    this.state = { images: this.props.images};
  }

  render() {
    return (
      <div style={{display: 'flex', flexWrap: 'wrap'}}>
        {this.props.images.map( (image, index) => {
          return (
            <div style={{margin:'30px', position:'relative', minWidth:'500px'}} key={index}>
              <ImageBox image={image} currentUser={this.props.currentUser} usedApi={this.props.usedApi} token={this.props.token}/>
            </div>
          )
        })}
      </div>
    );
  }
}
class Playlist extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }


    getData1(){
        let headers = { 'Content-Type': 'application/json', };
        return fetch('http://127.0.0.1:8000/api/playlist/2/?format=json',  { headers,  })
            .then(res => res.json())
            .then(data => {
                console.log(data);
                // do something with data
            });
    }

    getData(){
        this.getData1();
        return (<div>Hello World</div>);
    }

    render(){
        return(
            <div>Siem{this.getData()}</div>
        )
    }
}

export default Playlist;

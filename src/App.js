import logo from './logo.svg';
/*import './App.css';*/


const Images = (props) => {
  return (
    <div>
      {props.images.map((image, index) => {
        return <div key="newsimg{index}">
          <img src={image.uri} alt={image.description} />
        </div>
    })}
    </div>
  );
};

const Author = (props) => {
  return <div>{props.author.name}</div>
}

const Authors = (props) => {
  return <div>
    {
      props.authors.map((author, index)=>{
        return <div key="author{index}">
          By {author.name}
        </div>
      })
    }
  </div>
}

const Body = (props) => {
  return <div>{props.body}</div>
}


function App() {
  const news_data = {
    "authors":[
      {"name":"An author"}
    ],
    "images":[
      {"description":"An example image", "uri":"http://example.com/image.png"}
    ],
    "body": "This is the article body."
  }
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <Images images={news_data.images} />
      <Authors authors={news_data.authors}/>
      <Body body={news_data.body} />
    </div>
  );
}

export default App;

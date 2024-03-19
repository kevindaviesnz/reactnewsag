import logo from './logo.svg';
import './App.css';

const ArticleImages = (props) => {
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

const ArticleAuthor = (props) => {
  return <div>Author:{props.author.name}</div>
}

const ArticleAuthors = (props) => {
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

const ArticleBody = (props) => {
  return <div>{props.body}</div>
}

function App() {
  const images = [
    { "uri": "http://example.com", "description": "An example image" },
    {"uri":"http://example.com", "description":"Another example image"}
  ]
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <ArticleImages images={images} />
        <ArticleAuthor author={{"name":"Me"}} />
        <ArticleBody body="This is the body of the article" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React!!! Oh Yeah!!!!
        </a>
      </header>
    </div>
  );
}

export default App;

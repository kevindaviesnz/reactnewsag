import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Fragment } from 'react'

// Providers
import IssueProvider from './contexts/Issue'
import Issues from './Issues'
import ArticleProvider from './contexts/ArticleContext'
import Articles from './Articles'


const withClassName = Component => props => (
  <Component {...props} className="my-class" />
)
const MyComponent = ({className}) => <div className={className} />
const MyComponentWithClassName = withClassName(MyComponent)

const Button = ({children}) => <button className="btn">{children}</button>

const ArticleImages = (props) => {
  return (
    <div>
      {props.images.map((image, index) => {
        return <div key="newsimg{index}">
          <img {...image} />
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

const ArticleBody = (props: any) => {
  return <div>{props.body}</div>
}

function App() {
  const [count, setCount] = useState(0)
  const images = [
    { "src": "http://example.com", "alt": "An example image" },
    {"src":"http://example.com", "alt":"Another example image"}
  ]
  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
        <ArticleImages images={images} />
        <ArticleAuthor author={{"name":"Me"}} />
        <ArticleBody body="This is the body of the article" />
        <Button>
          <img src="http://example.com/img.png" alt="An example image"/>
          <span>Click me!</span>
        </Button>
        <div>------------ hey!!! yo</div>
        <ArticleProvider url="https://3yxdd3ce42.execute-api.ap-southeast-2.amazonaws.com/get-news-api-function"> 
            <Articles />
        </ArticleProvider>

      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more!
      </p>
    </>
  )
}

export default App

import { FC, createContext, useState, useEffect, ReactElement, useCallback } from 'react'
import axios from 'axios'

/* Declare interfaces */
export type IArticle = {
    number: number
    title: string
    url: string
    state: string
}
interface Article_Context {
    articles: IArticle[]
    url: string
}
interface Props {
    url: string
}

/* The first thing we need to do after declaring the interfaces is to create our context by using the createContext func-
tion and defining the value we want to export: */
export const ArticleContext = createContext<Article_Context>({ articles: [], url: '' })

/* Once we have ArticleContext, we need to create a component where we can receive props, set some
states, and perform the fetch by using useEffect, and then we render ArticleContext.Provider
where we specify the context (value) we will export: */
const ArticleProvider: FC<Props> = ({ children, url }) => { // "FC" indicates that Articles is a FunctionComponent type., for url see App.tsx and Articles.tsx
    
    // State
    const [articles, setArticles] = useState<IArticle[]>([])
    
    // Define a function to fetch articles from the provided URL
    const fetchArticles = useCallback(async () => {
        const response = await axios(url)  // Fetch data from the provided URL using axios
        if (response) {
            setArticles(response.data)  // Set the fetched articles to the component state
        }
    }, [url])  // This function depends on the 'url' prop

    // Effects
    useEffect(() => {   
        fetchArticles()  // Call the fetchArticles function when the component mounts or when 'fetchArticles' changes
    }, [fetchArticles])  // This effect depends on the 'fetchArticles' function

    // Create a context object containing 'articles' and 'url' states
    const context = {
        articles,
        url
    }

    // Render the ArticleContext.Provider with the provided context and children
    return <ArticleContext.Provider value={context}>{children}</ArticleContext.Provider>
}
export default ArticleProvider

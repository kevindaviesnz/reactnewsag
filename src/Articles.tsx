// This file: Articles.tsx
// Dependencies
import { FC, useContext } from 'react'
// Contexts
import { ArticleContext, IArticle } from './contexts/ArticleContext'
import NewsArticle from './NewsArticle'


const Articles: FC = () => { // "FC" indicates that Articles is a FunctionComponent type.
    // Here you consume your Context, and you can grab the articles value.
    const { articles, url } = useContext(ArticleContext) /* for url see App.tsx */

    // Render a list of articles obtained from the context
    return (
        <>
            <h1>ContentPI Articles from Context</h1>
            {articles.map((article: IArticle) => (
                <div key={`article-${article.uuid}`}>
                    <NewsArticle />
                    <img src={`${article.images[0]}`} alt="article image"/>
                    <a href={`${article.uri}`}>{article.headline}</a> {' '}
                    {article.categories[0]}
                </div>
            ))}
        </>
    )
}

export default Articles

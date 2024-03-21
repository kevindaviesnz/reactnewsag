import { FC, createContext, useState, useEffect, ReactElement, useCallback } from 'react'
import axios from 'axios'

/* Declare interfaces */
export type Issue = {
    number: number
    title: string
    url: string
    state: string
}
interface Issue_Context {
    issues: Issue[]
    url: string
}
interface Props {
    url: string
}

/* The first thing we need to do after declaring the interfaces is to create our context by using the createContext func-
tion and defining the value we want to export: */
export const IssueContext = createContext<Issue_Context>({ issues: [], url: '' })

/* Once we have IssueContext, we need to create a component where we can receive props, set some
states, and perform the fetch by using useEffect, and then we render IssueContext.Provider
where we specify the context (value) we will export: */
const IssueProvider: FC<Props> = ({ children, url }) => { // FC = FunctionComponent
    
    // State
    const [issues, setIssues] = useState<Issue[]>([])
    
    // Define a function to fetch issues from the provided URL
    const fetchIssues = useCallback(async () => {
        const response = await axios(url)  // Fetch data from the provided URL using axios
        if (response) {
            setIssues(response.data)  // Set the fetched issues to the component state
        }
    }, [url])  // This function depends on the 'url' prop

    // Effects
    useEffect(() => {   
        fetchIssues()  // Call the fetchIssues function when the component mounts or when 'fetchIssues' changes
    }, [fetchIssues])  // This effect depends on the 'fetchIssues' function

    // Create a context object containing 'issues' and 'url' states
    const context = {
        issues,
        url
    }

    // Render the IssueContext.Provider with the provided context and children
    return <IssueContext.Provider value={context}>{children}</IssueContext.Provider>
}
export default IssueProvider

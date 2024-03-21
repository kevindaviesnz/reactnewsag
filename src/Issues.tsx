// Dependencies
import { FC, useContext } from 'react'
// Contexts
import { IssueContext, Issue } from './contexts/Issue'

const Issues: FC = () => {
    // Here you consume your Context, and you can grab the issues value.
    const { issues, url } = useContext(IssueContext)

    // Render a list of issues obtained from the context
    return (
        <>
            <h1>ContentPI Issues from Context</h1>
            {issues.map((issue: Issue) => (
                <p key={`issue-${issue.number}`}>
                    <strong>#{issue.number}</strong> {' '}
                    <a href={`${url}/${issue.number}`}>{issue.title}</a> {' '}
                    {issue.state}
                </p>
            ))}
        </>
    )
}

export default Issues

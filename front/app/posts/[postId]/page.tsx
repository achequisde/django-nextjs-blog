'use client';

import useSWR from 'swr';
import dateFormat from "dateformat";

const fetcher = (...args) => fetch(...args).then((res) => res.json())

export default function PostDetail({ params }) {
    const { data, error } = useSWR(`http://localhost:8000/api/posts/${params.postId}`, fetcher);

    if (!data) return <p></p>

    return (
        <main className='container'>
            <header>
                <h1>{data.title}</h1>
                <time className='small'>{dateFormat(data.created, "mediumDate")}</time>
                <p className='small'>{data.author.name}</p>
            </header>

            <p className='p-4'>
                {data.content}
            </p>
        </main>
    )
}

import Link from "next/link";
import dateFormat from "dateformat";

function Post({ id, title, extract, content, author, created }) {
  return (
    <article className="border m-3 p-4">
      <h2><Link href={`/posts/${id}`}>{title}</Link></h2>
      <time className="small" dateTime={created}>{dateFormat(created, "mediumDate")}</time>
      <p className="mt-3">{`${extract}...`}</p>
      <footer>
        <p className="small">{author.name}</p>
      </footer>
    </article>
  )
}

export default async function Home() {
  const posts = await getPosts();

  return (
    <main className="container p-3">
      {posts.map((post, index) =>
        <section>
          <Post key={post.index} {...post} />
        </section>
      )}
    </main>
  )
}

async function getPosts() {
  const res = await fetch("http://localhost:8000/api/posts", { cache: 'no-store', next: { revalidate: 0 } });

  if (!res.ok) {
    throw new Error(`Couldn't fetch posts.`);
  }

  return res.json();
}
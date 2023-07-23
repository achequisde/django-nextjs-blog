import Link from 'next/link';

import 'bootstrap/dist/css/bootstrap.css';
import './globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <header>
          <nav>
            <Link className='btn btn-primary m-3' href={'/'}>Home</Link>
          </nav>
        </header>
        {children}
      </body>
    </html>
  )
}

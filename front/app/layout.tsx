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
          <nav className='p-3'>
            <a className='link-primary m-3 text-decoration-none fs-4' href={'/'}>Home</a>
          </nav>
        </header>
        {children}
      </body>
    </html>
  )
}

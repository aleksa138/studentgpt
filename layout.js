// 2. app/layout.js
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: 'Arial', margin: 0, background: '#0f172a', color: 'white' }}>
        {children}
      </body>
    </html>
  );
}
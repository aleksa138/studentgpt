// 3. app/page.js (главная)
'use client';
import { useState } from 'react';

export default function Home() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const addNote = () => {
    if (!title || !content) return;
    setNotes([...notes, { title, content }]);
    setTitle('');
    setContent('');
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>📚 StudyHub</h1>

      <div style={{ marginBottom: 20 }}>
        <input
          placeholder="Название конспекта"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ display: 'block', marginBottom: 10, padding: 10, width: '100%' }}
        />

        <textarea
          placeholder="Содержимое"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          style={{ display: 'block', marginBottom: 10, padding: 10, width: '100%', height: 100 }}
        />

        <button onClick={addNote} style={{ padding: 10, cursor: 'pointer' }}>
          Добавить
        </button>
      </div>

      <h2>Конспекты</h2>

      {notes.map((note, index) => (
        <div key={index} style={{ background: '#1e293b', padding: 15, marginBottom: 10, borderRadius: 10 }}>
          <h3>{note.title}</h3>
          <p>{note.content}</p>
        </div>
      ))}
    </div>
  );
}






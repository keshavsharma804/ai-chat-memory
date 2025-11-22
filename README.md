# VectorLabs AI – Chat with Memory + Web Search

An AI chat application with *long-term memory, **real-time web search, and a **ChatGPT-style UI* – built as a full-stack project for learning and portfolio use.

- 🧠 *Vector memory* using Pinecone (stores past conversations per user)
- 🌍 *Real-time web search* using Tavily (latest news, facts, info)
- 🤝 *LLM reasoning* using OpenRouter (Mistral-Nemo + embeddings)
- 🖥 *Modern React frontend* with multi-chat sessions and clean UX
- ☁ *Serverless backend* on Cloudflare Workers

---

## 🔧 Tech Stack

*Backend*

- Cloudflare Workers
- Pinecone (Serverless index)
- Tavily Search API
- OpenRouter API
  - intfloat/e5-base-v2 (embeddings)
  - mistral-nemo (chat completions)
- JSON REST API (/chat, /health)

*Frontend*

- React + Vite
- Modern chat UI (sidebar, chat bubbles, loading state)
- Environment-based backend URL

---

## 🧱 Architecture

*High level flow:*

1. User sends a message from the React frontend → /chat
2. Backend:
   - Creates an *embedding* for the message via OpenRouter
   - *Queries Pinecone* for similar past messages (user-scoped memory)
   - *Calls Tavily* to fetch fresh web results (news / facts)
   - Combines:
     - Memory (if relevant)
     - Web search results
     - LLM’s own knowledge  
   - Generates a final reply using mistral-nemo on OpenRouter
   - Stores the new message back into Pinecone as a memory
3. Frontend displays reply, shows loading state, and maintains multi-chat sessions.


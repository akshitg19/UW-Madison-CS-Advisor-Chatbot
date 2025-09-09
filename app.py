/**
 * React Frontend for the UW-Madison CS Advisor Chatbot.
 *
 * This script creates the modern, user-facing web interface for the RAG-powered chatbot,
 * built with React, TypeScript, and WebGL for a dynamic experience. It handles 
 * conversational sessions to provide a natural and context-aware user interaction.
 *
 * Author: Akshit Ganesh
 * Date: 09/08/25
 */

import React, { useState, useEffect, useRef } from 'react';

// --- Type Definitions for TypeScript ---
interface Message {
  role: 'user' | 'assistant';
  content: string;
  isError?: boolean;
}

interface ChatMessageProps {
  message: Message;
}

// --- Component: WebGLBackground ---
// Renders a visually engaging, branded background to enhance user immersion
// and reinforce the UW-Madison identity.
const WebGLBackground = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const gl = canvas.getContext('webgl');
    if (!gl) {
      console.error("WebGL is not supported.");
      return;
    }

    // GLSL Shader Code
    const vertexShaderSource = `
      attribute vec2 a_position;
      void main() {
        gl_Position = vec4(a_position, 0.0, 1.0);
      }
    `;

    // Shader Logic: Defines the "digital aurora" effect using GLSL.
    // The colors are intentionally aligned with UW-Madison's branding.
    const fragmentShaderSource = `
      precision highp float;
      uniform vec2 u_resolution;
      uniform float u_time;

      // A more organic noise function using sine waves
      float fbm(vec2 st) {
        float value = 0.0;
        float amplitude = 0.5;
        for (int i = 0; i < 5; i++) {
            value += amplitude * abs(sin(st.x * (0.5 * float(i)) + u_time * 0.2));
            st.x *= 2.0;
            amplitude *= 0.5;
        }
        return value;
      }

      void main() {
        vec2 st = gl_FragCoord.xy / u_resolution.xy;
        st.x *= u_resolution.x / u_resolution.y; // Aspect ratio correction

        // Define a color palette
        vec3 color1 = vec3(0.01, 0.0, 0.1);  // Deep Space Blue
        vec3 color2 = vec3(0.8, 0.1, 0.3);  // UW-Madison Cardinal Red inspiration
        vec3 color3 = vec3(0.1, 0.3, 0.6);  // Bright Blue

        // Create a time-dependent vertical gradient
        float t = 0.5 + 0.5 * sin(u_time * 0.1 + st.y * 3.0);
        vec3 base_color = mix(color1, color3, t);

        // Add multiple layers of flowing, distorted waves
        float slow_waves = sin(st.y * 4.0 - u_time * 0.3) * 0.5 + 0.5;
        float fast_waves = fbm(st * vec2(1.0, 3.0));
        
        // Combine the waves
        float final_wave = smoothstep(0.4, 0.7, slow_waves + fast_waves * 0.4);

        // Mix the wave color with the base gradient
        vec3 final_color = mix(base_color, color2, final_wave * 0.8);
        
        // Add subtle grain for texture
        final_color += (fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123) - 0.5) * 0.05;

        // Add vignette to focus the center
        float vignette = 1.0 - length(gl_FragCoord.xy / u_resolution.xy - 0.5) * 1.2;
        final_color *= vignette;

        gl_FragColor = vec4(final_color, 1.0);
      }
    `;

    // Compile and link shaders
    const createShader = (type: number, source: string) => {
      const shader = gl.createShader(type);
      if (!shader) return null;
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error('Shader compile error:', gl.getShaderInfoLog(shader));
        gl.deleteShader(shader);
        return null;
      }
      return shader;
    };

    const vertexShader = createShader(gl.VERTEX_SHADER, vertexShaderSource);
    const fragmentShader = createShader(gl.FRAGMENT_SHADER, fragmentShaderSource);
    if (!vertexShader || !fragmentShader) return;

    const program = gl.createProgram();
    if (!program) return;
    gl.attachShader(program, vertexShader);
    gl.attachShader(program, fragmentShader);
    gl.linkProgram(program);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
      console.error('Program link error:', gl.getProgramInfoLog(program));
      return;
    }
    gl.useProgram(program);

    // Buffer for a full-screen quad
    const positionBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
    const positionAttributeLocation = gl.getAttribLocation(program, "a_position");
    gl.enableVertexAttribArray(positionAttributeLocation);
    gl.vertexAttribPointer(positionAttributeLocation, 2, gl.FLOAT, false, 0, 0);

    // Uniform locations
    const resolutionUniformLocation = gl.getUniformLocation(program, "u_resolution");
    const timeUniformLocation = gl.getUniformLocation(program, "u_time");

    let animationFrameId: number;
    const render = (time: number) => {
      time *= 0.001; // convert to seconds
      
      // Resize canvas to match display size
      const { clientWidth, clientHeight } = gl.canvas;
      if (gl.canvas.width !== clientWidth || gl.canvas.height !== clientHeight) {
        gl.canvas.width = clientWidth;
        gl.canvas.height = clientHeight;
        gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight);
      }
      
      gl.uniform2f(resolutionUniformLocation, gl.canvas.width, gl.canvas.height);
      gl.uniform1f(timeUniformLocation, time);

      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
      animationFrameId = requestAnimationFrame(render);
    };
    
    animationFrameId = requestAnimationFrame(render);
    
    return () => {
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return <canvas ref={canvasRef} className="absolute top-0 left-0 w-full h-full -z-10" />;
};


// --- Helper Components ---
const Spinner = () => (
  <div className="w-6 h-6 border-4 border-gray-300 border-t-blue-500 rounded-full animate-spin"></div>
);

// Component: ChatMessage - Displays a single user or bot message, ensuring a clear, readable chat history.
const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const { role, content, isError } = message;
  const isUser = role === 'user';

  return (
    <div className={`flex items-start gap-3 my-4 ${isUser ? 'justify-end' : 'justify-start'}`}>
      {!isUser && (
        <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center text-white font-bold flex-shrink-0">
          B
        </div>
      )}
      <div 
        className={`p-4 max-w-lg rounded-2xl shadow-md animate-fade-in-up
          ${isUser ? 'bg-blue-600 text-white rounded-br-none' : 'bg-white text-gray-800 rounded-bl-none'}
          ${isError ? 'bg-red-100 text-red-800 border border-red-300' : ''}`}
      >
        <div className="prose prose-sm" dangerouslySetInnerHTML={{ __html: content.replace(/\n/g, '<br />') }} />
      </div>
       {isUser && (
        <div className="w-10 h-10 bg-gray-300 rounded-full flex items-center justify-center text-gray-600 font-bold flex-shrink-0">
          U
        </div>
      )}
    </div>
  );
};


// --- Component: App ---
// The primary application container that orchestrates the chat interface,
// state management, and API communication.
const App: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', content: "Hello! How can I help you with the Computer Sciences major today?" }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState<string | null>(null);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Function: handleSubmit - Manages the full user interaction cycle:
  // sending the query, handling the loading state, and rendering the AI response.
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      // Configuration: The API endpoint for the backend. This must be updated post-deployment.
      const API_URL = "https://your-api-gateway-url.execute-api-us-east-1.amazonaws.com/prod/chat"; 

      const payload = {
        question: input,
        session_id: sessionId,
      };

      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`API Error: ${response.status} ${response.statusText}`);
      }

      const result = await response.json();

      const assistantMessage: Message = { role: 'assistant', content: result.answer };
      setMessages(prev => [...prev, assistantMessage]);
      setSessionId(result.session_id);

    } catch (err: any) {
      console.error("Failed to fetch from API:", err);
      const errorMessage: Message = { 
        role: 'assistant', 
        content: `**Error:** Could not connect to the advisor API. Please try again later.\n\n*Details: ${err.message}*`,
        isError: true 
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="font-sans h-screen flex flex-col relative isolate overflow-hidden">
      <WebGLBackground />
      {/* Header */}
      <header className="bg-white/70 backdrop-blur-sm shadow-md p-4 flex items-center justify-between border-b border-white/20">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 bg-red-800 rounded-full flex items-center justify-center text-white text-2xl font-bold">
            W
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-800">UW-Madison CS Advisor</h1>
            <p className="text-sm text-gray-600">AI-Powered Guidance</p>
          </div>
        </div>
      </header>
      
      {/* Chat Messages Area */}
      <main className="flex-1 overflow-y-auto p-6">
        <div className="max-w-3xl mx-auto">
          {messages.map((msg, index) => <ChatMessage key={index} message={msg} />)}
          {isLoading && (
            <div className="flex items-start gap-3 my-4 justify-start">
               <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center text-white font-bold flex-shrink-0">
                  B
               </div>
              <div className="p-4 max-w-lg rounded-2xl shadow-md bg-white text-gray-800 rounded-bl-none flex items-center">
                <Spinner />
                <span className="ml-3 text-gray-500">BadgerBot is thinking...</span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </main>

      {/* Input Form */}
      <footer className="bg-white/70 backdrop-blur-sm border-t border-white/20 p-4">
        <div className="max-w-3xl mx-auto">
          <form onSubmit={handleSubmit} className="flex items-center gap-3">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask a question about the CS major..."
              className="flex-1 p-3 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
              disabled={isLoading}
            />
            <button
              type="submit"
              className="bg-blue-600 text-white rounded-full p-3 hover:bg-blue-700 disabled:bg-gray-400 transition-colors"
              disabled={isLoading || !input.trim()}
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 10l7-7m0 0l7 7m-7-7v18" />
              </svg>
            </button>
          </form>
        </div>
      </footer>
    </div>
  );
};

export default App;



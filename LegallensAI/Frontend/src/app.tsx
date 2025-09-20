import UploadBox from "./components/UploadBox";

function App() {
  return (
    <main className="min-h-screen bg-white flex flex-col items-center justify-center px-6 py-12 text-center">
      <h1 className="text-5xl font-extrabold text-gray-900 mb-6">
        ⚖️ LegalLens AI
      </h1>
      <p className="text-lg text-gray-600 mb-8 max-w-xl">
        Your intelligent assistant for analyzing legal documents and generating
        smart arguments.
      </p>

      <UploadBox />
    </main>
  );
}

export default App;

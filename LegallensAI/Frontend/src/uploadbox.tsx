import { useState } from "react";

export default function UploadBox() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setMessage("");
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setUploading(true);
      const res = await fetch("http://127.0.0.1:8000/upload-pdf/", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Upload failed");

      const data = await res.json();
      setMessage(`✅ Uploaded: ${data.filename}`);
    } catch (err) {
      setMessage("❌ Failed to upload file. Check backend.");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="border-2 border-dashed border-gray-300 rounded-2xl p-6 w-full max-w-lg text-center">
      <input
        type="file"
        accept="application/pdf"
        onChange={handleFileChange}
        className="mb-4"
      />
      <button
        onClick={handleUpload}
        disabled={uploading}
        className="px-6 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition disabled:bg-gray-400"
      >
        {uploading ? "Uploading..." : "Upload PDF"}
      </button>
      {message && <p className="mt-4 text-gray-700">{message}</p>}
    </div>
  );
}

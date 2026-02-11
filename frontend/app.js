const createForm = document.getElementById("createForm");
const statusEl = document.getElementById("status");
const postsEl = document.getElementById("posts");
const refreshBtn = document.getElementById("refresh");

function setStatus(message, isError = false) {
  statusEl.textContent = message;
  statusEl.style.color = isError ? "#c23a2f" : "#5b5b5f";
}

function formatDate(value) {
  if (!value) return "";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleString();
}

async function request(path, options = {}) {
  const url = path;
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json", ...options.headers },
    ...options,
  });
  if (!response.ok) {
    const detail = await response.text();
    throw new Error(detail || response.statusText);
  }
  if (response.status === 204) return null;
  return response.json();
}

async function loadPosts() {
  postsEl.innerHTML = "";
  setStatus("Loading posts...");
  try {
    const posts = await request("/blogs/");
    if (!posts.length) {
      postsEl.innerHTML = "<p class=\"post-meta\">No posts yet. Create the first one.</p>";
    } else {
      posts.forEach((post) => postsEl.appendChild(renderPost(post)));
    }
    setStatus("Feed updated.");
  } catch (error) {
    setStatus(`Failed to load posts: ${error.message}`, true);
  }
}

function renderPost(post) {
  const card = document.createElement("article");
  card.className = "post-card";

  const header = document.createElement("div");
  header.innerHTML = `
    <h3>${post.title}</h3>
    <div class="post-meta">
      <span class="badge">${post.published ? "Published" : "Draft"}</span>
      <span>Created: ${formatDate(post.created_at)}</span>
      <span>${post.updated_at ? `Updated: ${formatDate(post.updated_at)}` : ""}</span>
    </div>
  `;

  const body = document.createElement("p");
  body.textContent = post.content;

  const actions = document.createElement("div");
  actions.className = "post-actions";

  const editBtn = document.createElement("button");
  editBtn.className = "btn ghost";
  editBtn.textContent = "Edit";

  const deleteBtn = document.createElement("button");
  deleteBtn.className = "btn ghost";
  deleteBtn.textContent = "Delete";

  const editForm = document.createElement("form");
  editForm.className = "edit-form";
  editForm.innerHTML = `
    <label>
      Title
      <input name="title" type="text" value="${post.title}" />
    </label>
    <label>
      Content
      <textarea name="content" rows="4">${post.content}</textarea>
    </label>
    <label class="toggle">
      <input name="published" type="checkbox" ${post.published ? "checked" : ""} />
      <span>Published</span>
    </label>
    <button class="btn primary" type="submit">Save</button>
  `;
  editForm.style.display = "none";

  editBtn.addEventListener("click", () => {
    editForm.style.display = editForm.style.display === "none" ? "grid" : "none";
  });

  deleteBtn.addEventListener("click", async () => {
    if (!confirm(`Delete "${post.title}"?`)) return;
    try {
      await request(`/blogs/${post.id}`, { method: "DELETE" });
      setStatus("Post deleted.");
      await loadPosts();
    } catch (error) {
      setStatus(`Delete failed: ${error.message}`, true);
    }
  });

  editForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(editForm);
    const payload = {
      title: formData.get("title"),
      content: formData.get("content"),
      published: formData.get("published") === "on",
    };
    try {
      await request(`/blogs/${post.id}`, {
        method: "PUT",
        body: JSON.stringify(payload),
      });
      setStatus("Post updated.");
      await loadPosts();
    } catch (error) {
      setStatus(`Update failed: ${error.message}`, true);
    }
  });

  actions.appendChild(editBtn);
  actions.appendChild(deleteBtn);

  card.appendChild(header);
  card.appendChild(body);
  card.appendChild(actions);
  card.appendChild(editForm);

  return card;
}

refreshBtn.addEventListener("click", loadPosts);

createForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(createForm);
  const payload = {
    title: formData.get("title"),
    content: formData.get("content"),
    published: formData.get("published") === "on",
  };
  setStatus("Creating post...");
  try {
    await request("/blogs/", {
      method: "POST",
      body: JSON.stringify(payload),
    });
    createForm.reset();
    setStatus("Post created.");
    await loadPosts();
  } catch (error) {
    setStatus(`Create failed: ${error.message}`, true);
  }
});

setStatus("Loading posts...");
loadPosts();

function _trigger() {
  activate_typing_effect();
  activate_clone_image_effect();
}

function activate_clone_image_effect(){
  const elements = document.querySelectorAll(".jutsu_images img");
  for (const e of elements) {
    e.addEventListener("click", clone_image);
  }
}

async function activate_typing_effect() {
  const elements = document.querySelectorAll(".typed-text");
  for (const el of elements) {
    const txt = el.innerText;
    el.innerText = "";
    await typing(el, txt);
  }
}

function typing(el, txt) {
  return new Promise((resolve) => {
    el.style.display = "block";
    let i = 0;
    const speed = 70;

    function typer() {
      if (i < txt.length) {
        el.innerHTML += txt.charAt(i);
        i++;
        setTimeout(typer, speed);
      } else {
        el.classList.add("final-typed-text");
        resolve();
      }
    }

    typer();
  });
}

function _remove_context(context_name) {
  const context = document.querySelector(context_name);
  context.remove();
}

function clone_image(param) {
  const el = param.target;
  const clone = el.cloneNode();

  const container = document.querySelector('.jutsu_images_sequence');
  const input = document.querySelector("input[type='hidden']");

  input.value += el.alt + ",";

  container.appendChild(clone);
}

function remove_clones(){
  const elements = document.querySelectorAll('.jutsu_images_sequence img');
  for (const e of elements) e.remove();
  const input = document.querySelector("input[type='hidden']");
  input.value = '';
}

const emojis = ["😳","😂","😎","😍","😛","😭","🥵","🥶","🤡","🥳","🤢","👺","👻","☠","👽","👾","🤖","💩","🙉","🙀","🦄","🐲","🐳","🦆","👀","👌","👏","👋","🎃","🎉","💎","🔊","🔒","⌛","🍫","🍕","🍖","🚗","🚂"];
let cardAmount = 12;

let cards = [];

let flippedCards = 0;

let notPickedEmojis = emojis;
let emojiMap = [];
// Eww
for (let i = 1; i < cardAmount+1; i++) {
  if (i % 2 == 0) {
    console.log("Even!")
    emojiMap.push(emojiMap[i-2]); // ??!
  } else {
    console.log("Odd!")
    const emoji = notPickedEmojis[Math.floor(Math.random() * notPickedEmojis.length)];
    notPickedEmojis = notPickedEmojis.filter((e) => e !== emoji);
    emojiMap.push(emoji);
  }
  console.log(i, emojiMap)
}

// Randomise order of emojis
// I have no idea how this works, but it does
for (let i = emojiMap.length - 1; i > 0; i--) {
  const j = Math.floor(Math.random() * (i + 1));
  [emojiMap[i], emojiMap[j]] = [emojiMap[j], emojiMap[i]];
}

// This is a mess
let i = 0;
while (i < cardAmount) {
  const el = document.createElement("buton");
  el.className = "card";
  el.setAttribute("data-index", i)
  el.setAttribute("data-flipped", true)
  el.setAttribute("disabled", true)
  el.setAttribute("data-locked", false)
  el.addEventListener("click", cardClick);
  const contentEl = document.createElement("span");
  contentEl.setAttribute("class", "card-content");
  contentEl.innerHTML = emojiMap[i];
  el.appendChild(contentEl);
  document.getElementsByTagName("main")[0].appendChild(el);
  cards.push(el);
  i++;
}

// Why is this a seperate function
function cardClick(e) {
  const el = e.target;
  const index = JSON.parse(el.getAttribute("data-index"));
  let flipped = JSON.parse(el.getAttribute("data-flipped"));
  const disabled = JSON.parse(el.getAttribute("disabled"));
  if (disabled) return;
  flippedCards = flippedCards + 1;
  if (flippedCards >= 2) {
    for (card of cards){
      card.setAttribute("disabled", true);
      if (card.children[0].innerHTML == el.children[0].innerHTML) {
        card.setAttribute("data-locked", true);
        el.setAttribute("data-locked", true)
      }
    }
    setTimeout(() => {
      for (card of cards) {
        if (!JSON.parse(card.getAttribute("data-locked"))) {
          card.setAttribute("disabled", false);
          card.setAttribute("data-flipped", false);
        }
      }
      flippedCards = 0;
    }, 1000); // THis is so stupid and ugly
  }
  el.setAttribute("data-flipped", !flipped);
  flipped = !flipped;
  console.log(`Card #${index + 1} is ${flipped ? "now" : "not"} flipped.`);
}


// I hate that I have to do this, but I have to
setTimeout(() => {
  for (card of cards) {
    card.setAttribute("data-flipped", false)
    card.setAttribute("disabled", false)
  }
},1500)

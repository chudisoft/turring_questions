function countSpecialCharacters(word) {
  let specialCount = 0;
  const letters = new Set(word.toLowerCase());

  for (const c of letters) {
    const lower = c;
    const upper = c.toUpperCase();

    if (word.includes(lower) && word.includes(upper)) {
      const firstUpperIndex = word.indexOf(upper);

      // Find all lowercase occurrences indices
      const lowerIndices = [];
      for (let i = 0; i < word.length; i++) {
        if (word[i] === lower) {
          lowerIndices.push(i);
        }
      }

      // Check if all lowercase indices appear before first uppercase index
      if (lowerIndices.every(index => index < firstUpperIndex)) {
        specialCount++;
      }
    }
  }

  return specialCount;
}

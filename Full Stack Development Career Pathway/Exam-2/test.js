const books = [
    {
      title: "The City We Became",
      author: "N. K. Jemisin",
      tags: ["fantasy", "fiction", "afrofutursim", "science fiction", "sci-fi"]
    },
    {
      title: "The Catcher in the Rye",
      author: "J. D. Salinger",
      tags: ["fiction", "young adult", "YA", "realism", "coming of age", "classic"]
    },
    {
      title: "The Hundred Thousand Kingdoms",
      author: "N. K. Jemisin",
      tags: ["fantasy", "fiction", "adventure", "series"]
    },
    {
      title: "Sapiens: A Brief History of Humankind",
      author: "Yuval Noah Harari",
      tags: ["nonfiction", "history", "anthropology", "science", "sociology"]
    },
    {
      title: "Behave: The Biology of Humans at Our Best and Worst",
      author: "Robert M. Sapolsky",
      tags: ["nonfiction", "anthropology", "science", "sociology", "biology"]
    },
    {
      title: "The Parable of the Talents",
      author: "Octavia Butler", 
      tags: ["fiction", "dystopian", "science fiction"]
    },
    {
      title: "1984",
      author: "George Orwell", 
      tags: ["fiction", "dystopian", "science fiction", "classics", "adult"]
    },
    {
      title: "Remarkably Bright Creatures",
      author: "Shelby Van Pelt",
      tags: ["fiction", "mystery", "magical realism"]
    },
    {
      title: "Crying in H Mart",
      author: "Michelle Zauner",
      tags: ["memoir", "nonfiction", "autobiography"]
    },
    {
      title: "Wild: From Lost to Found on the Pacific Crest Trail",
      author: "Cheryl Strayed",
      tags: ["nonfiction", "memoir", "adventure", "travel"]
    }
  ]

const flattenObjectValuesIntoArray = (arrOfObjs) => {
    let flattenedObj;
    const flattenedObjsArr = [];
    for (let obj = 0; obj < arrOfObjs.length; obj++) {
      const objValues = Object.values(arrOfObjs[obj]);
      flattenedObj = [...objValues.flat()]
      flattenedObjsArr.push(flattenedObj)
    }
    return flattenedObjsArr;
  };

  const filterBooks = (searchInput, listOfBooks) => {
    let finalBooksArray = [];
    const flattenedBooks = flattenObjectValuesIntoArray(listOfBooks);
    for (let i = 0; i < flattenedBooks.length; i++) {
      for (let j = 0; j < flattenedBooks[i].length; j++) {
        if (typeof flattenedBooks[i][j] === 'string' && flattenedBooks[i][j].toLowerCase().includes(searchInput.toLowerCase()) && !finalBooksArray.includes(flattenedBooks[i][0])) {
          finalBooksArray.push(flattenedBooks[i][0]);
        }
      }
    }
    return finalBooksArray;
  };

console.log(filterBooks("fantasy", books));

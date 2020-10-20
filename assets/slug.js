//save the title and the slug in a constant variable
const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

//replace every char that isn't a letter to hyphen or replace spaces, and convert all to lower case
const slugify = (val) => {
    return val.toString().toLocaleLowerCase().trim()
    .replace(/&/g, '-and-').replace(/[\s\W-]+/g, '-')
};

titleInput.addEventListener('keyup', (e)=>{
    slugInput.setAttribute('value', slugify(titleInput.value));
});
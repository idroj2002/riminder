mainCategoryButton = document.getElementById('main-category-button');
categoryButtons = document.getElementsByClassName('category-button');
notes = document.getElementsByClassName('note-card');

categorySelector = document.getElementById('category-selector');

mainCategory = 'recetas';

for (i = 0; i < categoryButtons.length; i++) {
    let categoryButton = categoryButtons[i];
    categoryButton.addEventListener('click', () => {
        mainCategoryButton.classList.remove('active');
        for (i = 0; i < categoryButtons.length; i++) {
            categoryButtons[i].classList.remove('active');
        }
        categoryButton.classList.add('active');

        html = "{% if categ|lower == " + categoryButton.innerHTML + " %}";
        categorySelector.innerHTML = html;
    });
}
    
mainCategoryButton.addEventListener('click', ()=> {
    mainCategoryButton.classList.add('active');
    for (i = 0; i < categoryButtons.length; i++) {
        categoryButtons[i].classList.remove('active');
    }
})

if (mainCategory != null){
    trobat = false;
    for (i = 0; i < notes.length; i++) {
        let note = notes[i];
        for (j = 0; j < note.dataset.categories.length; j++) {
            if (mainCategory == note.dataset.categories[j]) {
                trobat = true;
                break;
            }
            console.log(mainCategory)
            console.log(note.dataset.categories)
            if (trobat == false) {
                note.classList.add('hidden');
            }
        }
        trobat = false;
    }
}
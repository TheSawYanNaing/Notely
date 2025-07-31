document.addEventListener("DOMContentLoaded", function()
{
    // Getting all category
    const noteElement = this.querySelectorAll(".note")

    categories = Array.from(noteElement).map(function(note)
    {
        return note.textContent
    })

    // Selecting search inpu
    const input = this.querySelector("#q")

    input.addEventListener("keyup", function()
    {
        const search = this.value.trim()

        if (!search)
        {
            // show all element
            noteElement.forEach(function(note)
            {
                note.style.display = "inline"
            })
        }

        else 
        {
            noteElement.forEach(function(note)
            {
                if (note.textContent.toLowerCase().includes(search.toLowerCase()))
                {
                    note.style.display = "inline"
                }

                else 
                {
                    note.style.display = "none"
                }
            })
        }
    })
})

document.addEventListener("DOMContentLoaded", function()
{
    // Getting all category
    const categoryElement = this.querySelectorAll(".category")

    categories = Array.from(categoryElement).map(function(category)
    {
        return category.textContent
    })

    // Selecting search inpu
    const input = this.querySelector("#q")

    input.addEventListener("keyup", function()
    {
        const search = this.value.trim()

        if (!search)
        {
            // show all element
            categoryElement.forEach(function(category)
            {
                category.style.display = "inline"
            })
        }

        else 
        {
            categoryElement.forEach(function(category)
            {
                if (category.textContent.toLowerCase().includes(search.toLowerCase()))
                {
                    category.style.display = "inline"
                }

                else 
                {
                    category.style.display = "none"
                }
            })
        }
    })
})

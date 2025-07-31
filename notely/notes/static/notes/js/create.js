const form = document.querySelector(".create-form")

function addError(className, message)
{
    const element = document.querySelector(`.${className}`)

    // Creat a sapn
    const newSpan = document.createElement("span")
    newSpan.textContent = message 

    element.append(newSpan)
}

form.addEventListener("submit", function(event)
{
    event.preventDefault()

    // Deleting all older span
    const oldSpans = document.querySelectorAll("span")

    oldSpans.forEach(function(span)
    {
        span.remove()
    })
    
    formData = new FormData(form)

    // Getting input
    const category = formData.get("category").trim()
    const title = formData.get("title").trim()
    const content = formData.get("content").trim()

    if (!category)
    {
        addError("category", "Missing Category")
        return 
    }

    if (!title)
    {
        addError("title", "Missing Title")
        return 
    }

    if (!content)
    {
        addError("content", "Missing Content")
        return 
    }

    form.submit()
})
const PASSWORD_REGEX = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\$\*\#@])[A-Za-z\d\$\*\#@]{5,8}$/;

const form = document.querySelector(".register-form")

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

    // Selecing all span
    const oldSpans = document.querySelectorAll("span")

    oldSpans.forEach(function(span)
    {
        span.remove()
    })

    formData = new FormData(form) 

    const username = formData.get("username")
    const password = formData.get("password")

    if (!username)
    {
        addError("username", "Invalid username")
        return 
    }

    if (!PASSWORD_REGEX.test(password))
    {
        addError("password", "Invalid Password")
        return
    }

    form.submit()
})
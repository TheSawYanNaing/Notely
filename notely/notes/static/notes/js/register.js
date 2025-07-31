const form = document.querySelector(".register-form")

const USERNAME_REGEX = /^[a-zA-Z][a-zA-Z0-9]{4,7}$/;
const PASSWORD_REGEX = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\$\*\#@])[A-Za-z\d\$\*\#@]{5,8}$/;


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
    // Prevent submitting
    event.preventDefault()

    // Getting all of the old span
    const oldSpans = document.querySelectorAll("span")

    oldSpans.forEach(function(oldSpan)
    {
        oldSpan.remove()
    })
    
    // Getting form data
    const formData = new FormData(form)

    // Getting username, email, password and confirmpassword
    const username = formData.get("username")
    const email = formData.get("email")
    const password = formData.get("password")
    const confirmPassword = formData.get("confirmPassword")

    if (!username || !USERNAME_REGEX.test(username))
    {
        addError("username", "User name must starts with a letter and must only contains number and letter 5 to 8 characters")
        return
    }

    if (!email)
    {
        addError("email", "Invalid Email")
        return
    }

    if (!password || !PASSWORD_REGEX.test(password))
    {
        addError("password", "Password must be 5–8 characters long, contain at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character ($ * # @).")
        return 
    }

    if (!confirmPassword || confirmPassword != password)
    {
        addError("confirmPassword", "Password must match")
        return 
    }

    form.submit()
})
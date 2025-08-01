const noteContainer = document.querySelector(".adding")
const createDiv = document.querySelector(".create")
const organize = document.querySelector(".organize")
const access = document.querySelector(".access")
const usageInfo = document.querySelector(".usage-info")

document.addEventListener("DOMContentLoaded", function()
{
    noteContainer.style.opacity = "1"
    noteContainer.style.top = "0"
    createDiv.style.left = "0"
    organize.style.top = "0"
    access.style.left = "0"

    this.addEventListener("scroll", function()
    {
        const windowHeight = window.innerHeight
        const usageInfoRect = usageInfo.getBoundingClientRect()

        if (usageInfoRect.top > 0 && usageInfoRect.top < windowHeight - 100)
        {
            usageInfo.style.opacity = "1"
            usageInfo.style.top = "0"
        }

        else 
        {
            usageInfo.style.opacity = "0"
            usageInfo.style.top = "30px"
        }
    })
})


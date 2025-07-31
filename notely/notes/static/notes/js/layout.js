const menuContainer = document.querySelector(".menu-container")
const menuBar = document.querySelector(".menu-bar")

// Adding event on menuBar
menuBar.addEventListener("click", function()
{
    const height = menuContainer.clientHeight;

    if (height === 0)
    {
        menuContainer.style.height = "130px";
    }

    else 
    {
        menuContainer.style.height = "0"
    }
})
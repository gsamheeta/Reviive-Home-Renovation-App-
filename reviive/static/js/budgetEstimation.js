$(document).ready(function () {
    let totalExpenses = 0;


    // Event handler for the "Add Expense" button click
    $("#addExpense").click(function () {
        const item = $("#item").val();
        const cost = parseFloat($("#cost").val());

        if (!item || isNaN(cost) || cost <= 0) {
            alert("Please enter a valid item and cost.");
            return;
        }

        totalExpenses += cost;

        // Update the total expenses and reset input fields
        $("#totalExpenses").text(totalExpenses.toFixed(2));
        $("#item").val("");
        $("#cost").val("");

        // Create a new list item with entered values, "Edit," and "Delete" buttons beside them
        const newItem = $(`<li data-cost="${cost}">
            <span>${item}: $${cost.toFixed(2)}</span>
            <button class="editExpense">Edit</button>
            <button class="deleteExpense">Delete</button>
        </li>`);

        // Add the expense to the list
        $("#expenseList").append(newItem);
    });

    // Event delegation for editing and deleting
    $("#expenseList").on("click", ".editExpense", function () {
        // Edit the expense item
        const listItem = $(this).closest("li");
        const item = listItem.find('span').text().split(":")[0];
        const cost = parseFloat(listItem.data("cost"));

        const editedItem = prompt("Edit item:", item);
        const editedCost = parseFloat(prompt("Edit cost:", cost));

        if (editedItem && !isNaN(editedCost) && editedCost > 0) {
            totalExpenses -= cost;
            totalExpenses += editedCost;
            listItem.data("cost", editedCost);
            listItem.find('span').text(`${editedItem}: $${editedCost.toFixed(2)}`);
            $("#totalExpenses").text(totalExpenses.toFixed(2));
        }
    });

    $("#expenseList").on("click", ".deleteExpense", function () {
        // Delete the expense item
        const listItem = $(this).closest("li");
        const expenseCost = listItem.data("cost");
        totalExpenses -= expenseCost;
        $("#totalExpenses").text(totalExpenses.toFixed(2));
        listItem.remove();
    });
});

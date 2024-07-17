function getBudgetObject(income, gdp, capita) {
    const budget = {
        income,
        gdp,
        capita,
    };

    return budget;
}

module.exports = getBudgetObject;

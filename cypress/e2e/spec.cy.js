describe('template spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:5000')
  })
})

describe("The correct information for each property is displayed", () => {
  beforeEach(() => {
    cy.visit('http://localhost:5000')
  })
  it("has the correct number of properties displayed on the screen", () => {

    cy.get("p").contains("4")
  })
})
const mockPropertyData = require("../../properties.json")

const mockPropertyAreas  = [111.44, 32.02, 120.00, 38.18]


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

        cy.get("p").contains(`${mockPropertyData.length}`)
    })

    it("has a list of property coordinates for each property", () => {
        cy.get("ul").each(($ul, buildingNo) => {
            cy.wrap($ul).within(($ul) => {
                cy.get("li").each(($li, index) => {
                    cy.wrap($li).should("contain.text", `${mockPropertyData[buildingNo].geometry.coordinates[0][index][0]}, ${mockPropertyData[buildingNo].geometry.coordinates[0][index][1]}`)
                })
            })
        })
    })

    it("each property has the correct OSID displayed", () => {
        cy.get(".property").each((property, propertyNumber) => {
            cy.wrap(property).within(() => {
                cy.get('[data-testId="osid"]').each((osid) => {
                    cy.wrap(osid).should("contain.text", mockPropertyData[propertyNumber].properties.osid)
                })
            })
        })
    })

    it("each property should display the correct date its building age was last updated", () => {
        cy.get(".property").each((property, propertyNumber) => {
            cy.wrap(property).within(() => {
                cy.get('[data-testId="age-last-updated"]').each((age) => {
                    cy.wrap(age).should("contain.text", mockPropertyData[propertyNumber].properties.buildingage_updatedate)
                })
            })
        })
    })

    it("each property should display its area in metres sq", () => {
         cy.get(".property").each((property, index) => {
            cy.wrap(property).within(() => {
                cy.get('[data-testId="area"]').each((age) => {
                    cy.wrap(age).should("contain.text", mockPropertyAreas[index])
                })
            })
        })
    })
})



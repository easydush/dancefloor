import faker from "@faker-js/faker";

export const getFakeDancer = () => {
    return {
        name: faker.name.findName(),
        sex: faker.name.gender(true) === 'Male',
        skills: [
            {
                level: faker.random.arrayElement(['LOW', 'MEDIUM', 'HIGH']),
                dance: faker.random.arrayElement(['hip-hop', 'pop', 'electrodance'])
            }
        ]
    }
}
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        state = []

        for asteroid in asteroids:
            while state and state[-1] > 0 and asteroid < 0:

                if abs(asteroid) > abs(state[-1]):
                    state.pop()
                    continue

                elif abs(asteroid) == abs(state[-1]):
                    state.pop()
                    break

                else:
                    break

            else:
                state.append(asteroid)

        return state
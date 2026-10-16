// Réglages du jeu (mêmes valeurs que la version Roblox).

export const CONFIG = {
  name: 'PROJECT-M13',
  maxPartySize: 4,
  partyCodeLength: 4,
  tickRate: 30,
  snapshotRate: 15,

  player: { health: 100, speed: 16, respawnSeconds: 5, fallDamage: 15 },
  basicAttack: { damage: 8, range: 7, cooldown: 0.45 },

  retenir: { shieldCapacity: 40, shieldSeconds: 4, storedSeconds: 8, slowFactor: 0.8, releaseRadius: 18 },
  rendre: { radius: 25, selfCost: 8, heal: 8 },
  repousser: { deflectSeconds: 3, radius: 14, push: 12, damage: 5, instabilityGain: 12, transferRange: 60 },

  instability: { max: 100, decayPerSecond: 1, minorThreshold: 50, resetAfterMajor: 40 },

  silhouette: { health: 30, speed: 11, damage: 6, attackRange: 4, attackCooldown: 1.2 },
  boss: { baseHealth: 700, perExtraPlayer: 300, speed: 9, slamDamage: 25, slamRadius: 10 },

  waves: { maxAlive: 5, interval: 14 },
};

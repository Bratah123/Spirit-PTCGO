from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import mimic_passive


card = PokemonCardDef(
    guid="7144fd09-dbb5-59f3-bf23-f2a785b68b4c",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Ability(
            title="Mimic",
            game_text="As long as Sudowoodo is your Active Pok\u00e9mon, it copies all of the Defending Pok\u00e9mon's attacks, including their costs. This power can't be used if Sudowoodo is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=mimic_passive,
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)

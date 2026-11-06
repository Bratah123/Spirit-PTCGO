from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import fragrance_trap, fragrance_trap_condition


card = PokemonCardDef(
    guid="17d6460e-a19d-5ea6-b238-e2dd83f63584",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasVictreebel.Name",
    display_name="Erika's Victreebel",
    searchable_by=["Erika's Victreebel", "Stage 2", "ErikasVictreebel"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasWeepinbell.Name",
    family_id=69,
    abilities=[
        Ability(
            title="Fragrance Trap",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, and if your opponent has any Benched Pok\u00e9mon, choose 1 of them and switch it with his or her Active Pok\u00e9mon. This power can't be used if Erika's Victreebel is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=fragrance_trap_condition,
            effect=fragrance_trap,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 3},
            damage=50,
        ),
    ],
)

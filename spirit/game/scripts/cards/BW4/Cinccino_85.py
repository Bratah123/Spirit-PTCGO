from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3a013297-84ba-53df-9241-56b7f4dbaca1",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1", "Cinccino"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="BW4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Ability(
            title="Smooth Coat",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pok\u00e9mon's Echoed Voice attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
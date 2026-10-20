from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="dff407ba-5498-5dff-9e7c-4acfd2b5dbd3",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=99,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Sand Slammer",
            game_text="At any time between turns, if this Pok\u00e9mon is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Flying Beatdown",
            game_text="You may discard a Grass Energy and a Fighting Energy attached to this Pok\u00e9mon. If you do, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)
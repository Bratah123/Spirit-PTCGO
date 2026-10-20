from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b901b866-2d57-54a0-8198-e651bab1bd51",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    display_name="Beheeyem",
    searchable_by=["Beheeyem", "Stage 1", "Team Plasma", "Beheeyem"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=70,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    family_id=605,
    abilities=[
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Damakinesis",
            game_text="Move 6 damage counters from any of your Pok\u00e9mon to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)
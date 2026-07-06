from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e62bc2c7-139b-5741-b864-43ed029d1cab",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1", "Grapploct"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    abilities=[
        Ability(
            title="Stranglehold Master",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon's Retreat Cost is ColorlessColorless more.",
            effect=unimplemented,
        ),
        Attack(
            title="Synchro Buster",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
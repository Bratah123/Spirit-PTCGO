from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a1a37e5d-6891-558e-8c21-b56e8acf183a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=66,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Netherworld Gate",
            game_text="Once during your turn, if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. If you do, put 3 damage counters on this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Screaming Circle",
            game_text="Put 2 damage counters on your opponent's Active Pok\u00e9mon for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)
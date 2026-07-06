from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="100c2dfb-3434-55cb-8d3d-6a4f165c0e58",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatterene.Name",
    display_name="Hatterene",
    searchable_by=["Hatterene", "Stage 2", "Hatterene"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    family_id=856,
    abilities=[
        Ability(
            title="Mind Hat",
            game_text="Once during your turn, you may use this Ability. Each player discards a card from their hand. (Your opponent discards first.)",
            effect=unimplemented,
        ),
        Attack(
            title="Dripping Grudge",
            game_text="Put 1 damage counter on your opponent's Active Pok\u00e9mon for each Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)
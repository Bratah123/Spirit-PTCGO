from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0db247ea-d398-55fa-b13f-dda102ca3033",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=106,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Tempting Tune",
            game_text="Once during your turn, you may search your deck for a Supporter card, reveal it, shuffle your deck, then put that card on top of it.",
            effect=unimplemented,
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=60,
        ),
    ],
)
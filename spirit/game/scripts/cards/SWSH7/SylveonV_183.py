from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1f21bbac-b2ae-5ada-bfac-8a2c382e544d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonV.Name",
    display_name="Sylveon V",
    searchable_by=["Sylveon V", "Basic", "V", "Rapid Strike", "SylveonV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=183,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=700,
    abilities=[
        Ability(
            title="Dream Gift",
            game_text="Once during your turn, you may search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
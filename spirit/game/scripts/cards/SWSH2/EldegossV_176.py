from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ca9186d-2139-5842-aa69-bffe8434071c",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EldegossV.Name",
    display_name="Eldegoss V",
    searchable_by=["Eldegoss V", "Basic", "V", "EldegossV"],
    subtypes=["Basic", "V"],
    collector_number=176,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=830,
    abilities=[
        Ability(
            title="Happy Match",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put a Supporter card from your discard pile into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Float Up",
            game_text="You may shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
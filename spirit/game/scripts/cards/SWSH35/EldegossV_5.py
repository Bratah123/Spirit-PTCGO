from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="38550279-82e4-527e-82f4-6deacda81cac",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EldegossV.Name",
    display_name="Eldegoss V",
    searchable_by=["Eldegoss V", "Basic", "V", "EldegossV"],
    subtypes=["Basic", "V"],
    collector_number=5,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
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
            game_text="You may shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
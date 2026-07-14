from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack, switch_self_attack

card = PokemonCardDef(
    guid="a150ebfb-bccf-5915-acc1-3dfc054fb9cb",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonV.Name",
    display_name="Vaporeon V",
    searchable_by=["Vaporeon V", "Basic", "V", "Rapid Strike", "VaporeonV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=172,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=134,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Splash Jump",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=switch_self_attack(),
        ),
    ],
)
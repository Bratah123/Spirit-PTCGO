from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.attacks_common import bonus_if, has_tool
from spirit.game.session.effects import is_item_card

card = PokemonCardDef(
    guid="505bdf56-6674-52ff-aa9b-743f89d0698b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrRimeV.Name",
    display_name="Galarian Mr. Rime V",
    searchable_by=["Galarian Mr. Rime V", "Basic", "V", "Fusion Strike", "GalarianMrRimeV"],
    subtypes=["Basic", "V", "Fusion Strike"],
    collector_number=49,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=866,
    abilities=[
        Attack(
            title="Surprising Hand",
            game_text="Search your deck for up to 3 Item cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(is_item_card, count=3, minimum=0, reveal=True),
        ),
        Attack(
            title="Customized Cane",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool attached, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=bonus_if(lambda ctx: has_tool(ctx.attacker), 90),
        ),
    ],
)
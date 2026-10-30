from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="cdd8c068-28d5-51cc-b2f5-b04df6b1e856",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    display_name="Zigzagoon",
    searchable_by=["Zigzagoon", "Basic", "Zigzagoon"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=263,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(1),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="f69f13ec-266f-5a98-8e3c-4136f5140eb9",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KangaskhanEX.Name",
    display_name="Kangaskhan-EX",
    searchable_by=["Kangaskhan-EX", "Basic", "EX", "KangaskhanEX"],
    subtypes=["Basic", "EX"],
    collector_number=78,
    set_code="XY2",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Kindred Kick",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
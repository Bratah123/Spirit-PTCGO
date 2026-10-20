from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, flip_damage


card = PokemonCardDef(
    guid="0d5fbb5a-0cad-59d7-a2a4-5725a4f6dd56",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramEX.Name",
    display_name="Reshiram-EX",
    searchable_by=["Reshiram-EX", "Basic", "EX", "ReshiramEX"],
    subtypes=["Basic", "EX"],
    collector_number=36,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Glinting Claw",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Brave Fire",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=flip_damage(tails_self_damage=50),
        ),
    ],
)
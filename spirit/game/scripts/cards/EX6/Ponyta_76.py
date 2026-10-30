from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="8f80eae7-31d4-5d08-8b86-f2299168008d",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic", "Ponyta"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)
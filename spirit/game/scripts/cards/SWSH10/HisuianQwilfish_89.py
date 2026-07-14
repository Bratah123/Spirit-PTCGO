from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="497dad7c-2df9-5d4c-b87d-0daa3a2cf087",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianQwilfish.Name",
    display_name="Hisuian Qwilfish",
    searchable_by=["Hisuian Qwilfish", "Basic", "HisuianQwilfish"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=211,
    abilities=[
        Attack(
            title="Spiny Rush",
            game_text="Flip a coin until you get tails. This attack does 10 damage for each heads.",
            cost={},
            damage=10,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=10),
        ),
    ],
)
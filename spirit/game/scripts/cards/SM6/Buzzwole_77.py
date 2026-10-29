from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.sm6 import sledgehammer

card = PokemonCardDef(
    guid="ce1d0cc1-e95b-54da-8aa2-f2824ca75797",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buzzwole.Name",
    display_name="Buzzwole",
    searchable_by=["Buzzwole", "Basic", "Ultra Beast", "Buzzwole"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=77,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=794,
    abilities=[
        Attack(
            title="Sledgehammer",
            game_text="If your opponent has exactly 4 Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=sledgehammer,
        ),
        Attack(
            title="Swing Around",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)

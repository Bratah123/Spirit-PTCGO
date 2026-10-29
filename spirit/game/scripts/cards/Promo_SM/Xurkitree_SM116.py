from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm6 import cablegram

card = PokemonCardDef(
    guid="6a6abf0b-5eb5-59ba-8b87-ba0f07c7de45",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xurkitree.Name",
    display_name="Xurkitree",
    searchable_by=["Xurkitree", "Basic", "Ultra Beast", "Xurkitree"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=116,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=796,
    abilities=[
        Attack(
            title="Dazzle Blast",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Cablegram",
            game_text="If you have exactly 3 Prize cards remaining, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=cablegram,
        ),
    ],
)

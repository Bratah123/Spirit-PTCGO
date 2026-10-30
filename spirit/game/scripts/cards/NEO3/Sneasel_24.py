from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import swipe


card = PokemonCardDef(
    guid="60a1b825-6658-55f4-a3e8-eaad80c2fa8b",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=215,
    abilities=[
        Attack(
            title="Swipe",
            game_text="Flip a coin. If heads, discard all Trainer cards attached to your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=swipe,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)

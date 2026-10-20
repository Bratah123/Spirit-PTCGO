from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing


card = PokemonCardDef(
    guid="e8906058-dd26-5896-a05b-af4d8699b326",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    display_name="Oshawott",
    searchable_by=["Oshawott", "Basic", "Oshawott"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=501,
    abilities=[
        Attack(
            title="Sleep Pulse",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)
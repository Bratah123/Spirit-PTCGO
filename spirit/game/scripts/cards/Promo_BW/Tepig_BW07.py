from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_bonus


card = PokemonCardDef(
    guid="110171df-54a2-5ebf-8442-b670de1387f8",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    display_name="Tepig",
    searchable_by=["Tepig", "Basic", "Tepig"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=498,
    abilities=[
        Attack(
            title="Singe",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
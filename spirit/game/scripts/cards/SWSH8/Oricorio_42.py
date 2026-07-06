from spirit.game.card_effects.pokemon import LessonInZealPassive, glistening_droplets
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91504f79-cabd-5abc-aa32-b397543a6b24",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Fusion Strike", "Oricorio"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=42,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Ability(
            title="Lesson in Zeal",
            game_text="All of your Fusion Strike Pok\u00e9mon take 20 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance). You can't apply more than 1 Lesson in Zeal Ability at a time.",
            passive=LessonInZealPassive(),
        ),
        Attack(
            title="Glistening Droplets",
            game_text="Put 5 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=glistening_droplets,
        ),
    ],
)
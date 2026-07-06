from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="51e663e4-700f-5619-a1b0-ffbe09ca6c2f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianStunfiskV.Name",
    display_name="Galarian Stunfisk V",
    searchable_by=["Galarian Stunfisk V", "Basic", "V", "GalarianStunfiskV"],
    subtypes=["Basic", "V"],
    collector_number=128,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Ability(
            title="Metal Skin",
            game_text="This Pok\u00e9mon gets +20 HP for each Metal Energy attached to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Trapping Bite",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 12 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)
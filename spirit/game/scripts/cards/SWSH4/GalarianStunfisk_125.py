from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b2d10fb-ccb4-5ded-9437-d7299e3a2c3d",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianStunfisk.Name",
    display_name="Galarian Stunfisk",
    searchable_by=["Galarian Stunfisk", "Basic", "GalarianStunfisk"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Ability(
            title="Counterattack",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Grip and Squeeze",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=unimplemented,
        ),
    ],
)
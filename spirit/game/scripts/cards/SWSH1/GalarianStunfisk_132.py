from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59f91582-85c7-57c7-9fa5-7bc37ce7e13b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianStunfisk.Name",
    display_name="Galarian Stunfisk",
    searchable_by=["Galarian Stunfisk", "Basic", "GalarianStunfisk"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Ability(
            title="Snap Trap",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an opponent's attack (even if it is Knocked Out), discard an Energy from the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Damage Rush",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
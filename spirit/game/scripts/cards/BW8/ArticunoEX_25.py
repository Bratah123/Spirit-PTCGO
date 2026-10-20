from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="4777e539-6f96-5cab-ab7d-9d4a72a90997",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArticunoEX.Name",
    display_name="Articuno-EX",
    searchable_by=["Articuno-EX", "Basic", "EX", "Team Plasma", "ArticunoEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=25,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=spread_damage(10, also_base=True),
        ),
        Attack(
            title="Frost Prison",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)
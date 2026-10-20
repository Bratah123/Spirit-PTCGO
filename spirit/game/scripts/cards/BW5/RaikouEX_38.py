from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ddfcac0-4f28-5d26-8841-60d8d7a7eb53",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaikouEX.Name",
    display_name="Raikou-EX",
    searchable_by=["Raikou-EX", "Basic", "EX", "RaikouEX"],
    subtypes=["Basic", "EX"],
    collector_number=38,
    set_code="BW5",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Thunder Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Volt Bolt",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 100 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7320f688-c15a-54e5-a296-d3e4291cb88e",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianTyphlosionVSTAR.Name",
    display_name="Hisuian Typhlosion VSTAR",
    searchable_by=["Hisuian Typhlosion VSTAR", "VSTAR", "HisuianTyphlosionVSTAR"],
    subtypes=["VSTAR"],
    collector_number=193,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianTyphlosionV.Name",
    family_id=157,
    abilities=[
        Attack(
            title="Hollow Flame",
            game_text="Put 3 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
        Attack(
            title="Shimmering Star",
            game_text="If your opponent's Active Pok\u00e9mon has exactly 4 damage counters on it, that Pok\u00e9mon is Knocked Out. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)